# -*- coding:utf-8 -*-
"""
通过selenium打开网页，然后截图
"""

from selenium import webdriver

browser = webdriver.Chrome()

# 1. 打开网页：
browser.get('http://www.codelieche.com/')

# 2. 获取图片
# 2-1: 获取base64的图片数据
# browser.get_screenshot_as_base64()

# 2-2：保存成一个文件
# 保存文件需要是.png后缀的名字
browser.get_screenshot_as_file(filename='./test123.png')

# 2-3：获取图片为png 相当于读取了png的图片
image_content = browser.get_screenshot_as_png()
# 把图片内容保存到文件中
with open('./123.png', 'wb') as f:
    f.write(image_content)


