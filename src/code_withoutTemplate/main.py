"""不带模板路线：批量生成图表。

流程：随机选主题、图表类型、主题配色 → 生成数据 → 生成代码 → 按配色优化
代码 → Rscript 出图。对应论文中「不给参考模板」的一组实验。

用法：
    cd src/code_withoutTemplate && python main.py
输出目录由 CHARTGEN_OUTPUT_DIR 决定，默认在项目根目录的 output/ 下。
"""
import os
import random
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from config.list import chart_themes, chart_types, color_matchings, topics
from src.code_withoutTemplate.code_generator import (
    generate_code_for_chart, generate_code_for_chart_optimization)
from src.stages.data import generate_data, save_generated_data
from src.stages.execute import run_r_code
from src.stages.paths import WITHOUT_TEMPLATE_PREFIX, sample_dir
from src.stages.pipeline import parse_response, run_batch
from src.utils.api_config import APIConfig, APIConfig1
from src.utils.api_client import APIClient

MODEL_NAME = "gpt-4o"       # 用于区分输出子目录
NUM_ITERATIONS = 50         # 生成次数，可调大
MAX_WORKERS = 64


def generate_and_process(client, optimizer_client, index, model_name):
    """生成一条数据，产出代码并优化后执行出图。"""
    topic = random.choice(topics)
    chart_type = random.choice(chart_types)
    chart_theme = random.choice(chart_themes)
    color_matching = random.choice(color_matchings)

    payload, err = parse_response(generate_data(client, topic, chart_type))
    if payload is None:
        return index, err

    save_generated_data(payload["Data"], index, WITHOUT_TEMPLATE_PREFIX, model_name)

    draft = generate_code_for_chart(
        client, topic, payload["Data"], chart_type,
        payload["Main Title"], payload["Subtitle"])
    optimized = generate_code_for_chart_optimization(
        model_name, optimizer_client, chart_theme, chart_type, color_matching,
        draft, payload["Data Source"], index)

    try:
        run_r_code(optimized, sample_dir(WITHOUT_TEMPLATE_PREFIX, model_name, index))
    except Exception as e:
        return index, f"出图失败: {e}"
    return index, ""


def main():
    client = APIClient(APIConfig())
    optimizer_client = APIClient(APIConfig1())
    run_batch(range(1, NUM_ITERATIONS + 1),
              lambda i: generate_and_process(client, optimizer_client, i, MODEL_NAME),
              max_workers=MAX_WORKERS)


if __name__ == "__main__":
    main()
