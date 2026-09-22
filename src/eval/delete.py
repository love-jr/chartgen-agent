import os
import shutil 

def has_required_files(folder_path):
    required_extensions = {".R", ".png", ".json"}
    
    files = {os.path.splitext(f)[1] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))}
    
    return required_extensions.issubset(files)

def delete_subdirectories(parent_folder):
    try:
        subdirs = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))]
        
        for subdir in subdirs:
            if not has_required_files(subdir): 
                print(f"缺少必要文件，正在删除: {subdir}")
                shutil.rmtree(subdir)  
                
    except Exception as e:
        print(f"发生错误: {e}")


delete_subdirectories('/data/yangyuming/projects/chart_generation/chartWithTemplate')
