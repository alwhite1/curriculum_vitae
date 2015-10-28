from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test.client import Client
from apps.users.views import main


class MainPageTest(TestCase):

    def test_root_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, main)

    def test_correct_main_page_template(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'main.html')
