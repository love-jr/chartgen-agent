"""数据集批量生成：带模板路线 + 低分样本优化重出。

与实验一的区别：本脚本产出「优化后」的图表数据集，即对初评低于阈值的
样本先删除、再改写代码重出图，用于论文中的优化前后对照。

用法：
    cd src/eval && python generate_datasets.py [模型名]
"""
import os
import shutil
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.code_withTemplate.main import generate_and_process
from src.eval.common import make_client, sample_indices
from src.stages.evaluate import eval_chart, parse_scores
from src.stages.execute import run_r_code
from src.stages.optimize import optimize_code
from src.stages.paths import WITH_TEMPLATE_PREFIX, sample_dir, sample_png
from src.stages.pipeline import run_batch

DEFAULT_MODEL = "deepseek"      # 命令行未指定模型时的默认值
NUM_ITERATIONS = 6000
THRESHOLD = 8.0
GENERATE_WORKERS = 8
EVAL_WORKERS = 8
SCORES_FILE = "datasets_scores.txt"


def refine_or_keep(eval_client, optimize_client, model_name, index):
    """评分；低于阈值则优化并重出图，否则记入合格清单。

    返回 ``(index, 分数或 None, 错误信息)``。
    """
    png = sample_png(WITH_TEMPLATE_PREFIX, model_name, index)
    if not os.path.exists(png):
        return index, None, "图片不存在"

    scores, suggestion = parse_scores(eval_chart(eval_client, png))
    if scores is None:
        return index, None, "评分回复无法解析"

    if scores["Total"] >= THRESHOLD:
        return index, scores, ""

    # 低于阈值：先取代码再删目录，避免读到已删除的 temp_code.R
    folder = sample_dir(WITH_TEMPLATE_PREFIX, model_name, index)
    code = optimize_code(optimize_client, folder, suggestion, png)
    if not code:
        return index, scores, "获取优化代码失败"

    shutil.rmtree(folder, ignore_errors=True)
    try:
        run_r_code(code, folder)
    except Exception as e:
        return index, scores, f"优化后出图失败: {e}"
    return index, scores, ""


def main():
    model_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    eval_client = make_client("doubao")
    gen_client = make_client(model_name)
    optimize_client = make_client(model_name)

    print(f"=== 生成 {model_name} ===")
    run_batch(range(1, NUM_ITERATIONS + 1),
              lambda i: generate_and_process(gen_client, i, model_name),
              max_workers=GENERATE_WORKERS)

    print("=== 评分并按阈值优化 ===")
    kept = 0
    with ThreadPoolExecutor(max_workers=EVAL_WORKERS) as pool:
        futures = [pool.submit(refine_or_keep, eval_client, optimize_client,
                               model_name, i)
                   for i in sample_indices(WITH_TEMPLATE_PREFIX, model_name)]
        for future in as_completed(futures):
            index, scores, err = future.result()
            if err:
                print(f"[{index:04d}] {err}")
                continue
            if scores is not None and scores["Total"] >= THRESHOLD:
                kept += 1
                with open(SCORES_FILE, "a", encoding="utf-8") as f:
                    f.write(f"DIR: chart_{index:04d}\n")
                    for key, value in scores.items():
                        f.write(f"{key}: {value}\n")
                    f.write("=" * 30 + "\n")

    print(f"达标样本数：{kept}")


if __name__ == "__main__":
    main()
