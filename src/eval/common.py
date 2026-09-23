"""实验脚本的公共部分：模型清单、结果落盘、成图评估循环。

原 ``experiment1/2/3/4.py`` 各自把「模型清单 + 线程池 + 解析评分 + 累加平均」
抄了一遍，且抄出多种不一致（有的 ``range(0)`` 空转、有的把一个目录当 index
传给评分函数、有的 ``rmtree`` 后立刻回读已删目录）。此处统一。

模型清单与论文中参与对比的模型一一对应。
"""
import os

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.stages.evaluate import DIMENSIONS, eval_chart, parse_scores
from src.stages.paths import sample_png
from src.utils.api_config import (
    APIConfig, APIConfig1, APIConfig_DL70B, APIConfig_DQ7B, APIConfig_DQ32B,
    APIConfig_Deepseek, APIConfig_DouBao, APIConfig_ERNIE, APIConfig_GLM3,
    APIConfig_GPT4, APIConfig_GPTO1, APIConfig_MISTRAL7B, APIConfig_MOON,
    APIConfig_QWQ32B,
)

CONFIG_CLASSES = {
    "gpt-4o": APIConfig,
    "gpt-4": APIConfig_GPT4,
    "o1": APIConfig_GPTO1,
    "claude": APIConfig1,
    "deepseek": APIConfig_Deepseek,
    "doubao": APIConfig_DouBao,
    "ernie": APIConfig_ERNIE,
    "qwq32b": APIConfig_QWQ32B,
    "d_llama70b": APIConfig_DL70B,
    "d_qwq32b": APIConfig_DQ32B,
    "d_qwq7b": APIConfig_DQ7B,
    "glm3": APIConfig_GLM3,
    "mistral7b": APIConfig_MISTRAL7B,
    "moonshot": APIConfig_MOON,
}


def make_client(model_name):
    """按模型名构造 API 客户端。"""
    from src.utils.api_client import APIClient
    return APIClient(CONFIG_CLASSES[model_name]())


def sample_indices(prefix, model_name):
    """列出某模型目录下已有的样本序号。"""
    from src.utils.output import output_path
    base = output_path(f"{prefix}{model_name}")
    if not os.path.isdir(base):
        return []
    return sorted(int(d.rsplit("_", 1)[-1]) for d in os.listdir(base)
                  if d.startswith("chart_") and os.path.isdir(os.path.join(base, d)))


def score_one(client, prefix, model_name, index):
    """给单个样本评分，返回 ``(index, 错误信息, 分数或 None)``。"""
    png = sample_png(prefix, model_name, index)
    if not os.path.exists(png):
        return index, "图片不存在", None
    scores, _ = parse_scores(eval_chart(client, png))
    if scores is None:
        return index, "评分回复无法解析", None
    return index, "", scores


def evaluate_model(client, prefix, model_name, worker=32):
    """评估某模型全部样本，返回 ``(平均分字典, 成功数)``。

    平均分字典含五个维度与 ``Total``；无可用样本时返回 ``(None, 0)``。
    """
    indices = sample_indices(prefix, model_name)
    if not indices:
        return None, 0

    keys = list(DIMENSIONS) + ["Total"]
    totals = {k: 0.0 for k in keys}
    counted = 0

    with ThreadPoolExecutor(max_workers=worker) as pool:
        futures = [pool.submit(score_one, client, prefix, model_name, i)
                   for i in indices]
        for future in as_completed(futures):
            index, err, scores = future.result()
            if err:
                print(f"[{model_name} {index:04d}] {err}")
                continue
            counted += 1
            for k in keys:
                totals[k] += scores[k]

    if not counted:
        return None, 0
    return {k: round(v / counted, 2) for k, v in totals.items()}, counted


def write_result(results_file, model_name, avg_scores, success_count, total):
    """把一次评估结果追加到 txt，格式与历史 ``results*.txt`` 保持一致。"""
    with open(results_file, "a", encoding="utf-8") as f:
        f.write(f"Model: {model_name}\n")
        if avg_scores is None:
            f.write("Average Scores: 无数据\n")
        else:
            ordered = [avg_scores[k] for k in list(DIMENSIONS) + ["Total"]]
            f.write(f"Average Scores: {ordered}\n")
        f.write(f"Success Rate: {success_count}\n")
        f.write(f"Total Samples: {total}\n")
        f.write("=" * 30 + "\n")


def report(model_name, avg_scores, success_count, total, results_file):
    """打印并落盘一次评估结果。"""
    write_result(results_file, model_name, avg_scores, success_count, total)
    print(f"Model: {model_name}")
    print(f"Average Scores: {avg_scores}")
    print(f"Success Rate: {success_count}/{total}")
