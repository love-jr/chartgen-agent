"""阶段 ①：图表数据生成与保存。

同一个提示词模板（``config/prompts/data_generation.txt``）既用于 API，
也用于本地模型，二者只差客户端类型。
"""
import json
import os

from src.utils.output import output_dir
from src.utils.prompt import PROMPTS_DIR, fill_prompt, load_prompt

DATA_PROMPT = os.path.join(PROMPTS_DIR, "data_generation.txt")

_LOAD_FAILED = "加载 data_generation.txt 失败，请检查文件路径或内容。"
_GEN_FAILED = "生成文本失败，请稍后再试。"


def _build_prompt(topic: str, chart_type: str) -> str:
    template = load_prompt(DATA_PROMPT)
    if not template:
        return ""
    return fill_prompt(template, topic=topic, chart_type=chart_type)


def generate_data(client, topic: str, chart_type: str) -> str:
    """调用 API 生成图表数据，失败时返回提示字符串。"""
    prompt = _build_prompt(topic, chart_type)
    if not prompt:
        return _LOAD_FAILED
    try:
        return client.process_text_query(prompt)
    except Exception:
        return _GEN_FAILED


def generate_data_local_model(topic: str, chart_type: str, local_client) -> str:
    """用本地推理模型生成图表数据。"""
    prompt = _build_prompt(topic, chart_type)
    if not prompt:
        return _LOAD_FAILED
    return local_client.process_text_query(prompt)


def save_generated_data(generated_data, index: int, prefix: str, model_name: str) -> None:
    """把生成的数据写入 ``<输出根>/<prefix><模型名>/chart_XXXX/chart_info.json``。"""
    folder = output_dir(f"{prefix}{model_name}", f"chart_{index:04d}")
    path = os.path.join(folder, "chart_info.json")
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(generated_data, f, ensure_ascii=False, indent=4)
        print(f"数据已保存为 {path}")
    except OSError as e:
        print(f"保存数据失败: {e}")
