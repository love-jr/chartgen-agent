import re
import os
import subprocess

def _sanitize_output_r(text: str, chart_folder: str):
    """
    提取并执行生成的 R 代码块（使用 subprocess 调用 Rscript）。
    """
    # 1. 提取 R 代码块
    code_blocks = re.findall(r'```r\s*(.*?)```', text, re.M | re.S)
    
    if not code_blocks:
        # 如果没有找到 R 代码块，就把整个 text 当作 R 代码
        code_to_execute = text
    else:
        # 如果找到多个，只执行第一个
        code_to_execute = code_blocks[0]
    
    try:
        # 2. 写入临时文件  
        temp_file_path = os.path.join(chart_folder, 'new_temp_code.R')
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        with open(temp_file_path, 'w', encoding='utf-8') as f:
            f.write(code_to_execute)
        
        # 3. 用 Rscript 执行
        subprocess.run(["Rscript", temp_file_path], check=True)
        
    except Exception as e:
        # 如果执行错误，删除生成的文件夹  /data/yangyuming/projects/chart_generation/chart
        
        # if os.path.exists(chart_folder):
        #     shutil.rmtree(chart_folder)
        print(f"执行 R 代码时发生错误，文件夹 {chart_folder}")
        raise e
