"""实验四：优化前后得分对比。

取出带模板路线中初评低于阈值（默认 7 分）的样本，用阶段 ③ 的优化提示词
改写代码并重新出图，再评一次，比较优化前后的平均分。结果追加到
``result4.txt``。

用法：
    cd src/eval && python experiment4.py [样本父目录]
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.eval.common import make_client, sample_indices
from src.stages.evaluate import DIMENSIONS, eval_chart, parse_scores
from src.stages.execute import run_r_code
from src.stages.optimize import optimize_code
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_dir, sample_png
from src.utils.output import output_dir

MODEL_NAME = "deepseek"
THRESHOLD = 7.0             # 低于此分才优化
WORKERS = 8
RESULTS_FILE = "result4.txt"

_KEYS = list(DIMENSIONS) + ["Total"]


def process_one(eval_client, optimize_client, index):
    """评一次 → 低于阈值则优化并重评，返回 ``(index, 优化前, 优化后)``。"""
    png = sample_png(WITH_TEMPLATE_PREFIX, MODEL_NAME, index)
    if not os.path.exists(png):
        return index, None, None

    before, suggestion = parse_scores(eval_chart(eval_client, png))
    if before is None or before["Total"] >= THRESHOLD:
        return index, before, None

    folder = sample_dir(WITH_TEMPLATE_PREFIX, MODEL_NAME, index)
    code = optimize_code(optimize_client, folder, suggestion, png)
    if not code:
        return index, before, None
    try:
        run_r_code(code, folder)
    except Exception as e:
        print(f"[{index:04d}] 优化后出图失败: {e}")
        return index, before, None

    after, _ = parse_scores(eval_chart(eval_client, png))
    return index, before, after


def _average(samples):
    if not samples:
        return None
    return {k: round(sum(s[k] for s in samples) / len(samples), 2) for k in _KEYS}


def main():
    eval_client = make_client("doubao")     # 评分统一用 DouBao 视觉模型
    optimize_client = make_client(MODEL_NAME)

    indices = sample_indices(WITH_TEMPLATE_PREFIX, MODEL_NAME)
    if not indices:
        raise SystemExit(f"没有找到样本：{output_dir(f'{WITH_TEMPLATE_PREFIX}{MODEL_NAME}')}")

    before_all, after_all = [], []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(process_one, eval_client, optimize_client, i)
                   for i in indices]
        for future in as_completed(futures):
            index, before, after = future.result()
            if before is not None and before["Total"] < THRESHOLD:
                before_all.append(before)
                if after is not None:
                    after_all.append(after)

    avg_before = _average(before_all)
    avg_after = _average(after_all)

    print(f"\n【优化前平均得分】(n={len(before_all)})")
    for k in _KEYS:
        print(f"{k}: {avg_before[k]:.2f}" if avg_before else f"{k}: 无数据")
    print(f"\n【优化后平均得分】(n={len(after_all)})")
    for k in _KEYS:
        print(f"{k}: {avg_after[k]:.2f}" if avg_after else f"{k}: 无数据")

    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(f"Model: {MODEL_NAME}\n")
        f.write(f"Threshold: {THRESHOLD}\n")
        f.write(f"【优化前平均得分】(n={len(before_all)})\n")
        for k in _KEYS:
            f.write(f"{k}: {avg_before[k]:.2f}\n" if avg_before else f"{k}: 无数据\n")
        f.write(f"\n【优化后平均得分】(n={len(after_all)})\n")
        for k in _KEYS:
            f.write(f"{k}: {avg_after[k]:.2f}\n" if avg_after else f"{k}: 无数据\n")
        f.write("=" * 30 + "\n")


if __name__ == "__main__":
    main()
