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
        self.fail("Write me!")

