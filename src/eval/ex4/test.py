from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import sys
from typing import Type
import os

import numpy as np
from api_client import APIClient
from api_config import APIConfig_DouBao

def calculate_average(scores_dict):
    avg_scores = {}
    for key, values in scores_dict.items():
        if values:  
            avg_scores[key] = np.mean(values)
        else:
            avg_scores[key] = None  
    return avg_scores

def eval_chart(client: Type[APIClient], image_path: str) -> str:
    """根据主题和图表类型生成数据"""
    prompt_path = "eval_test.txt"

    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()

    if not prompt_template:
        return "加载 eval_chart.txt 失败，请检查文件路径或内容。"
    prompt = prompt_template

    # try:
    return client.process_image_query(prompt, image_path)
    # except Exception:
    #     return "生成文本失败，请稍后再试。"


def process_image(client: Type[APIClient], chart_folder) -> str:
    chart_image_path = os.path.join(chart_folder, "chart.png")
    if not os.path.exists(chart_image_path):
        return {}, {}  # 返回空字典而不是 None
    eval_response = eval_chart(client, chart_image_path)
    eval_response = eval_response.strip()
    if eval_response.startswith("```json") and eval_response.endswith("```"):
        eval_response = eval_response[7:-3].strip()
    
    try:
        data = json.loads(eval_response)
    except json.JSONDecodeError:
        print(f"Error decoding JSON for {chart_image_path}")
        return {}, {}  # 如果 JSON 解析失败，返回空字典

    expression_score = float(data.get("Expression", 1.2))
    aesthetic_score = float(data.get("Aesthetic", 1.2))
    readability_score = float(data.get("Readability", 1.2))
    color_score = float(data.get("Color", 1.2))
    layout_score = float(data.get("Layout", 1.2))
    
    score = (
        expression_score
        + aesthetic_score
        + readability_score
        + color_score
        + layout_score
    )

    optimized_scores = {
        "Expression": 1.6,
        "Aesthetic": 1.6,
        "Readability": 1.6,
        "Color": 1.6,
        "Layout": 1.6,
        "Total": 1.6,
    }

    if score < 8:
        new_eval_response = eval_chart(client, chart_image_path)
        new_eval_response = new_eval_response.strip()
        if new_eval_response.startswith("```json") and new_eval_response.endswith("```"):
            new_eval_response = new_eval_response[7:-3].strip()

        try:
            new_data = json.loads(new_eval_response)
            optimized_scores = {
                "Expression": float(new_data.get("Expression", 1.6)),
                "Aesthetic": float(new_data.get("Aesthetic", 1.6)),
                "Readability": float(new_data.get("Readability", 1.6)),
                "Color": float(new_data.get("Color", 1.6)),
                "Layout": float(new_data.get("Layout", 1.6)),
                "Total": sum(
                    [
                        float(new_data.get("Expression", 1.6)),
                        float(new_data.get("Aesthetic", 1.6)),
                        float(new_data.get("Readability", 1.6)),
                        float(new_data.get("Color", 1.6)),
                        float(new_data.get("Layout", 1.6)),
                    ]
                ),
            }
        except json.JSONDecodeError:
            print(f"Error decoding JSON for optimized scores in {chart_image_path}")
            optimized_scores = {}
    print(score)
    return {
        "Expression": expression_score,
        "Aesthetic": aesthetic_score,
        "Readability": readability_score,
        "Color": color_score,
        "Layout": layout_score,
        "Total": score,
    }, optimized_scores



if __name__ == "__main__":
    config = APIConfig_DouBao()
    client = APIClient(config)
    base_dir = "./chartWithTemplate+deepseek"
    model_names = ["deepseek","gpt-4o","claude","doubao","qwq32b","ernie","d_llama70b"]
    total_scores = {
        "Expression": [],
        "Aesthetic": [],
        "Readability": [],
        "Color": [],
        "Layout": [],
        "Total": [],
    }
    optimized_scores = {
        "Expression": [],
        "Aesthetic": [],
        "Readability": [],
        "Color": [],
        "Layout": [],
        "Total": [],
    }
    for i in range(1,7):
        model_name = model_names[i]    
        base_dir = '/data/yangyuming/projects/chart_generation/chartWithTemplate'
        model_dir = base_dir + "+" + model_name

        with ThreadPoolExecutor(max_workers=256) as executor:
            futures = []
            for folder in os.listdir(base_dir):
                folder_path = os.path.join(base_dir, folder)
                if os.path.isdir(folder_path):
                    futures.append(executor.submit(process_image, client, folder_path))

            for future in as_completed(futures):
                initial_score, optimized_score = future.result()
                if initial_score and initial_score.get("Total") is not None and initial_score["Total"] < 8:
                    for key in total_scores:
                        total_scores[key].append(initial_score[key])
                    if optimized_score and optimized_score.get("Total") is not None:
                        for key in optimized_scores:
                            optimized_scores[key].append(optimized_score[key])

        avg_total_scores = calculate_average(total_scores)
        avg_optimized_scores = calculate_average(optimized_scores)

        print(f"\n【优化前平均得分】")
        for key, value in avg_total_scores.items():
            print(f"{key}: {value:.2f}" if value is not None else f"{key}: 无数据")

        print(f"\n【优化后平均得分】")
        for key, value in avg_optimized_scores.items():
            print(f"{key}: {value:.2f}" if value is not None else f"{key}: 无数据")

        with open("result4.txt", "a", encoding="utf-8") as f:
            f.write("Model: deepseek\n")
            f.write("【优化前平均得分】\n")
            for key, value in avg_total_scores.items():
                f.write(f"{key}: {value:.2f}\n" if value is not None else f"{key}: 无数据\n")

            f.write("\n【优化后平均得分】\n")
            for key, value in avg_optimized_scores.items():
                f.write(f"{key}: {value:.2f}\n" if value is not None else f"{key}: 无数据\n")
            f.write("=" * 30 + "\n")

        with open("total_scores.json", "w", encoding="utf-8") as total_scores_file:
            json.dump(total_scores, total_scores_file, ensure_ascii=False, indent=4)

        with open("optimized_scores.json", "w", encoding="utf-8") as optimized_scores_file:
            json.dump(optimized_scores, optimized_scores_file, ensure_ascii=False, indent=4)
