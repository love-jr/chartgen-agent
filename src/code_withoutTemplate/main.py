"""不带模板的图表生成流程。

流程：随机选主题、图表类型、主题配色 → 生成数据 → 生成代码 → 优化代码 → Rscript 出图。
输出目录由 CHARTGEN_OUTPUT_DIR 决定，默认在项目根目录的 output/ 下。
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import json
import sys

from data_generator import generate_data
from data_saver import save_generated_data
from code_generator import generate_code_for_chart, generate_code_for_chart_optimization
from code_executor import _sanitize_output_r

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from config.list import chart_themes, chart_types, color_matchings, topics
from src.utils.api_config import APIConfig
from src.utils.api_config1 import APIConfig1
from src.utils.api_client import APIClient

MODEL_NAME = "gpt-4o"       # 用于区分输出子目录
NUM_ITERATIONS = 50         # 生成次数，可调大
MAX_WORKERS = 256


def generate_and_process(client, optimizer_client, index, model_name):
    """生成一条数据，产出代码并优化后执行出图。"""
    topic = random.choice(topics)
    chart_type = random.choice(chart_types)
    chart_theme = random.choice(chart_themes)
    color_matching = random.choice(color_matchings)

    response_text = generate_data(client, topic, chart_type)
    try:
        json_text = response_text.split("<output_begining>")[1].split("<output_ending>")[0].strip()
        data = json.loads(json_text)
    except (IndexError, json.JSONDecodeError, AttributeError) as e:
        print(f"[{index:04d}] 数据解析失败：{type(e).__name__}: {e}")
        return

    save_generated_data(data["Data"], index, model_name)

    generated_code = generate_code_for_chart(
        client, topic, data["Data"], chart_type, data["Main Title"], data["Subtitle"])

    optimized_code = generate_code_for_chart_optimization(
        model_name, optimizer_client, chart_theme, chart_type,
        color_matching, generated_code, data["Data Source"], index)

    _sanitize_output_r(optimized_code, index, model_name)


def main():
    client = APIClient(APIConfig())
    optimizer_client = APIClient(APIConfig1())

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(generate_and_process, client, optimizer_client, i, MODEL_NAME)
                   for i in range(1, NUM_ITERATIONS + 1)]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"任务失败: {e}")


if __name__ == "__main__":
    main()
