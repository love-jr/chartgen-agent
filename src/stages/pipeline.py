"""生成流程的公共部分：回复解析与并行驱动。

两条路线的 ``main.py``、以及各实验脚本原先各自复制一遍「解析模型回复里
的 JSON」「线程池跑批」的样板。此处统一，流程本身仍留在各自的 main。
"""
import json
import re

from concurrent.futures import ThreadPoolExecutor, as_completed


def parse_response(response_text):
    """从数据生成回复中取出 JSON 对象。

    兼容 ``<output_begining>…<output_ending>``、```json 代码块、裸 JSON。
    返回 ``(payload, 错误信息)``；成功时错误信息为空串。
    """
    if "<output_begining>" in response_text and "<output_ending>" in response_text:
        text = response_text.split("<output_begining>")[1].split("<output_ending>")[0]
    else:
        block = re.search(r"```json\s*([\s\S]+?)```", response_text)
        if block:
            text = block.group(1)
        else:
            bare = re.search(r"\{[\s\S]*\}", response_text)
            if not bare:
                return None, "回复中未找到 JSON"
            text = bare.group(0)
    try:
        return json.loads(text.strip()), ""
    except json.JSONDecodeError as e:
        return None, f"JSON 解析失败: {e}"


def run_batch(tasks, worker, max_workers=64):
    """并行执行 ``tasks``，``worker(task)`` 返回 ``(index, 错误信息)``。

    单个任务的异常被捕获并打印，不影响其余任务。
    """
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(worker, task) for task in tasks]
        for future in as_completed(futures):
            try:
                index, err = future.result()
            except Exception as e:
                print(f"任务异常: {type(e).__name__}: {e}")
                continue
            if err:
                print(f"[{index:04d}] {err}")
