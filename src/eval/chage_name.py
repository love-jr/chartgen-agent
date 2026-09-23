import os

def change_subdirectories(parent_folder):
    try:
        subdirs = sorted(
            [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))]
        )
        # subdirs = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))]
        for idx, old_path in enumerate(subdirs, start=1):
            new_name = f"chart_{idx:04d}"  
            new_path = os.path.join(parent_folder, new_name)

            if old_path != new_path: 
                print(f"重命名 {old_path} → {new_path}")
                os.rename(old_path, new_path)
    except Exception as e:
        print(f"发生错误: {e}")

change_subdirectories('/data/yangyuming/projects/chart_generation/chartWithTemplate')
