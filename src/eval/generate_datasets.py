from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import json
import shutil
import sys
import subprocess

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.code_withTemplate.data_generator import generate_data, generate_data_local_model
from src.code_withTemplate.data_saver import save_generated_data
from src.code_withTemplate.code_generator import generate_code_for_chart,generate_code_for_chart_local_model
from src.code_withTemplate.code_executor import _sanitize_output_r
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

def select_chart_list(chart_topic):
    if chart_topic == "Single broken line":
        return Single_broken_line
    elif chart_topic == "multiple broken lines (3 to 5 lines)":
        return multiple_broken_lines
    elif chart_topic == "single broken line represented by a dotted line":
        return Single_broken_line_dotted
    elif chart_topic == "multiple broken lines represented by dotted lines":
        return multiple_broken_lines_dotted
    elif chart_topic == "Single Pie Chart":
        return Single_Pie_Chart
    elif chart_topic == "simple bar chart (horizontal)":
        return simple_bar_chart
    elif chart_topic == "paired bar chart (horizontal)":
        return paired_bar_chart
    elif chart_topic == "simple column chart (vertical)":
        return simple_column_chart
    elif chart_topic == "paired column chart (vertical)":
        return paired_column_chart
    else:
        return None


# 指定每个图表类型的选取概率（权重）
weights = [0.1, 0.15, 0.1, 0.15, 0.04, 0.1, 0.13, 0.1, 0.13]


def generate_and_process(client,i,model_name):
    topic=random.choice(topics)
    generated_data = None
    # 按照指定的权重随机选择一个图表类型
    chart_type = random.choices(chart_types, weights=weights, k=1)[0]  

    selected_chart_list =select_chart_list(chart_type)
    #print(select_chart_list)
    template=random.choice(selected_chart_list)
    # print(template)
    response_text = generate_data(client, topic, chart_type)

    json_text = response_text.split("<output_begining>")[1].split("<output_ending>")[0].strip()
   
    # print(response_text)
    try:
        data = json.loads(json_text)
        # title=data["Main Title"]
        # subtitle=data["Subtitle"]
        generated_data=data["Data"]
        # source=(data["Data Source"])
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    
    #保存生成的数据
    save_generated_data(generated_data, i, model_name)
    
    # 生成图表代码 
    generated_code = generate_code_for_chart(model_name, client, topic, data, chart_type, template, i)

    #执行代码
    _sanitize_output_r(generated_code, i, model_name)

def process_chart(client, chart_folder):
    
    """处理每个图表文件夹，进行评估和优化"""
    # 获取图表的评估结果
    chart_image_path = os.path.join(chart_folder, 'chart.png')
    eval_response = eval_chart(client, chart_image_path)

    # Ensure the eval_response is a valid JSON string without extra backticks or characters
    eval_response = eval_response.strip()  # Strip any leading/trailing whitespaces
    if eval_response.startswith("```json") and eval_response.endswith("```"):
        eval_response = eval_response[7:-3].strip()  # Remove the ```json and closing ```

    try:
        # Parse the cleaned JSON response
        data = json.loads(eval_response)
        # score = data['score']
        expression_score = float(data.get("Expression", 0))
        aesthetic_score = float(data.get("Aesthetic", 0))
        readability_score = float(data.get("Readability", 0))
        color_score = float(data.get("Color", 0))
        layout_score = float(data.get("Layout", 0))
        suggestion = data['suggestion']
        score = expression_score + aesthetic_score + readability_score + color_score + layout_score
        # score = int(score)
        score_text = f"""Expression Score: {expression_score}
Aesthetic Score: {aesthetic_score}
Readability Score: {readability_score}
Color Score: {color_score}
Layout Score: {layout_score}
Total Score: {score}
"""
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {eval_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        if score < 8:
            if os.path.exists(chart_folder):
                shutil.rmtree(chart_folder)
            print(f"图表评分为 {score},删除路径{chart_folder}")
            print(f"图表评分为 {score}，需要优化。正在优化 temp_code.R...")
            # 优化图表代码
            code_path = os.path.join(chart_folder, 'temp_code.R')
            optimized_code=optimize_code(client,chart_folder,suggestion)
            _sanitize_output_r(optimized_code,chart_folder)
            #print(optimized_code)
        else:
            with open("datasets_scores.txt", "a") as f:
                f.write(f"DIR: {chart_folder}\n")
                f.write(f"{score_text}\n")
                f.write("=" * 30 + "\n")
            print(f"图表评分为 {score}，无需优化。")
    except Exception as e:
        print(f"处理评估结果时出错: {e}")

    return [expression_score, aesthetic_score, readability_score, color_score, layout_score, score]

def eval_chart():
    # 获取图表的评估结果
    chart_image_path = os.path.join(chart_folder, 'chart.png')
    eval_response = eval_chart(client, chart_image_path)

    # Ensure the eval_response is a valid JSON string without extra backticks or characters
    eval_response = eval_response.strip()  # Strip any leading/trailing whitespaces
    if eval_response.startswith("```json") and eval_response.endswith("```"):
        eval_response = eval_response[7:-3].strip()  # Remove the ```json and closing ```

    try:
        # Parse the cleaned JSON response
        data = json.loads(eval_response)
        # score = data['score']
        expression_score = float(data.get("Expression", 0))
        aesthetic_score = float(data.get("Aesthetic", 0))
        readability_score = float(data.get("Readability", 0))
        color_score = float(data.get("Color", 0))
        layout_score = float(data.get("Layout", 0))
        suggestion = data['suggestion']
        score = expression_score + aesthetic_score + readability_score + color_score + layout_score
        # score = int(score)
        score_text = f"""Expression Score: {expression_score}
Aesthetic Score: {aesthetic_score}
Readability Score: {readability_score}
Color Score: {color_score}
Layout Score: {layout_score}
Total Score: {score}
"""
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {eval_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        if score < 8:
            if os.path.exists(chart_folder):
                shutil.rmtree(chart_folder)
            print(f"图表评分为 {score},删除路径{chart_folder}")
            print(f"图表评分为 {score}，需要优化。正在优化 temp_code.R...")
            # 优化图表代码
            code_path = os.path.join(chart_folder, 'temp_code.R')
            optimized_code=optimize_code(client,chart_folder,suggestion)
            _sanitize_output_r(optimized_code,chart_folder)
            #print(optimized_code)
        else:
            with open("datasets_scores.txt", "a") as f:
                f.write(f"DIR: {chart_folder}\n")
                f.write(f"{score_text}\n")
                f.write("=" * 30 + "\n")
            print(f"图表评分为 {score}，无需优化。")
    except Exception as e:
        print(f"处理评估结果时出错: {e}")

    return [expression_score, aesthetic_score, readability_score, color_score, layout_score, score]

def main():
    """主程序"""

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
    model_names = ["deepseek","gpt-4o-1","claude","doubao","qwq32b","ernie"]
    model_dirs = ["Qwen2.5-7B-Instruct", "Qwen2.5-1.5B-Instruct","Qwen2.5-0.5B-Instruct"]
    # model_dirs = []
    # 数量
    num_iterations = 6000  # 可以修改为所需的生成次数

    total_scores = [] 
    num_folders = 0
    results_file = "results.txt"
    for i in range(1,2):
        c = clients[i]
        model_name = model_names[i]
        # 使用 ThreadPoolExecutor 进行并行化加速
        with ThreadPoolExecutor(max_workers=256) as executor:
            futures = []
            for i in range(1, num_iterations + 1):
                future = executor.submit(generate_and_process, c, i, model_name)
                futures.append(future)

            # 等待所有任务完成
            for future in as_completed(futures):
                try:
                    future.result()  # 获取返回值，如果有异常会抛出
                except Exception as e:
                    print(f"任务失败: {e}")
    for i in range(1,2):
        c = clients[i]
        model_name = model_names[i]    
        base_dir = '/data/yangyuming/projects/chart_generation/chartWithTemplate'
        model_dir = base_dir + "+" + model_name
    # 使用 ThreadPoolExecutor 进行并行化加速
        futures = []
        with ThreadPoolExecutor(max_workers=256) as executor:
            
            # 遍历主文件夹下面的所有子文件夹
            
            for folder in os.listdir(model_dir):
                folder_path = os.path.join(model_dir, folder)
                if os.path.isdir(folder_path):
                    # 提交任务
                    futures.append(executor.submit(process_chart, client, folder_path))
        for future in as_completed(futures):
            try:
                scores = future.result()
                if not scores:
                    continue
                if not total_scores:
                    total_scores = scores  # 初始化
                else:
                    total_scores = [x + y for x, y in zip(total_scores, scores)]
                    
            except Exception as e:
                print(f"Error processing chart: {e}")
            

            
            
        num_folders = count_subdirectories(model_dir)
        avg_scores = [round(total / num_folders, 2) for total in total_scores]
        suc = num_folders if num_folders else 0
        # with open(results_file, "a") as f:
        #     f.write(f"Model: {model_name}\n")
        #     f.write(f"Average Scores: {avg_scores}\n")
        #     f.write(f"Success Rate: {suc:.2f}\n")
        #     f.write("=" * 30 + "\n")

        print(f"Score: {avg_scores}, Success Rate: {suc:.2f}")
        print(f"score:{avg_scores}")
        print(f"suc:{num_folders}")


if __name__ == "__main__":
    main()