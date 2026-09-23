"""实验三：不带模板路线的多模型对比。

与实验一的区别只在阶段 ②：不给参考模板，改用主题配色提示词优化代码。
结果追加到 ``resultsWithoutT.txt``。

用法：
    cd src/eval && python experiment3.py
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.code_withoutTemplate.main import generate_and_process
from src.eval.common import evaluate_model, make_client, report
from src.stages.paths import WITHOUT_TEMPLATE_PREFIX
from src.stages.pipeline import run_batch

MODELS = [
    "deepseek", "gpt-4o", "doubao", "d_llama70b", "d_qwq32b", "qwq32b",
    "d_qwq7b", "ernie",
]

NUM_ITERATIONS = 50
GENERATE_WORKERS = 8
RESULTS_FILE = "resultsWithoutT.txt"


def main():
    for model_name in MODELS:
        print(f"=== 生成 {model_name} ===")
        client = make_client(model_name)
        optimizer = make_client("deepseek")
        run_batch(
            range(1, NUM_ITERATIONS + 1),
            lambda i, c=client, o=optimizer, m=model_name: generate_and_process(c, o, i, m),
            max_workers=GENERATE_WORKERS)

        print(f"=== 评估 {model_name} ===")
        avg, success = evaluate_model(client, WITHOUT_TEMPLATE_PREFIX, model_name)
        report(model_name, avg, success, NUM_ITERATIONS, RESULTS_FILE)


if __name__ == "__main__":
    main()
