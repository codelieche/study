# -*- coding:utf-8 -*-
"""
鼠标事件拖拽元素
"""
from selenium import webdriver
# ActionChains类鼠标操作的常用方法
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

# 找个有拖拽效果的站点，演示
browser.get('https://www.codelieche.com/')

# 实例化action
action = ActionChains(browser)

# 拖拽的源和目标元素
# source：鼠标按下的源元素；target：鼠标释放的目标元素
source = browser.find_element_by_css_selector('h1.logo')
target = browser.find_element_by_id('search')

action.drag_and_drop(source=source, target=target).perform()
