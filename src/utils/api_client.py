import base64
import time
from typing import List, Dict
import logging
from openai import OpenAI
import httpx
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import subprocess
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
    lines = [ln for ln in result.stdout.strip().splitlines() if ln.strip()]
    free_memory = []
    for mem in lines:
        parts = mem.split(',')
        if len(parts) < 2:
            continue
        try:
            free_memory.append(int(parts[0]))
        except ValueError:
            continue
    if not free_memory:
        return None
    return free_memory.index(max(free_memory))


_free_gpu = get_free_gpu()
device = torch.device(
    f"cuda:{_free_gpu}" if (torch.cuda.is_available() and _free_gpu is not None) else "cpu")
class APIClient:
    """API客户端类"""
    def __init__(self, config):
        """初始化API客户端"""
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        self.client = OpenAI(
            base_url=config.api_base,
            api_key=config.api_key,
            http_client=httpx.Client(verify=False)  # 添加verify=False
        )

    def encode_image(self, image_path: str) -> str:
        """将图片编码为base64格式"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            self.logger.error(f"图片编码失败: {str(e)}")
            raise

    def get_response(self, messages: List[Dict], retries: int = 3, delay: int = 1) -> str:
        """获取GPT响应"""
        last_error = None
        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.config.model_version,
                    messages=messages,
                    max_tokens=self.config.max_tokens,
                    temperature=self.config.temperature
                )
                return response.choices[0].message.content
            except Exception as e:
                last_error = e
                if attempt < retries - 1:
                    time.sleep(delay)
                    continue
        raise last_error

    def process_text_query(self, prompt: str, system_message: str = "", response_format: dict = None) -> str:
        """处理文本查询"""
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        try:
            # 构建API调用参数
            params = {
                "model": self.config.model_version,
                "messages": messages,
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature
            }
            
            # 如果提供了response_format，添加到参数中
            if response_format:
                params["response_format"] = response_format
            
            response = self.client.chat.completions.create(**params)
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"文本处理失败: {str(e)}")
            raise

    def process_image_query(self, prompt: str, image_path: str, system_message: str = "") -> str:
        """处理图片相关的查询"""
        base64_image = self.encode_image(image_path)

        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})

        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{base64_image}"}
                }
            ]
        })

        return self.get_response(messages)




class LocalModelClient:
    def __init__(self, model_dir: str, max_tokens: int = 10240, temperature: float = 0.7):
        self.model_dir = model_dir
        self.max_tokens = max_tokens
        self.temperature = temperature

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
            self.model = AutoModelForCausalLM.from_pretrained(model_dir).to(device)
        except Exception as e:
            raise ValueError(f"加载模型失败，请检查路径是否正确: {e}")

    def process_text_query(self, prompt: str, system_message: str = "", response_format: dict = None) -> str:
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        conversation_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

        input_ids = self.tokenizer(conversation_text, return_tensors="pt").input_ids.to(device)
        input_length = input_ids.shape[1]
        attention_mask = torch.ones(input_ids.shape,dtype=torch.long,device=device)
        output_ids = self.model.generate(
            input_ids, max_length=self.max_tokens, temperature=self.temperature,
            pad_token_id=self.tokenizer.eos_token_id, attention_mask=attention_mask   
        )
        generated_tokens = output_ids[0][input_length:]
        output_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        
        if response_format:
            try:
                return json.loads(output_text)
            except json.JSONDecodeError:
                return {"error": "生成的文本不是有效的 JSON", "raw_output": output_text}

        return output_text
