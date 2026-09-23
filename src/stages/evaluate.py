"""阶段 ③ 的「评估」部分：对成图打分。

五个维度各 0–2 分、共 10 分，分别对应 Cleveland 认知感知理论、Tufte 数据
墨水比、Web 内容无障碍指南、孟塞尔色彩体系与 UI 设计规范。评分提示词见
``config/prompts/eval_chart.txt``。
"""
import json
import os
import re

from src.utils.prompt import PROMPTS_DIR, load_prompt

EVAL_PROMPT = os.path.join(PROMPTS_DIR, "eval_chart.txt")

#: 五个评分维度（与提示词和 results.txt 保持一致）
DIMENSIONS = ("Expression", "Aesthetic", "Readability", "Color", "Layout")

_FENCED = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.S)


def eval_chart(client, image_path: str) -> str:
    """把成图交给视觉模型打分，返回原始回复文本。"""
    prompt = load_prompt(EVAL_PROMPT)
    if not prompt:
        return "加载 eval_chart.txt 失败，请检查文件路径或内容。"
    try:
        return client.process_image_query(prompt, image_path)
    except Exception:
        return "生成文本失败，请稍后再试。"


def parse_scores(response: str, default: float = 0.0):
    """解析评分回复。

    返回 ``(scores, suggestion)``，其中 ``scores`` 为六个键的字典
    （五个维度 + ``Total``）。解析失败返回 ``(None, "")``。
    """
    text = response.strip()
    fenced = _FENCED.match(text)
    if fenced:
        text = fenced.group(1)
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, AttributeError):
        return None, ""

    scores = {dim: float(data.get(dim, default)) for dim in DIMENSIONS}
    scores["Total"] = sum(scores.values())
    return scores, data.get("suggestion", "")
