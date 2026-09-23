"""阶段 ③ 的「出图」部分：执行生成的 R 代码（ggplot2）。

含一个轻量依赖修复：模型常忘记 ``library()``，此处按函数名补上。
"""
import os
import re
import shutil
import subprocess

#: R 函数/操作符 -> 所属包
_LIBRARY_HINTS = {
    "mutate": "dplyr",
    "%>%": "dplyr",
    "theme_ipsum_rc": "hrbrthemes",
    "finalise_plot": "bbplot",
    "bbc_style": "bbplot",
    "scale_fill_nejm": "ggsci",
    "theme_wsj": "ggthemes",
    "geom_text_repel": "ggrepel",
}

_CODE_BLOCK = re.compile(r"```[rR]\s*(.*?)```", re.M | re.S)


def extract_r_code(text: str) -> str:
    """从模型回复中取出 R 代码；没有代码块时退回原文。"""
    blocks = _CODE_BLOCK.findall(text)
    return blocks[0] if blocks else text


def auto_fix_libraries(code: str) -> str:
    """补上代码用到但未 ``library()`` 的包。"""
    loaded = set(re.findall(r"library\((.*?)\)", code))
    needed = {lib for func, lib in _LIBRARY_HINTS.items()
              if func in code and lib not in loaded}
    if not needed:
        return code
    header = "\n".join(f"library({lib})" for lib in sorted(needed))
    return header + "\n\n" + code


def run_r_code(text: str, folder: str, script_name: str = "temp_code.R") -> None:
    """把 R 代码写入 ``folder`` 并执行；失败时删除该样本目录并抛出异常。"""
    code = auto_fix_libraries(extract_r_code(text))
    os.makedirs(folder, exist_ok=True)
    script = os.path.join(folder, script_name)
    with open(script, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(["Rscript", script], check=True)
    except Exception:
        shutil.rmtree(folder, ignore_errors=True)
        print(f"执行 R 代码失败，已删除样本目录 {folder}")
        raise
