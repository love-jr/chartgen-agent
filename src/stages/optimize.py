"""阶段 ③ 的「优化」部分：依据评语改写绘图代码。

读取样本目录中上一版 R 代码，连同评语交给模型重写，并把产出路径指向同一
张图，从而原地覆盖。提示词见 ``config/prompts/last_optimazation.txt``。
"""
import os
import re

from src.utils.prompt import PROMPTS_DIR, fill_prompt, load_prompt

OPTIMIZE_PROMPT = os.path.join(PROMPTS_DIR, "last_optimazation.txt")

_SOURCE_FILE = "temp_code.R"

_SAVE_PATH = re.compile(r"(save_filepath\s*=\s*['\"]).*?(['\"])")


def redirect_save_path(code: str, png_path: str) -> str:
    """把代码里的 ``save_filepath`` 指到本机路径（R 里用正斜杠）。"""
    return _SAVE_PATH.sub(
        lambda m: f"save_filepath = '{png_path.replace(os.sep, '/')}'", code)


def optimize_code(client, folder: str, suggestion: str, png_path: str) -> str:
    """依据评语优化 ``folder/temp_code.R``，返回改写后的代码。

    调用方负责执行与落盘（见 ``stages.execute.run_r_code``）。
    """
    template = load_prompt(OPTIMIZE_PROMPT)
    if not template:
        return ""
    source = load_prompt(os.path.join(folder, _SOURCE_FILE))
    if not source:
        return ""

    prompt = fill_prompt(template, code=source, suggestion=suggestion)
    try:
        return redirect_save_path(client.process_text_query(prompt), png_path)
    except Exception:
        return ""
