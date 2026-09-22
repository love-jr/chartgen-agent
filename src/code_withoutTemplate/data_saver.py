import os
import json


def save_generated_data(generated_data: str, index: int, model_name: str):
    """将生成的数据保存为 JSON 文件"""
    # 创建 chart 文件夹及子文件夹

    chart_folder_path = '/data/yangyuming/projects/chart_generation/chart' + '+' + model_name
    os.makedirs(chart_folder_path, exist_ok=True)

    # 创建每个主题的文件夹，如 chart_0001、chart_0002 等
    chart_subfolder = f'chart_{index:04d}'  # 格式化为四位数字，例如 chart_0001
    chart_subfolder_path = os.path.join(chart_folder_path, chart_subfolder)
    os.makedirs(chart_subfolder_path, exist_ok=True)

    # 保存生成的图表信息为 JSON 文件
    chart_info_path = os.path.join(chart_subfolder_path, 'chart_info.json')
    try:
        with open(chart_info_path, 'w', encoding='utf-8') as file:
            json.dump(generated_data, file, ensure_ascii=False, indent=4)
        print(f"数据已保存为 {chart_info_path}")
    except Exception as e:
        print(f"保存数据失败: {e}")