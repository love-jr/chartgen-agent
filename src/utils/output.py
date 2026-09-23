"""输出目录解析。

原实现把输出路径硬编码为某台机器上的绝对路径
（``/data/yangyuming/projects/chart_generation/...``），换机器即无法运行。
现改为：

1. 读环境变量 ``CHARTGEN_OUTPUT_DIR``（推荐）；
2. 未设置时用项目根目录下的 ``output/``。

各生成脚本通过 ``output_dir()`` 取根目录，再自行拼子目录名。
"""
import os

# 项目根目录：src/utils/output.py -> 上溯三层
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

ENV_VAR = "CHARTGEN_OUTPUT_DIR"


def output_dir(*parts):
    """返回输出根目录（可附带子路径），并确保目录存在。

    >>> output_dir()                       # .../chartgen-agent/output
    >>> output_dir("chartWithTemplate+gpt-4o", "chart_0001")
    """
    root = os.environ.get(ENV_VAR) or DEFAULT_OUTPUT_DIR
    path = os.path.join(root, *parts) if parts else root
    os.makedirs(path, exist_ok=True)
    return path
