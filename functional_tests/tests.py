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
        print(self.live_server_url)
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

        self.fail('Finish the test')
