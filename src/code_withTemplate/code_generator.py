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

def generate_code_for_chart(model_name:str, client: Type[APIClient], topic:str, data: str, chart_type: str,template:str, index: int) -> str:
    """根据生成的数据调用 API 生成可视化代码"""
    prompt_path = os.path.join(os.path.dirname(__file__), '..','..','config', 'prompts', 'code_generation_template.txt')
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 code_generation.txt 失败，请检查文件路径或内容。"
    #列表类型转化
    json_data_str = json.dumps(data, ensure_ascii=False)
    # 生成完整的 API 请求
    prompt = prompt_template.replace("{topic}", topic).replace("{data}", json_data_str).replace("{chart_type}", chart_type).replace("{template}", template)
    
    try:
        generated_code = client.process_text_query(prompt)
        generated_code = _replace_output_file_path(generated_code, index,model_name)
        return generated_code
    except Exception:
        return "生成代码失败，请稍后再试。"
    
def generate_code_for_chart_local_model(local_client: Type[LocalModelClient] ,model_dir: str, topic:str, data: str, chart_type: str,template:str, index: int) -> str:
    

    prompt_path = os.path.join(os.path.dirname(__file__), '..','..','config', 'prompts', 'code_generation_template.txt')
    prompt_template = load_prompt(prompt_path)
    if not prompt_template:
        return "加载 code_generation.txt 失败，请检查文件路径或内容。"
    #列表类型转化
    json_data_str = json.dumps(data, ensure_ascii=False)
    # 生成完整的 API 请求
    prompt = prompt_template.replace("{topic}", topic).replace("{data}", json_data_str).replace("{chart_type}", chart_type).replace("{template}", template)
    
    try:
        generated_code = local_client.process_text_query(prompt)
        generated_code = _replace_output_file_path(generated_code, index, model_dir)
        return generated_code
    except Exception:
        return "生成代码失败，请稍后再试。"

def _replace_output_file_path(generated_code: str, index: int, model_name: str) -> str:
    """把生成的 R 代码里的 save_filepath 替换为本机输出路径。"""
    output_file_pattern = r"(save_filepath\s*=\s*['\"]).*?(['\"])"
    chart_path = output_dir(f"chartWithTemplate+{model_name}", f"chart_{index:04d}", "chart.png")
    # R 代码里用正斜杠，避免 Windows 反斜杠被当成转义
    new_output_path = f"save_filepath = '{chart_path.replace(os.sep, '/')}'"
    return re.sub(output_file_pattern, new_output_path, generated_code)
