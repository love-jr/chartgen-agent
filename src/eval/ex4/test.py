"""早期探索：优化前后得分对比（论文之外的试验代码）。

与 ``experiment4.py`` 的区别：本脚本不重新出图，仅对同一批样本连评两次，
用于观察评分接口自身的稳定性（同一张图的两次评分差即噪声）。结果写入
``result4.txt`` 与 ``total_scores.json`` / ``optimized_scores.json``。

用法：
    cd src/eval/ex4 && python test.py
"""
import json
import os
import sys

from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import numpy as np

from src.stages.evaluate import DIMENSIONS, eval_chart, parse_scores
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_png
from src.utils.api_client import APIClient
from src.utils.api_config import APIConfig_DouBao
from src.utils.output import output_path

MODELS = ["deepseek", "gpt-4o", "claude", "doubao", "qwq32b", "ernie",
          "d_llama70b"]
THRESHOLD = 8.0
WORKERS = 32

_KEYS = list(DIMENSIONS) + ["Total"]


def score_twice(client, prefix, model_name, index):
    """对同一张图连评两次，返回 ``(第一次, 第二次)``。"""
    png = sample_png(prefix, model_name, index)
    if not os.path.exists(png):
        return None, None
    first, _ = parse_scores(eval_chart(client, png))
    second, _ = parse_scores(eval_chart(client, png))
    return first, second


def _average(samples):
    if not samples:
        return {k: None for k in _KEYS}
    return {k: round(float(np.mean([s[k] for s in samples])), 2) for k in _KEYS}


def _write_result(model_name, before, after, out_dir):
    with open(os.path.join(out_dir, "result4.txt"), "a", encoding="utf-8") as f:
        f.write(f"Model: {model_name}\n")
        f.write(f"【第一次评分平均】(n={len(before)})\n")
        for k in _KEYS:
            f.write(f"{k}: {before[k]:.2f}\n" if before[k] is not None else f"{k}: 无数据\n")
        f.write(f"\n【第二次评分平均】(n={len(after)})\n")
        for k in _KEYS:
            f.write(f"{k}: {after[k]:.2f}\n" if after[k] is not None else f"{k}: 无数据\n")
        f.write("=" * 30 + "\n")


def main():
    client = APIClient(APIConfig_DouBao())
    out_dir = os.path.dirname(os.path.abspath(__file__))

    for model_name in MODELS:
        base = output_path(f"{WITH_TEMPLATE_PREFIX}{model_name}")
        if not os.path.isdir(base):
            print(f"{model_name}: 无样本目录，跳过")
            continue
        indices = sorted(int(d.rsplit("_", 1)[-1]) for d in os.listdir(base)
                         if d.startswith("chart_") and os.path.isdir(os.path.join(base, d)))
        if not indices:
            print(f"{model_name}: 无样本，跳过")
            continue

        before, after = [], []
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(score_twice, client, WITH_TEMPLATE_PREFIX,
                                   model_name, i) for i in indices]
            for future in as_completed(futures):
                first, second = future.result()
                if first is not None and first["Total"] < THRESHOLD:
                    before.append(first)
                    if second is not None:
                        after.append(second)

        avg_before = _average(before)
        avg_after = _average(after)

        print(f"\n{model_name} ——【第一次评分平均】(n={len(before)})")
        for k in _KEYS:
            print(f"  {k}: {avg_before[k]:.2f}" if avg_before[k] is not None else f"  {k}: 无数据")
        print(f"{model_name} ——【第二次评分平均】(n={len(after)})")
        for k in _KEYS:
            print(f"  {k}: {avg_after[k]:.2f}" if avg_after[k] is not None else f"  {k}: 无数据")

        _write_result(model_name, avg_before, avg_after, out_dir)

    with open(os.path.join(out_dir, "scores.json"), "w", encoding="utf-8") as f:
        json.dump({"note": "早期探索：同一张图两次评分的对比结果"}, f,
                  ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
