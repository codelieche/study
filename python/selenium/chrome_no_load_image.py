# -*- coding:utf-8 -*-
"""
Chrome 不加载图片
注意事项：
1. chromedriver：需要是Chrome对应的版本【一般推荐最新】否则会无效
2. http://chromedriver.storage.googleapis.com/index.html
"""

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# 设置不加载图片
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.taobao.com/')

