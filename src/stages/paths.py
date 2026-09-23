"""输出路径约定。

每个样本落在 ``<输出根>/<前缀><模型名>/chart_XXXX/`` 下。两条路线用不同
前缀区分，与论文中「带模板 / 不带模板」两组实验的目录布局一致；多模型
对比则靠模型名区分。
"""
from src.utils.output import output_dir, output_path

#: 带模板路线（``src/code_withTemplate/``）
WITH_TEMPLATE_PREFIX = "chartWithTemplate+"
#: 不带模板路线（``src/code_withoutTemplate/``）
WITHOUT_TEMPLATE_PREFIX = "chart+"


def sample_dir(prefix: str, model_name: str, index: int) -> str:
    """样本目录（会创建），如 ``output/chartWithTemplate+gpt-4o/chart_0001``。"""
    return output_dir(f"{prefix}{model_name}", f"chart_{index:04d}")


def sample_png(prefix: str, model_name: str, index: int) -> str:
    """样本图的完整路径（不创建目录，由 Rscript 写入）。"""
    return output_path(f"{prefix}{model_name}", f"chart_{index:04d}", "chart.png")
