import os
import json
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.output import output_dir


def save_generated_data(generated_data: str, index: int, model_name: str):
    """将生成的数据保存为 JSON 文件

    输出位置由 CHARTGEN_OUTPUT_DIR 决定，默认落在项目根目录的 output/ 下。
    """
    chart_subfolder_path = output_dir(f"chart+{model_name}", f"chart_{index:04d}")

    # 保存生成的图表信息为 JSON 文件
    chart_info_path = os.path.join(chart_subfolder_path, 'chart_info.json')
    try:
        with open(chart_info_path, 'w', encoding='utf-8') as file:
            json.dump(generated_data, file, ensure_ascii=False, indent=4)
        print(f"数据已保存为 {chart_info_path}")
    except Exception as e:
        print(f"保存数据失败: {e}")
