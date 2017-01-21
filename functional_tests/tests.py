#coding=utf-8
'''
function test
'''
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开网址首页
        # print(self.live_server_url)
        self.browser.get(self.live_server_url)

        #网址标题,头部 是否包含'To-Do'
        # import pdb;pdb.set_trace()
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她她输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文本框中输入 "Buy peacock feathers"(购买孔雀羽毛)
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车，页面更新
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        # 检查字符串是否和正则表达式匹配。
        # self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.assertRegex(edith_list_url, '/lists/.+')
        

        # 检查
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其它待办事项
        # 她输入 "User peocock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('User peacock feathers to make a fly')
        # 她按回车，页面更新
        inputbox.send_keys(Keys.ENTER)

        # 检查
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: User peacock feathers to make a fly')

        # 现在一个叫弗朗西斯的新用户访问了网站

        ## 我们使用一个新的浏览器会话
        ## 确保eds 的信息不会从cookie中泄漏出来
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 弗朗西斯访问首页
        # 页面中看不到易迪丝的清单

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # 弗朗西斯输入一个新的待办事项，新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 弗朗西斯获得了他的唯一URL
        francis_list_url = self.browser.current_url

        self.assertRegex(francis_list_url, 'lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这个页面还是没有yds的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 两个人都很满意，去睡觉了

        # self.fail('Finish the test')
