import sys
from typing import Type
import os
# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_client import APIClient
from src.code_withTemplate.prompt_loader import load_prompt


def eval_chart(client: Type[APIClient],  image_path: str) -> str:
    """根据主题和图表类型生成数据"""
    prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompts', 'eval_chart.txt')
    prompt_template = load_prompt(prompt_path)

    if not prompt_template:
        return "加载 eval_chart.txt 失败，请检查文件路径或内容。"
    prompt = prompt_template

    # try:
    return client.process_image_query(prompt,image_path)
    # except Exception:
    #     return "生成文本失败，请稍后再试。"

