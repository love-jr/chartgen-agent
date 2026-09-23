

import re
import sys
from typing import Type
import os

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_client import APIClient

from src.code_optimazation.prompt_loader import load_prompt

def optimize_code(client: Type[APIClient],  chart_folder : str , suggestion:str) -> str:
    """根据主题和图表类型生成数据"""
    prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'prompts', 'last_optimazation.txt')
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 last_optimazation.txt 失败，请检查文件路径或内容。"
    
    code_path = os.path.join(chart_folder, 'temp_code.R')
    new_path = os.path.join(chart_folder, 'new_code.R')
    code = load_prompt(code_path)
    if not code:
        return "加载 code 失败，请检查文件路径或内容。"
    
    prompt = prompt_template.replace("{code}", code).replace("{suggestion}", suggestion)
    
    try:
        generated_code= client.process_text_query(prompt)
        return _replace_output_file_path(generated_code, code_path)
    except Exception:
        return "生成文本失败，请稍后再试。"

def _replace_output_file_path(generated_code: str, new_path: str) -> str:
    """替换代码中的 output_file 路径"""
    # 正则表达式匹配 output_file 后面的路径，确保它是一个路径字符串
    output_file_pattern = r"(save_filepath\s*=\s*['\"]).*?(['\"])"
    # 新路径
    new_output_path = f"save_filepath = '{new_path}'"
    print(new_output_path)
    # 使用 re.sub 进行替换
    generated_code = re.sub(output_file_pattern, new_output_path, generated_code)

    return generated_code

