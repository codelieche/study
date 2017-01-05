#coding=utf-8
'''
function test
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开网址首页
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # 页面中又显示了一个文本框，可以输入其它待办事项
        # 她输入 "User peocock feathers to make a fly"

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()
