
# 适合又拍云对象储存的 url 刷新，每行一个 URL 地址，每个 URL 地址以 http:// 或 https:// 开头，每次输入不超过 50 个。
# 这段代码会提取当前目录下的 public 目录中的 sitemap-0.xml 中的 url 链接，写入到 urls.md 文件中

import xml.etree.ElementTree as ET

def extract_urls(file_name):
    # 解析XML文件
    tree = ET.parse(file_name)
    # 获取根元素
    root = tree.getroot()
    # 找到所有的loc元素
    urls = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    # 提取所有的链接
    urls = [url.text for url in urls if url.text.startswith(('http://', 'https://'))]
    # 每次处理50个URL
    for i in range(0, len(urls), 50):
        yield urls[i:i+50]

# 测试函数
with open('urls.md', 'w') as f:
    for batch in extract_urls('./public/sitemap-0.xml'):
        f.write('\n'.join(batch))
        f.write('\n')
