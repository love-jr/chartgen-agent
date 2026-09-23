"""实验二：对已生成结果批量评估（不重新生成）。

用于补评：模型目录里已有样本，只想重跑评分链路。
结果追加到 ``results.txt``（与实验一同一文件，便于对比）。

用法：
    cd src/eval && python experiment2.py
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.eval.common import evaluate_model, make_client, report
from src.stages.paths import WITH_TEMPLATE_PREFIX

MODELS = ["deepseek", "gpt-4o", "claude"]
RESULTS_FILE = "results.txt"


def main():
    for model_name in MODELS:
        client = make_client(model_name)
        avg, success = evaluate_model(client, WITH_TEMPLATE_PREFIX, model_name)
        if avg is None:
            print(f"{model_name}: 无可用样本，跳过")
            continue
        report(model_name, avg, success, success, RESULTS_FILE)


if __name__ == "__main__":
    main()
