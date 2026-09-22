import sys
from typing import Type
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_client import APIClient
from src.code_withTemplate.prompt_loader import load_prompt
from src.utils.api_client import LocalModelClient


def generate_data(client: Type[APIClient],  topic: str, chart_type: str) -> str:
    """根据主题和图表类型生成数据"""
    prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompts', 'data_generation.txt')
    prompt_template = load_prompt(prompt_path)

    if not prompt_template:
        return "加载 data_generation.txt 失败，请检查文件路径或内容。"

    prompt = prompt_template.replace("{topic}", topic).replace("{chart_type}", chart_type)

    try:
        return client.process_text_query(prompt)
    except Exception:
        return "生成文本失败，请稍后再试。"
    

def generate_data_local_model(topic: str, chart_type: str, local_client: Type[LocalModelClient]) -> str:

    prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompts', 'data_generation.txt')
    prompt_template = load_prompt(prompt_path)

    if not prompt_template:
        return "加载 data_generation.txt 失败，请检查文件路径或内容。"

    prompt = prompt_template.replace("{topic}", topic).replace("{chart_type}", chart_type)

    return local_client.process_text_query(prompt)