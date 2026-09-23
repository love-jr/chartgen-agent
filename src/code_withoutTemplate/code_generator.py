"""阶段 ②（不带模板路线）：仅依据数据与图表类型生成 ggplot2 代码。

提示词用 ``code_generation.txt``，不给参考模板；生成后还可交给优化提示词
（``code_optimazation.txt``）按主题/配色进一步改写。
"""
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.stages.optimize import redirect_save_path
from src.stages.paths import WITHOUT_TEMPLATE_PREFIX, sample_png
from src.utils.prompt import PROMPTS_DIR, fill_prompt, load_prompt

PROMPT_PATH = os.path.join(PROMPTS_DIR, "code_generation.txt")
OPTIMIZE_PROMPT_PATH = os.path.join(PROMPTS_DIR, "code_optimazation.txt")

_LOAD_FAILED = "加载提示词失败，请检查文件路径或内容。"
_GEN_FAILED = "生成代码失败，请稍后再试。"


def _generate(prompt, client, png, model_name):
    if not prompt:
        return _LOAD_FAILED
    try:
        return redirect_save_path(client.process_text_query(prompt), png)
    except Exception:
        return _GEN_FAILED


def generate_code_for_chart(client, topic, generated_data, chart_type, title,
                            subtitle):
    """按主题与标题生成绘图代码（本函数不改写输出路径，由调用方处理）。"""
    template = load_prompt(PROMPT_PATH)
    if not template:
        return _LOAD_FAILED
    prompt = fill_prompt(
        template, topic=topic,
        data=json.dumps(generated_data, ensure_ascii=False),
        chart_type=chart_type, title=title, subtitle=subtitle)
    try:
        return client.process_text_query(prompt)
    except Exception:
        return _GEN_FAILED


def generate_code_for_chart_local_model(local_client, topic, generated_data,
                                        chart_type, title, subtitle):
    """同上，改用本地推理模型。"""
    template = load_prompt(PROMPT_PATH)
    if not template:
        return _LOAD_FAILED
    prompt = fill_prompt(
        template, topic=topic,
        data=json.dumps(generated_data, ensure_ascii=False),
        chart_type=chart_type, title=title, subtitle=subtitle)
    try:
        return local_client.process_text_query(prompt)
    except Exception:
        return _GEN_FAILED


def generate_code_for_chart_optimization(model_name, client, chart_theme,
                                         chart_type, color_matching,
                                         generated_code, source, index):
    """按主题配色与数据来源改写代码，并把输出指向本机样本目录。"""
    template = load_prompt(OPTIMIZE_PROMPT_PATH)
    if not template:
        return _LOAD_FAILED
    prompt = fill_prompt(
        template, chart_theme=chart_theme, color_matching=color_matching,
        chart_type=chart_type, source=source, code=generated_code)
    return _generate(prompt, client,
                     sample_png(WITHOUT_TEMPLATE_PREFIX, model_name, index),
                     model_name)
