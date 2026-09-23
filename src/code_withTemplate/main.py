"""带模板路线：批量生成图表。

流程：随机选主题与图表类型 → 生成数据 → 生成 ggplot2 代码 → Rscript 出图。
对应论文中「给定参考模板」的一组实验。

用法：
    cd src/code_withTemplate && python main.py
输出目录由 CHARTGEN_OUTPUT_DIR 决定，默认在项目根目录的 output/ 下。
"""
import os
import random
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from config.list import (
    chart_types, topics,
    Single_broken_line, multiple_broken_lines,
    Single_broken_line_dotted, multiple_broken_lines_dotted,
    Single_Pie_Chart, simple_bar_chart, paired_bar_chart,
    simple_column_chart, paired_column_chart,
)
from src.code_withTemplate.code_generator import generate_code_for_chart
from src.stages.data import generate_data, save_generated_data
from src.stages.execute import run_r_code
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_dir
from src.stages.pipeline import parse_response, run_batch
from src.utils.api_config import APIConfig
from src.utils.api_client import APIClient

#: 图表类型 -> 该类型的参考模板列表
CHART_TEMPLATES = {
    "Single broken line": Single_broken_line,
    "multiple broken lines (3 to 5 lines)": multiple_broken_lines,
    "single broken line represented by a dotted line": Single_broken_line_dotted,
    "multiple broken lines represented by dotted lines": multiple_broken_lines_dotted,
    "Single Pie Chart": Single_Pie_Chart,
    "simple bar chart (horizontal)": simple_bar_chart,
    "paired bar chart (horizontal)": paired_bar_chart,
    "simple column chart (vertical)": simple_column_chart,
    "paired column chart (vertical)": paired_column_chart,
}

#: 各图表类型的选取概率，顺序与 chart_types 一致
CHART_WEIGHTS = [0.1, 0.15, 0.1, 0.15, 0.04, 0.1, 0.13, 0.1, 0.13]

MODEL_NAME = "gpt-4o"       # 用于区分输出子目录
NUM_ITERATIONS = 3500       # 生成次数，首次试跑请调小
MAX_WORKERS = 64


def generate_and_process(client, index, model_name):
    """生成一条数据及其图表代码并执行出图。"""
    topic = random.choice(topics)
    chart_type = random.choices(chart_types, weights=CHART_WEIGHTS, k=1)[0]
    template = random.choice(CHART_TEMPLATES[chart_type])

    payload, err = parse_response(generate_data(client, topic, chart_type))
    if payload is None:
        return index, err

    save_generated_data(payload["Data"], index, WITH_TEMPLATE_PREFIX, model_name)

    code = generate_code_for_chart(
        client, topic, payload, chart_type, template, index, model_name)
    try:
        run_r_code(code, sample_dir(WITH_TEMPLATE_PREFIX, model_name, index))
    except Exception as e:
        return index, f"出图失败: {e}"
    return index, ""


def main():
    client = APIClient(APIConfig())
    run_batch(range(1, NUM_ITERATIONS + 1),
              lambda i: generate_and_process(client, i, MODEL_NAME),
              max_workers=MAX_WORKERS)


if __name__ == "__main__":
    main()
