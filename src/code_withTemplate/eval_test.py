"""对单张已生成的图表调用评分接口，用于快速验证评分链路。

用法：
    python eval_test.py [图片路径]

不带参数时取输出目录下的 chartWithTemplate+gpt-4o/chart_0001/chart.png。
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.stages.evaluate import eval_chart
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_png
from src.utils.api_client import APIClient
from src.utils.api_config import APIConfig_DouBao


def main():
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = sample_png(WITH_TEMPLATE_PREFIX, "gpt-4o", 1)
    if not os.path.exists(image_path):
        raise SystemExit(f"图片不存在：{image_path}\n"
                         f"可传入路径参数，例如：python eval_test.py <图片路径>")

    client = APIClient(APIConfig_DouBao())
    print(eval_chart(client, image_path))


if __name__ == "__main__":
    main()
