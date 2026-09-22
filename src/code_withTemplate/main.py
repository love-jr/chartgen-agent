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
from config.list import chart_themes,chart_types,color_matchings,topics,Single_broken_line,multiple_broken_lines,Single_broken_line_dotted,multiple_broken_lines_dotted,Single_Pie_Chart,simple_bar_chart,paired_bar_chart,simple_column_chart,paired_column_chart
from src.utils.api_config import APIConfig
from src.utils.api_config1 import APIConfig1
from src.utils.api_client import APIClient
from src.utils.api_config_deepseek import APIConfig_Deepseek


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

def generate_and_process(client,i):
    topic=random.choice(topics)

    # 按照指定的权重随机选择一个图表类型
    chart_type = random.choices(chart_types, weights=weights, k=1)[0]  

    selected_chart_list =select_chart_list(chart_type)
    #print(select_chart_list)
    template=random.choice(selected_chart_list)
    # print(template)

    response_text = generate_data(client, topic, chart_type)
    json_text = response_text.split("<output_begining>")[1].split("<output_ending>")[0].strip()
    
    # 解析 JSON
    try:
        data = json.loads(json_text)
        title=data["Main Title"]
        subtitle=data["Subtitle"]
        generated_data=data["Data"]
        source=(data["Data Source"])
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
    
    #保存生成的数据
    save_generated_data(generated_data, i)
    
    # 生成图表代码 
    generated_code = generate_code_for_chart(client, topic, data,chart_type,template,i)

    #执行代码
    _sanitize_output_r(generated_code, i)

def main():
    """主程序"""

    config = APIConfig()
    config1 = APIConfig1()
    client = APIClient(config)
    client1 = APIClient(config1)
 

    # 数量
    num_iterations = 3500  # 可以修改为所需的生成次数

        # 使用 ThreadPoolExecutor 进行并行化加速
    with ThreadPoolExecutor(max_workers=256) as executor:
        futures = []
        for i in range(1, num_iterations + 1):
            future = executor.submit(generate_and_process, client, i)
            futures.append(future)

            # 等待所有任务完成
        for future in as_completed(futures):
            try:
                future.result()  # 获取返回值，如果有异常会抛出
            except Exception as e:
                print(f"任务失败: {e}")


if __name__ == "__main__":
    main()