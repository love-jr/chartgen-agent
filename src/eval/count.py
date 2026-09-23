"""统计目录下的子文件夹数量。

用法：
    python count.py <目录>

不带参数时统计默认输出目录（CHARTGEN_OUTPUT_DIR 或项目根目录的 output/）。
"""
import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.output import output_dir


def count_subdirectories(folder_path):
    """计算指定文件夹下的子文件夹数量；出错返回 -1。"""
    try:
        items = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"错误：文件夹不存在：{folder_path}")
        return -1
    except PermissionError:
        print(f"错误：没有权限访问：{folder_path}")
        return -1
    return len([i for i in items if os.path.isdir(os.path.join(folder_path, i))])


def main():
    parser = argparse.ArgumentParser(description="统计目录下的子文件夹数量")
    parser.add_argument("folder", nargs="?", help="要统计的目录，默认输出根目录")
    args = parser.parse_args()

    folder = args.folder if args.folder else output_dir()
    count = count_subdirectories(folder)
    if count >= 0:
        print(f"文件夹 '{folder}' 中共有 {count} 个子文件夹。")


if __name__ == "__main__":
    main()
