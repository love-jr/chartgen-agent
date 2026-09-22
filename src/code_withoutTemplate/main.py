from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import random
import json
import sys
from data_generator import generate_data
from data_saver import save_generated_data
from code_generator import generate_code_for_chart,generate_code_for_chart_optimization
from code_executor import _sanitize_output_r

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from config.list import chart_themes,chart_types,color_matchings,topics
from src.utils.api_config import APIConfig
from src.utils.api_config1 import APIConfig1
from src.utils.api_client import APIClient




def generate_and_process(client,client1,i):
    topic=random.choice(topics)
    chart_type = random.choice(chart_types)
    chart_theme = random.choice(chart_themes)
    color_matching = random.choice(color_matchings)

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
    generated_code = generate_code_for_chart(client, topic,  generated_data, chart_type,title,subtitle)

    # #优化代码
    optimazed_code=generate_code_for_chart_optimization(client1,chart_theme,color_matching,generated_code,source,i)
   
    #print(optimazed_code)
    #执行代码
    _sanitize_output_r(optimazed_code, i)

def main():
    """主程序"""

    config = APIConfig()
    config1 = APIConfig1()
    client = APIClient(config)
    client1 = APIClient(config1)

    # 数量
    num_iterations = 50  # 可以修改为所需的生成次数

    # 使用 ThreadPoolExecutor 进行并行化加速
    with ThreadPoolExecutor(max_workers=256) as executor:
        futures = []
        for i in range(1, num_iterations + 1):
            future = executor.submit(generate_and_process, client, client1, i)
            futures.append(future)

        # 等待所有任务完成
        for future in as_completed(futures):
            try:
                future.result()  # 获取返回值，如果有异常会抛出
            except Exception as e:
                print(f"任务失败: {e}")


if __name__ == "__main__":
    main()