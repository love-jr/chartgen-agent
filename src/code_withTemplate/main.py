"""带模板的图表生成流程。

流程：随机选主题与图表类型 → 生成数据 → 生成 ggplot2 代码 → Rscript 出图。
输出目录由 CHARTGEN_OUTPUT_DIR 决定，默认在项目根目录的 output/ 下。
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import json
import sys

from data_generator import generate_data
from data_saver import save_generated_data
from code_generator import generate_code_for_chart
from code_executor import _sanitize_output_r

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from config.list import (
    chart_types, topics,
    Single_broken_line, multiple_broken_lines,
    Single_broken_line_dotted, multiple_broken_lines_dotted,
    Single_Pie_Chart, simple_bar_chart, paired_bar_chart,
    simple_column_chart, paired_column_chart,
)
from src.utils.api_config import APIConfig
from src.utils.api_client import APIClient

# 图表类型 -> 该类型的模板列表
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

# 各图表类型的选取概率，顺序与 chart_types 一致
CHART_WEIGHTS = [0.1, 0.15, 0.1, 0.15, 0.04, 0.1, 0.13, 0.1, 0.13]

MODEL_NAME = "gpt-4o"       # 用于区分输出子目录
NUM_ITERATIONS = 3500       # 生成次数，首次试跑请调小
MAX_WORKERS = 256


def generate_and_process(client, index, model_name):
    """生成一条数据及其图表代码并执行出图。"""
    topic = random.choice(topics)
    chart_type = random.choices(chart_types, weights=CHART_WEIGHTS, k=1)[0]

    templates = CHART_TEMPLATES.get(chart_type)
    if not templates:
        print(f"未知图表类型：{chart_type}")
        return
    template = random.choice(templates)

    response_text = generate_data(client, topic, chart_type)
    try:
        json_text = response_text.split("<output_begining>")[1].split("<output_ending>")[0].strip()
        data = json.loads(json_text)
    except (IndexError, json.JSONDecodeError, AttributeError) as e:
        print(f"[{index:04d}] 数据解析失败：{type(e).__name__}: {e}")
        return

    save_generated_data(data["Data"], index, model_name)

    generated_code = generate_code_for_chart(
        model_name, client, topic, data, chart_type, template, index)
    _sanitize_output_r(generated_code, index, model_name)


def main():
    client = APIClient(APIConfig())

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(generate_and_process, client, i, MODEL_NAME)
                   for i in range(1, NUM_ITERATIONS + 1)]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"任务失败: {e}")


if __name__ == "__main__":
    main()
