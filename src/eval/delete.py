"""清理缺少必要文件的图表目录。

用法：
    python delete.py <目录>
    python delete.py <目录> --dry-run    # 只列出将被删除的目录，不实际删除

会删除目录下「不同时包含 .R / .png / .json 三种文件」的子目录。
"""
import argparse
import os
import shutil

REQUIRED_EXTENSIONS = {".R", ".png", ".json"}


def has_required_files(folder_path):
    files = {os.path.splitext(f)[1] for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))}
    return REQUIRED_EXTENSIONS.issubset(files)


def delete_subdirectories(parent_folder, dry_run=False):
    """删除缺少必要文件的子目录，返回被处理的目录数。"""
    if not os.path.isdir(parent_folder):
        raise SystemExit(f"目录不存在：{parent_folder}")

    count = 0
    subdirs = [os.path.join(parent_folder, d) for d in sorted(os.listdir(parent_folder))
               if os.path.isdir(os.path.join(parent_folder, d))]
    for subdir in subdirs:
        if has_required_files(subdir):
            continue
        count += 1
        if dry_run:
            print(f"[dry-run] 将删除: {subdir}")
        else:
            print(f"缺少必要文件，正在删除: {subdir}")
            shutil.rmtree(subdir)
    print(f"合计 {count} 个目录" + ("（未实际删除）" if dry_run else "已删除"))
    return count


def main():
    parser = argparse.ArgumentParser(description="清理缺少必要文件的图表目录")
    parser.add_argument("folder", help="要清理的父目录")
    parser.add_argument("--dry-run", action="store_true", help="只列出，不删除")
    args = parser.parse_args()
    delete_subdirectories(args.folder, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
