#coding=utf-8
'''
function test
'''
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    # ch07-1001
    def  test_layout_and_styling(self):
        # yds访问网站首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她看到输入框完美地居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        # print(inputbox.location['x'] , inputbox.size['width'])
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )


