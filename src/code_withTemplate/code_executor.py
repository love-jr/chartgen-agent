import re
import os
import shutil
import subprocess

import re
import os
import shutil
import subprocess

def _auto_fix_r_code(code: str) -> str:
    """
    检查 R 代码中是否使用了某些函数，如果使用了却未加载对应库，则自动添加 library()。
    """
    fixes = {
        'mutate': 'dplyr',
        '%>%': 'dplyr',
        'theme_ipsum_rc': 'hrbrthemes',
        'finalise_plot': 'bbplot',
        'bbc_style': 'bbplot',
        'scale_fill_nejm': 'ggsci',
        'theme_wsj': 'ggthemes',
        'geom_text_repel': 'ggrepel',
    }

    existing_libraries = set(re.findall(r'library\((.*?)\)', code))
    required_libraries = {lib for func, lib in fixes.items() if func in code and lib not in existing_libraries}

    if required_libraries:
        header = "\n".join(f"library({lib})" for lib in sorted(required_libraries))
        code = header + "\n\n" + code

    return code

def _sanitize_output_r(text: str, index: int, model_name: str):
    """
    提取并执行 R 代码块（自动修复缺失库后执行）。
    """
    code_blocks = re.findall(r'```[rR]\s*(.*?)```', text, re.M | re.S)

    if not code_blocks:      
        # print("⚠️ 未发现 markdown R 代码块，尝试过滤自然语言")
        lines = text.splitlines()
        r_lines = []
        in_code = False
        for line in lines:
            if line.strip().lower().startswith("```r"):
                in_code = True
                continue
            elif line.strip() == "```":
                in_code = False
                continue
            if in_code:
                r_lines.append(line)
        code_to_execute = "\n".join(r_lines) if r_lines else text  # fallback
    else:
        code_to_execute = code_blocks[0]

    code_to_execute = _auto_fix_r_code(code_to_execute)

    try:
        temp_file_path = f'/data/yangyuming/projects/chart_generation/chartWithTemplate+{model_name}/chart_{index:04d}/temp_code.R'
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        with open(temp_file_path, 'w', encoding='utf-8') as f:
            f.write(code_to_execute)

        subprocess.run(["Rscript", temp_file_path], check=True)

    except Exception as e:
        chart_subfolder_path = f'/data/yangyuming/projects/chart_generation/chartWithTemplate+{model_name}/chart_{index:04d}'
        if os.path.exists(chart_subfolder_path):
            shutil.rmtree(chart_subfolder_path)
        print(f"执行 R 代码时发生错误，已删除数据文件夹 {index:04d}")
        raise e

# def _sanitize_output_r(text: str, index: int):
#     """
#     提取并执行生成的 R 代码块（使用 subprocess 调用 Rscript）。
#     """
#     # 1. 提取 R 代码块
#     code_blocks = re.findall(r'```r\s*(.*?)```', text, re.M | re.S)
    
#     if not code_blocks:
#         # 如果没有找到 R 代码块，就把整个 text 当作 R 代码
#         code_to_execute = text
#     else:
#         # 如果找到多个，只执行第一个
#         code_to_execute = code_blocks[0]
    
#     try:
#         # 2. 写入临时文件  
#         temp_file_path = f'/data/yangyuming/projects/chart_generation/chartWithTemplate/chart_{index:04d}/temp_code.R'
#         os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
#         with open(temp_file_path, 'w', encoding='utf-8') as f:
#             f.write(code_to_execute)
        
#         # 3. 用 Rscript 执行
#         subprocess.run(["Rscript", temp_file_path], check=True)
        
#     except Exception as e:
#         # 如果执行错误，删除生成的文件夹  /data/yangyuming/projects/chart_generation/chart
#         chart_subfolder_path = f'/data/yangyuming/projects/chart_generation/chartWithTemplate/chart_{index:04d}'
#         if os.path.exists(chart_subfolder_path):
#             shutil.rmtree(chart_subfolder_path)
#         print(f"执行 R 代码时发生错误，已删除数据文件夹 {index:04d}")
#         raise e
