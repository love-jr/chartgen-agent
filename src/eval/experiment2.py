import os
from pathlib import Path
import json
import sys

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
from src.eval.count import count_subdirectories

def process_chart(client, chart_folder):
    """处理每个图表文件夹，进行评估和优化"""
    # 获取图表的评估结果
    root_dir = Path(chart_folder)  # 修改为你的目标根目录
    chart_image_path = [str(path) for path in root_dir.rglob("*.png")]
    # chart_image_path = os.path.join(chart_folder, 'chart.png')
    eval_response = eval_chart(client, chart_image_path)

    # Ensure the eval_response is a valid JSON string without extra backticks or characters
    eval_response = eval_response.strip()  # Strip any leading/trailing whitespaces
    if eval_response.startswith("```json") and eval_response.endswith("```"):
        eval_response = eval_response[7:-3].strip()  # Remove the ```json and closing ```

    try:
        # Parse the cleaned JSON response
        data = json.loads(eval_response)
        # score = data['score']
        expression_score = float(data.get("Expression", 1.2))
        aesthetic_score = float(data.get("Aesthetic", 1.2))
        readability_score = float(data.get("Readability", 1.2))
        color_score = float(data.get("Color", 1.2))
        layout_score = float(data.get("Layout", 1.2))
        # suggestion = data['suggestion']
        score = expression_score + aesthetic_score + readability_score + color_score + layout_score
        # score = int(score)
        
    except json.JSONDecodeError:
        print(f"Error decoding JSON: {eval_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # try:
    #     if score < 8:
    #         print(f"图表评分为 {score}，需要优化。正在优化 temp_code.R...")
    #         # 优化图表代码
    #         #code_path = os.path.join(chart_folder, 'temp_code.R')
    #         optimized_code=optimize_code(client,chart_folder,suggestion)
    #         _sanitize_output_r(optimized_code,chart_folder)
    #         #print(optimized_code)
    #     else:
    #         print(f"图表评分为 {score}，无需优化。")
    # except Exception as e:
    #     print(f"处理评估结果时出错: {e}")

    return [expression_score, aesthetic_score, readability_score, color_score, layout_score, score]

def main():
    """主程序"""

    config = APIConfig()
    config1 = APIConfig1()
    client = APIClient(config)
    client1 = APIClient(config1)
    config_deepseek = APIConfig_Deepseek()
    client_deepseek = APIClient(config_deepseek)

    clients = [client_deepseek,client,client1]
    model_names = ["deepseek","gpt-4o","claude"]
    