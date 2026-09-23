"""对单张已生成的图表调用评分接口，用于快速验证评分链路。

用法：
    python eval_test.py [图片路径]

不带参数时取默认输出目录下的 chartWithTemplate/chart_0001/chart.png。
"""
import os
import sys

from eval_chart import eval_chart

# 将项目根目录加入系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.api_config_doubao import APIConfig_DouBao
from src.utils.api_client import APIClient
from src.utils.output import output_dir


def main():
    image_path = sys.argv[1] if len(sys.argv) > 1 else output_dir(
        "chartWithTemplate", "chart_0001", "chart.png")
    if not os.path.exists(image_path):
        raise SystemExit(f"图片不存在：{image_path}\n可传入路径参数，例如："
                         f"python eval_test.py <图片路径>")

    client = APIClient(APIConfig_DouBao())
    print(eval_chart(client, image_path))


if __name__ == "__main__":
    main()
