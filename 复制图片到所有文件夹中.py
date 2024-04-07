import os
import shutil

def copy_image_to_all_dirs(image_path, start_path):
    image_name = os.path.basename(image_path)  # 获取图片文件名
    for dirpath, dirnames, filenames in os.walk(start_path):
        target_path = os.path.join(dirpath, image_name)  # 构造目标路径
        if not os.path.exists(target_path):  # 如果图片在目标目录中不存在
            shutil.copy(image_path, dirpath)  # 将图片复制到这个目录中

# 使用方法：将 'image.jpg' 复制到当前目录及其所有子目录
copy_image_to_all_dirs('image.jpg', '.')