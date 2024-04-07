# 一些有用的脚本
## 复制图片到所有文件夹中.py
```python
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
```

## 通过设置环境变量来调用代理脚本

假定代理运行在本机，HTTP代理端口为52345
- windows cmd
```
set http_proxy=http://127.0.0.1:52345
set https_proxy=http://127.0.0.1:52345
```
- Windows Powershell
```
$env:http_proxy = "http://127.0.0.1:52345"
$env:http_proxy = "http://127.0.0.1:52345"
```
- linux 
```
export http_proxy="http://127.0.0.1:52345"
export https_proxy="http://127.0.0.1:52345"
```
- python 

```python 
import os
os.environ["http_proxy"] = "http://127.0.0.1:52345"
os.environ["https_proxy"] = "http://127.0.0.1:52345"
```
