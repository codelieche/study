from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # print(repr(response.content))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

        # 不要测试常量，应该测试实现的方式
        # self.assertTrue(response.content.startswith(b'<!DOCTYPE'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        