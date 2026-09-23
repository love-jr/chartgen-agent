"""提示词模板读取与填充。

原先 ``code_withTemplate/``、``code_withoutTemplate/``、``code_optimazation/``
各有一份内容完全相同的 ``prompt_loader.py``。现合并到此处。

填充用 ``str.replace`` 而非 ``str.format``：模板里含大量 R/ggplot2 花括号
（如 ``theme(axis.text = ...)``），``format`` 会把它们当成占位符而报错。
"""
import os

# config/prompts/：src/utils/prompt.py -> 上溯三层到项目根
PROMPTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "config", "prompts")


def load_prompt(name_or_path: str) -> str:
    """读取提示词模板。

    参数可以是 ``config/prompts/`` 下的文件名（如 ``"data_generation.txt"``），
    也可以是绝对/相对路径；读取失败返回空串。
    """
    path = name_or_path
    if not os.path.isabs(path) and os.sep not in path and "/" not in path:
        path = os.path.join(PROMPTS_DIR, path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def fill_prompt(text, /, **values) -> str:
    """把 ``text`` 里的 ``{key}`` 替换为给定值，未提供的占位符保持原样。

    第一个参数声明为位置专用（``/``），这样占位符名字无论叫 ``template``
    还是 ``source``，都能安全地作为关键字参数传入。
    """
    for key, value in values.items():
        text = text.replace("{" + key + "}", str(value))
    return text
