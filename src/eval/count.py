import os

def count_subdirectories(folder_path):
    """计算指定文件夹下的子文件夹数量"""
    try:
        # 获取 folder_path 下所有的文件和文件夹
        items = os.listdir(folder_path)

        # 统计文件夹数量
        subdirs = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
        return len(subdirs)
    except FileNotFoundError:
        print("错误：指定的文件夹不存在！")
        return -1
    except PermissionError:
        print("错误：没有权限访问该文件夹！")
        return -1

# 指定要计算的文件夹路径
folder_path = "/data/yangyuming/projects/chart_generation/chartWithTemplate"  # Windows 示例路径

# 计算并打印子文件夹数量
num_subdirs = count_subdirectories(folder_path)
if num_subdirs >= 0:
    print(f"文件夹 '{folder_path}' 中共有 {num_subdirs} 个子文件夹。")
