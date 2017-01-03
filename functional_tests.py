#coding=utf-8
'''
function test
'''
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开网址首页
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        #网址标题是否包含'To-Do'
        self.assertIn('To-Do', self.browser.title)

if __name__ == '__main__':
    unittest.main()
