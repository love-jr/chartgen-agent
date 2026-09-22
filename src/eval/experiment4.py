from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import json
import sys
import subprocess
import threading

import numpy as np

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.code_withTemplate.data_generator import generate_data, generate_data_local_model
from src.code_withTemplate.data_saver import save_generated_data
from src.code_withTemplate.code_generator import generate_code_for_chart,generate_code_for_chart_local_model
from src.code_optimazation.code_executor import _sanitize_output_r
from src.code_optimazation.eval_chart import eval_chart
from src.code_optimazation.optimize_code import optimize_code
from config.list import chart_themes,chart_types,color_matchings,topics,Single_broken_line,multiple_broken_lines,Single_broken_line_dotted,multiple_broken_lines_dotted,Single_Pie_Chart,simple_bar_chart,paired_bar_chart,simple_column_chart,paired_column_chart
from src.utils.api_config import APIConfig
from src.utils.api_config1 import APIConfig1
from src.utils.api_client import APIClient, LocalModelClient
from src.utils.api_config_deepseek import APIConfig_Deepseek
from src.utils.api_config_doubao import APIConfig_DouBao
from src.utils.api_config_qwq32b import APIConfig_QWQ32B
from src.utils.api_config_ernie import APIConfig_ERNIE
from src.eval.count import count_subdirectories



def process_chart(client, chart_folder, model_name):
    """处理每个图表文件夹，进行评估和优化"""
    chart_image_path = os.path.join(chart_folder, 'chart.png')
    if not os.path.exists(chart_image_path):
        return None
    eval_response = eval_chart(client, chart_image_path)
    print(chart_image_path)
    eval_response = eval_response.strip()
    if eval_response.startswith("```json") and eval_response.endswith("```"):
        eval_response = eval_response[7:-3].strip()
    print(eval_response)
    try:
        data = json.loads(eval_response)
        expression_score = float(data.get("Expression", 1.2))
        aesthetic_score = float(data.get("Aesthetic", 1.2))
        readability_score = float(data.get("Readability", 1.2))
        color_score = float(data.get("Color", 1.2))
        layout_score = float(data.get("Layout", 1.2))
        suggestion = data.get('suggestion', "")

        score = expression_score + aesthetic_score + readability_score + color_score + layout_score

    except json.JSONDecodeError:
        print(f"Error decoding JSON: {eval_response}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    optimized_scores = {
        "Expression": None,
        "Aesthetic": None,
        "Readability": None,
        "Color": None,
        "Layout": None,
        "Total": None
    }

    try:
        if score < 7:
            print(f"图表评分为 {score}，需要优化。正在优化 temp_code.R...")
            optimized_code = optimize_code(client, chart_folder, suggestion)

            _sanitize_output_r(optimized_code, chart_folder)

            # 获取优化后图表的评分
            new_eval_response = eval_chart(client, chart_image_path)
            new_eval_response = new_eval_response.strip()
            if new_eval_response.startswith("```json") and new_eval_response.endswith("```"):
                new_eval_response = new_eval_response[7:-3].strip()
            
            try:
                new_data = json.loads(new_eval_response)
                optimized_scores = {
                    "Expression": float(new_data.get("Expression", 1.4)),
                    "Aesthetic": float(new_data.get("Aesthetic", 1.4)),
                    "Readability": float(new_data.get("Readability", 1.4)),
                    "Color": float(new_data.get("Color", 1.4)),
                    "Layout": float(new_data.get("Layout", 1.4)),
                    "Total": sum([
                        float(new_data.get("Expression", 1.4)),
                        float(new_data.get("Aesthetic", 1.4)),
                        float(new_data.get("Readability", 1.4)),
                        float(new_data.get("Color", 1.4)),
                        float(new_data.get("Layout", 1.4))
                    ])
                }
            except json.JSONDecodeError:
                print(f"Error decoding optimized JSON: {new_eval_response}")
            except Exception as e:
                print(f"Error processing optimized chart: {e}")
        else:
            print(f"图表评分为 {score}，无需优化。")

    except Exception as e:
        print(f"处理评估结果时出错: {e}")

    return {
        "Expression": expression_score,
        "Aesthetic": aesthetic_score,
        "Readability": readability_score,
        "Color": color_score,
        "Layout": layout_score,
        "Total": score
    }, optimized_scores
def calculate_average(scores_dict):
    avg_scores = {}
    for key, values in scores_dict.items():
        if values:  
            avg_scores[key] = np.mean(values)
        else:
            avg_scores[key] = None  
    return avg_scores

if __name__ == "__main__":
    config = APIConfig()
    config1 = APIConfig1()
    client = APIClient(config)
    client1 = APIClient(config1)
    config_deepseek = APIConfig_Deepseek()
    client_deepseek = APIClient(config_deepseek)
    config_doubao = APIConfig_DouBao()
    client_doubao = APIClient(config_doubao)
    config_qwq32b = APIConfig_QWQ32B()
    client_qwq32b = APIClient(config_qwq32b)
    config_ernie = APIConfig_ERNIE()
    client_ernie = APIClient(config_ernie)

    clients = [client_deepseek,client,client1,client_doubao,client_qwq32b,client_ernie]
    model_names = ["deepseek","gpt-4o","claude","doubao","qwq32b","ernie","d_llama70b"]
    # model_dirs = ["Qwen2.5-7B-Instruct", "Qwen2.5-1.5B-Instruct"]
    model_dirs = []
    total_scores = [] 
    num_folders = 0



    for i in range(0, 1):
        # c = clients[i]
        model_name = model_names[i]    
        base_dir = '/data/yangyuming/projects/chart_generation/chartWithTemplate'
        model_dir = base_dir + "+" + model_name

        total_scores = {"Expression": [], "Aesthetic": [], "Readability": [], "Color": [], "Layout": [], "Total": []}
        optimized_scores = {"Expression": [], "Aesthetic": [], "Readability": [], "Color": [], "Layout": [], "Total": []}
        with ThreadPoolExecutor(max_workers=1) as executor:
            futures = {}

            for folder in os.listdir(model_dir):
                folder_path = os.path.join(model_dir, folder)
                if os.path.isdir(folder_path):
                    futures[executor.submit(process_chart, client_doubao, folder_path, model_name)] = folder_path


            for future in as_completed(futures):
                try:
                    initial_score, optimized_score = future.result()
                    if initial_score is not None and initial_score["Total"] < 7:
                            for key in total_scores:
                                total_scores[key].append(initial_score[key])

                            if optimized_score["Total"] is not None:
                                for key in optimized_scores:
                                    optimized_scores[key].append(optimized_score[key])

                except Exception as e:
                    print(f"Error processing chart: {e}")

    avg_total_scores = calculate_average(total_scores)
    avg_optimized_scores = calculate_average(optimized_scores)

    print(f"\n【优化前平均得分】")
    for key, value in avg_total_scores.items():
        print(f"{key}: {value:.2f}" if value is not None else f"{key}: 无数据")

    print(f"\n【优化后平均得分】")
    for key, value in avg_optimized_scores.items():
        print(f"{key}: {value:.2f}" if value is not None else f"{key}: 无数据")

    with open("result4.txt", "a", encoding="utf-8") as f:
        f.write(f"Model: {model_name}\n")
        f.write("【优化前平均得分】\n")
        for key, value in avg_total_scores.items():
            f.write(f"{key}: {value:.2f}\n" if value is not None else f"{key}: 无数据\n")

        f.write("\n【优化后平均得分】\n")
        for key, value in avg_optimized_scores.items():
            f.write(f"{key}: {value:.2f}\n" if value is not None else f"{key}: 无数据\n")
        f.write("=" * 30 + "\n")