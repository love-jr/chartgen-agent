"""模型客户端：远程 API 与本地推理两种。

密钥由调用方通过 config 传入（config 从环境变量读取，见 ``api_config``），
本模块不接触任何明文凭据。

``torch`` / ``transformers`` 仅在用到本地推理时才导入（见 ``_torch``），
这样只跑 API 的实验无需安装这两个重型依赖。
"""
import base64
import json
import logging
import os
import subprocess
import time
from typing import Dict, List

import httpx
from openai import OpenAI

#: 允许对自签证书的服务端关闭 TLS 校验（默认开启校验）
VERIFY_TLS_ENV = "CHARTGEN_VERIFY_TLS"

_torch = None


def _load_torch():
    """按需导入 torch 与 transformers，返回 ``(torch, AutoTokenizer, AutoModel)``。"""
    global _torch
    if _torch is None:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        _torch = (torch, AutoTokenizer, AutoModelForCausalLM)
    return _torch


def get_free_gpu():
    """返回显存最空闲的 GPU 序号；无 GPU 或取不到信息时返回 None。

    部分机器没有 nvidia-smi（CPU 机器、或未加入 PATH），此时不应中断导入。
    """
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.free,memory.total',
             '--format=csv,nounits,noheader'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
    except Exception:
        return None
    free_memory = []
    for line in result.stdout.strip().splitlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue
        try:
            free_memory.append(int(parts[0]))
        except ValueError:
            continue
    if not free_memory:
        return None
    return free_memory.index(max(free_memory))


def device():
    """本地推理要用的设备；无 torch 时抛 ImportError。"""
    torch, _, _ = _load_torch()
    free_gpu = get_free_gpu()
    if torch.cuda.is_available() and free_gpu is not None:
        return torch.device(f"cuda:{free_gpu}")
    return torch.device("cpu")


def _http_client():
    """构造 httpx 客户端。

    原先无条件 ``verify=False``，等于对全部服务商关闭证书校验。现改为默认
    校验；仅当显式设置 ``CHARTGEN_VERIFY_TLS=0`` 时才关闭。
    """
    if os.environ.get(VERIFY_TLS_ENV, "1").lower() in ("0", "false", "no"):
        return httpx.Client(verify=False)
    return httpx.Client()


class APIClient:
    """OpenAI 兼容接口的客户端（各服务商均走同一 SDK）。"""

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.client = OpenAI(
            base_url=config.api_base,
            api_key=config.api_key,
            http_client=_http_client(),
        )

    def encode_image(self, image_path: str) -> str:
        """将图片编码为 base64。"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def get_response(self, messages: List[Dict], retries: int = 3, delay: int = 1) -> str:
        """请求模型并返回文本，失败时重试 ``retries`` 次。"""
        if retries < 1:
            raise ValueError("retries 至少为 1")
        last_error = None
        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.config.model_version,
                    messages=messages,
                    max_tokens=self.config.max_tokens,
                    temperature=self.config.temperature,
                )
                return response.choices[0].message.content
            except Exception as e:
                last_error = e
                if attempt < retries - 1:
                    time.sleep(delay)
        raise last_error

    def process_text_query(self, prompt: str, system_message: str = "",
                           response_format: dict = None) -> str:
        """文本查询；``response_format`` 用于要求模型返回 JSON。"""
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        params = {
            "model": self.config.model_version,
            "messages": messages,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
        }
        if response_format:
            params["response_format"] = response_format

        try:
            response = self.client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error("文本处理失败: %s", e)
            raise

    def process_image_query(self, prompt: str, image_path: str,
                            system_message: str = "") -> str:
        """图片查询：把本地图片编码后随提示词一起提交。"""
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{self.encode_image(image_path)}"}},
            ],
        })
        return self.get_response(messages)


class LocalModelClient:
    """本地推理客户端，用于 Qwen2.5 系列的对照实验。

    需要额外安装 ``torch`` 与 ``transformers``（见 requirements-local.txt）。
    """

    def __init__(self, model_dir: str, max_tokens: int = 10240,
                 temperature: float = 0.7):
        self.max_tokens = max_tokens
        self.temperature = temperature
        torch, AutoTokenizer, AutoModelForCausalLM = _load_torch()
        self._torch = torch
        self._device = device()
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
            self.model = AutoModelForCausalLM.from_pretrained(model_dir).to(self._device)
        except Exception as e:
            raise ValueError(f"加载模型失败，请检查路径是否正确: {e}") from e

    def process_text_query(self, prompt: str, system_message: str = "",
                           response_format: dict = None):
        """本地生成；``response_format`` 非空时尝试解析为 JSON。"""
        torch = self._torch
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        conversation = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
        input_ids = self.tokenizer(conversation, return_tensors="pt").input_ids.to(self._device)
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=self._device)
        output_ids = self.model.generate(
            input_ids, max_length=self.max_tokens, temperature=self.temperature,
            pad_token_id=self.tokenizer.eos_token_id, attention_mask=attention_mask,
        )
        text = self.tokenizer.decode(output_ids[0][input_ids.shape[1]:],
                                     skip_special_tokens=True)
        if response_format:
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return {"error": "生成的文本不是有效的 JSON", "raw_output": text}
        return text
