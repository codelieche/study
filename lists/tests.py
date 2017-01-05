from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

from lists.views import home_page
from lists.models import Item

# Create your tests here.
class HomePageTest(TestCase):


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # print(repr(response.content))
        # print(get_token(request))
        expected_html = render_to_string('home.html', request=request)
        # 由于每次request中的csrf_token会变更，就取前100个字符对比将就下先。
        self.assertEqual(response.content.decode()[:100], expected_html[:100])

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'},
            request=request
        )
        # print(expected_html)
        # print(response.content.decode())
        # print(get_token(request))
        self.assertEqual(response.content.decode()[:100], expected_html[:100])

        
class ItemModelTest(TestCase):

    def test_saving_adn_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')