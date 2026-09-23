# from concurrent.futures import ThreadPoolExecutor, as_completed
# import os
# import random
# import json
# import sys
# from eval_chart import eval_chart
# # 将项目根目录加入系统路径
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# from src.utils.api_config import APIConfig
from src.utils.output import output_dir
# from src.utils.api_client import APIClient

from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import json
import sys
from eval_chart import eval_chart
# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_config import APIConfig
from src.utils.api_client import APIClient
from src.eval.delete import delete_subdirectories
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
        expression_score = data.get("Expression", 2)
        aesthetic_score = data.get("Aesthetic", 2)
        readability_score = data.get("Readability", 2)
        color_score = data.get("Color", 2)
        layout_score = data.get("Layout", 2)
        suggestion = data['suggestion']
        score = expression_score + aesthetic_score + readability_score + color_score + layout_score
        print(f"图表评分为 {score}")
        # score = int(score)
        
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {eval_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # try:
    #     if score < 7:
    #         if os.path.exists(chart_folder):
    #             shutil.rmtree(chart_folder)
    #         print(f"图表评分为 {score},删除路径{chart_folder}")
    #         # print(f"图表评分为 {score}，需要优化。正在优化 temp_code.R...")
    #         # # 优化图表代码
    #         # #code_path = os.path.join(chart_folder, 'temp_code.R')
    #         # optimized_code=optimize_code(client,chart_folder,suggestion)
    #         # _sanitize_output_r(optimized_code,chart_folder)
    #         #print(optimized_code)
    #     else:
    #         print(f"图表评分为 {score}，无需优化。")
    # except Exception as e:
    #     print(f"处理评估结果时出错: {e}")

    # return [expression_score, aesthetic_score, readability_score, color_score, layout_score, score]

def main():
    """主程序"""
    config = APIConfig()
    client = APIClient(config)

    # 设置目标目录路径 
    base_dir = output_dir("chartWithTemplate+gpt-4o")
    # delete_subdirectories(base_dir)
    # 使用 ThreadPoolExecutor 进行并行化加速
    with ThreadPoolExecutor(max_workers=256) as executor:
        futures = []
        # 遍历主文件夹下面的所有子文件夹
        for folder in os.listdir(base_dir):
            folder_path = os.path.join(base_dir, folder)
            if os.path.isdir(folder_path):
                # 提交任务
                futures.append(executor.submit(process_chart, client, folder_path))

        # 等待所有任务完成
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
