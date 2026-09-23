import re
import sys
from typing import Type
import os
import json

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_client import APIClient, LocalModelClient
from src.utils.output import output_dir

from src.code_withTemplate.prompt_loader import load_prompt

def generate_code_for_chart(client: Type[APIClient], topic:str, generated_data: str, chart_type: str, title:str,subtitle:str) -> str:
    """根据生成的数据调用 API 生成可视化代码"""
    prompt_path = os.path.join(os.path.dirname(__file__), '..','..','config', 'prompts', 'code_generation.txt')
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 code_generation.txt 失败，请检查文件路径或内容。"
    #列表类型转化
    json_data_str = json.dumps(generated_data, ensure_ascii=False)
    # 生成完整的 API 请求
    prompt = prompt_template.replace("{topic}", topic).replace("{data}", json_data_str).replace("{chart_type}", chart_type).replace("{title}", title).replace("{subtitle}", subtitle)
    
    try:
        generated_code = client.process_text_query(prompt)
        return generated_code
    except Exception:
        return "生成代码失败，请稍后再试。"
    

def generate_code_for_chart_local_model(local_client:Type[LocalModelClient], topic:str, generated_data: str, chart_type: str, title:str,subtitle:str) -> str:

    prompt_path = os.path.join(os.path.dirname(__file__), '..','..','config', 'prompts', 'code_generation.txt')
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 code_generation.txt 失败，请检查文件路径或内容。"
    #列表类型转化
    json_data_str = json.dumps(generated_data, ensure_ascii=False)
    # 生成完整的 API 请求
    prompt = prompt_template.replace("{topic}", topic).replace("{data}", json_data_str).replace("{chart_type}", chart_type).replace("{title}", title).replace("{subtitle}", subtitle)
    
    try:
        generated_code = local_client.process_text_query(prompt)

        return generated_code
    except Exception:
        return "生成代码失败，请稍后再试。"

def generate_code_for_chart_optimization(model_name : str, client: Type[APIClient],chart_theme:str, chart_type: str, color_matching: str,generated_code,source:str, index: int) -> str:
    """优化生成的代码"""
    
    prompt_path = os.path.join(os.path.dirname(__file__), '..','..','config', 'prompts', 'code_optimazation.txt')
    
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 code_optimazation.txt 失败，请检查文件路径或内容。"
    # 生成完整的 API 请求
    prompt = prompt_template.replace("{chart_theme}", chart_theme).replace("{color_matching}", color_matching).replace("{chart_type}", chart_type).replace("{source}", source).replace("{code}",generated_code)

    try:
        optimized_code = client.process_text_query(prompt)
        optimized_code = _replace_output_file_path(optimized_code, index, model_name)
        return optimized_code

    except Exception:
        return "生成代码失败，请稍后再试。"

def _replace_output_file_path(generated_code: str, index: int, model_name: str) -> str:
    """把生成的 R 代码里的 save_filepath 替换为本机输出路径。"""
    output_file_pattern = r"(save_filepath\s*=\s*['\"]).*?(['\"])"
    chart_path = output_dir(f"chart+{model_name}", f"chart_{index:04d}", "chart.png")
    # R 代码里用正斜杠，避免 Windows 反斜杠被当成转义
    new_output_path = f"save_filepath = '{chart_path.replace(os.sep, '/')}'"
    return re.sub(output_file_pattern, new_output_path, generated_code)
