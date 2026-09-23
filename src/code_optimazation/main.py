"""阶段 ③ 批量评分：对某个输出目录下所有样本逐一打分并汇总。

用法：
    python main.py [样本目录父目录]

默认父目录为 output/chartWithTemplate+gpt-4o。评分维度与提示词见
``src/stages/evaluate.py``；本脚本只做遍历与汇总，不修改任何文件。
"""
import os
import sys

from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.stages.evaluate import DIMENSIONS, eval_chart, parse_scores
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_png
from src.utils.api_client import APIClient
from src.utils.api_config import APIConfig
from src.utils.output import output_dir

SAMPLE_DIR = f"{WITH_TEMPLATE_PREFIX}gpt-4o"
MAX_WORKERS = 64


def process_chart(client, index):
    """对第 ``index`` 个样本评分，返回 ``(index, 错误信息, 分数)``。"""
    image = sample_png(WITH_TEMPLATE_PREFIX, "gpt-4o", index)
    if not os.path.exists(image):
        return index, "图片不存在", None
    scores, _ = parse_scores(eval_chart(client, image))
    if scores is None:
        return index, "评分回复无法解析", None
    return index, "", scores


def main():
    base_dir = sys.argv[1] if len(sys.argv) > 1 else output_dir(SAMPLE_DIR)
    samples = sorted(d for d in os.listdir(base_dir)
                     if os.path.isdir(os.path.join(base_dir, d)))
    if not samples:
        raise SystemExit(f"目录下没有样本：{base_dir}")

    client = APIClient(APIConfig())
    totals = {dim: 0.0 for dim in DIMENSIONS}
    totals["Total"] = 0.0
    counted = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(process_chart, client, i)
                   for i in range(1, len(samples) + 1)]
        for future in as_completed(futures):
            index, err, scores = future.result()
            if err:
                print(f"[{index:04d}] {err}")
                continue
            counted += 1
            for key in totals:
                totals[key] += scores[key]

    if not counted:
        raise SystemExit("没有可用样本，无法汇总")
    print(f"样本数 {counted}，平均分：")
    for key, value in totals.items():
        print(f"  {key}: {value / counted:.2f}")


if __name__ == "__main__":
    main()
