# -*- coding:utf-8 -*-
"""
选择框Select的使用
"""
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

browser.get('http://www.codelieche.com/article/create')

# 需要登陆账号，手动登陆，登陆的代码跳过了
time.sleep(5)
# 这个脚本重点演示怎么使用select

print(browser.title)

# 1. 先实例化select
# 1-1: 先找到select元素
ele_select_category = browser.find_element_by_name('category')
# 1-2：实例化Select
select = Select(ele_select_category)

# 2. 查看所有选项的值和text
for option in select.options:
    print(option.get_attribute('value'), option.text)

# 3. 选项选项
# 3-1：通过索引
select.select_by_index(index=2)
# 3-2: 通过text
select.select_by_visible_text(text="前端开发")
# 3-3: 通过value
select.select_by_value(value="4")
