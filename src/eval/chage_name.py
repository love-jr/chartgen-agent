"""把子目录按顺序重命名为 chart_0001、chart_0002 …

用法：
    python chage_name.py <目录>
    python chage_name.py <目录> --dry-run    # 只列出将发生的重命名

注意：重命名不可撤销，建议先加 --dry-run 确认。
"""
import argparse
import os


def change_subdirectories(parent_folder, dry_run=False):
    """按名称排序重命名子目录，返回重命名次数。"""
    if not os.path.isdir(parent_folder):
        raise SystemExit(f"目录不存在：{parent_folder}")

    count = 0
    subdirs = sorted(os.path.join(parent_folder, d) for d in os.listdir(parent_folder)
                     if os.path.isdir(os.path.join(parent_folder, d)))
    for idx, old_path in enumerate(subdirs, start=1):
        new_path = os.path.join(parent_folder, f"chart_{idx:04d}")
        if old_path == new_path:
            continue
        count += 1
        if dry_run:
            print(f"[dry-run] {old_path} → {new_path}")
        else:
            print(f"重命名 {old_path} → {new_path}")
            os.rename(old_path, new_path)
    print(f"合计 {count} 个目录" + ("（未实际重命名）" if dry_run else "已重命名"))
    return count


def main():
    parser = argparse.ArgumentParser(description="按顺序重命名子目录为 chart_XXXX")
    parser.add_argument("folder", help="要处理的父目录")
    parser.add_argument("--dry-run", action="store_true", help="只列出，不重命名")
    args = parser.parse_args()
    change_subdirectories(args.folder, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
