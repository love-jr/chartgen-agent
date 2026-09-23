"""实验一：带模板路线的多模型对比。

对每个模型各生成 ``NUM_ITERATIONS`` 个样本（带模板），再用视觉模型统一评分，
结果追加到 ``results.txt``。对应论文中「给定参考模板」的实验组。

用法：
    cd src/eval && python experiment1.py
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.code_withTemplate.main import generate_and_process
from src.eval.common import evaluate_model, make_client, report
from src.stages.paths import WITH_TEMPLATE_PREFIX
from src.stages.pipeline import run_batch

#: 参与对比的模型（顺序即执行顺序）
MODELS = [
    "deepseek", "gpt-4o", "doubao", "d_llama70b", "qwq32b", "ernie",
    "d_qwq32b", "d_qwq7b", "moonshot", "glm3", "mistral7b",
]

NUM_ITERATIONS = 50         # 每个模型生成多少条
GENERATE_WORKERS = 8        # 生成并发（过高易触发服务商限流）
RESULTS_FILE = "results.txt"


def main():
    for model_name in MODELS:
        print(f"=== 生成 {model_name} ===")
        client = make_client(model_name)
        run_batch(range(1, NUM_ITERATIONS + 1),
                  lambda i, c=client, m=model_name: generate_and_process(c, i, m),
                  max_workers=GENERATE_WORKERS)

        print(f"=== 评估 {model_name} ===")
        avg, success = evaluate_model(client, WITH_TEMPLATE_PREFIX, model_name)
        report(model_name, avg, success, NUM_ITERATIONS, RESULTS_FILE)


if __name__ == "__main__":
    main()
