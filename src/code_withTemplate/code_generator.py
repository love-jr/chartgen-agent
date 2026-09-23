"""阶段 ②（带模板路线）：依据数据与「图表类型 → 模板」生成 ggplot2 代码。

与不带模板路线的唯一区别是提示词用 ``code_generation_template.txt``，
并把该图表类型下的一个参考模板一并交给模型。
"""
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.stages.optimize import redirect_save_path
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_png
from src.utils.prompt import PROMPTS_DIR, fill_prompt, load_prompt

PROMPT_PATH = os.path.join(PROMPTS_DIR, "code_generation_template.txt")

_LOAD_FAILED = "加载 code_generation_template.txt 失败，请检查文件路径或内容。"
_GEN_FAILED = "生成代码失败，请稍后再试。"


def _build_prompt(topic, data, chart_type, template):
    template_text = load_prompt(PROMPT_PATH)
    if not template_text:
        return ""
    return fill_prompt(
        template_text, topic=topic, data=json.dumps(data, ensure_ascii=False),
        chart_type=chart_type, template=template)


def generate_code_for_chart(client, topic, data, chart_type, template, index,
                            model_name, prefix=WITH_TEMPLATE_PREFIX):
    """生成绘图代码并改写输出路径到本机。"""
    prompt = _build_prompt(topic, data, chart_type, template)
    if not prompt:
        return _LOAD_FAILED
    try:
        code = client.process_text_query(prompt)
    except Exception:
        return _GEN_FAILED
    return redirect_save_path(code, sample_png(prefix, model_name, index))


def generate_code_for_chart_local_model(local_client, model_dir, topic, data,
                                        chart_type, template, index,
                                        prefix=WITH_TEMPLATE_PREFIX):
    """同上，改用本地推理模型。"""
    prompt = _build_prompt(topic, data, chart_type, template)
    if not prompt:
        return _LOAD_FAILED
    try:
        code = local_client.process_text_query(prompt)
    except Exception:
        return _GEN_FAILED
    return redirect_save_path(code, sample_png(prefix, model_dir, index))
