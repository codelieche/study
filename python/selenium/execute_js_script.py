# -*- coding:utf-8 -*-
"""
让browser直行javascript
"""
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('http://codelieche.com')

# 执行javascript
# 1. execute_script: 同步方法
# 用它执行js代码会阻塞主线程执行，直到js代码执行完毕
browser.execute_script("console.log('执行js'); return document.title;")
# 如果js中有返回值，会返回它，没有会返回null

# 2. execute_async_script: 异步方法,它不会阻塞主线程执行。
# async 直行这个会有异常 TimeoutException:
# Message: asynchronous script timeout: result was not received in 30 seconds
# browser.execute_script

# 3. 执行execute_script的时候，传入python中的值给脚本中
browser.execute_script("""
    var v = arguments[0];
    console.log('async script');
    var x = document.title;
    console.log(v);
    """, "这个是我传入的值")

# 4. 滚动滑动条, 滚动到某个元素
browser.execute_script('''
    var ele=document.getElementsByClassName('item-info')[3];
    ele.scrollIntoView();
    ''')
# 滑动到底部
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 5. 执行alert，然后选中点击确认
# 5-1: 弹出alert
browser.execute_script("alert('Hello Alert!')")
# 5-2：点击确认
# 老的方法：switch_to_alert已经被丢弃
# 注意：switch_to.alert不是个方法哦，不要加括号
alert = browser.switch_to.alert
alert.accept()
