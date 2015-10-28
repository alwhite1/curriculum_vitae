from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test.client import Client
from apps.users.views import main, api


class MainPageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_root_url_resolves_to_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, main)

    def test_correct_main_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_api_url_resolves_to_api_page(self):
        found = resolve('/api/')
        self.assertEqual(found.func, api)

    def test_api_ajax_request(self):
        response = self.client.get('/api/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_api_not_ajax_request(self):
        response = self.client.get('/api/')
        self.assertEqual(response.content, 'Use ajax request')
