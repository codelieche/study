#coding=utf-8
'''
function test
'''
from unittest import skip

from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    # @skip
    def test_cannot_add_empty_list_items(self):
        # yds访问首页，不小心提交了一个空的待办事项
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # 首页刷新了，显示一个错误消息
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入一些文字，然后再次提交，这次没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # 她有点儿调皮，又提交了一个空待办事项
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # 在列表页她看到了一个类似的错误消息
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 输入文字之后就没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        # self.fail("Write me!")

