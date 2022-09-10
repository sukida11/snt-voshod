from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class PageCodeStatusTestCase(TestCase):

	def test_main_page_status_code(self):
		url = reverse('sntVoshod:index')
		req = self.client.get(url)
		self.assertEqual(200, req.status_code)

	def test_registration_page_status_code(self):
		url = reverse('sntVoshod:registration')
		req = self.client.get(url)
		self.assertEqual(200, req.status_code)

	def test_login_page_status_code(self):
		url = reverse('sntVoshod:login')
		req = self.client.get(url)
		self.assertEqual(200, req.status_code)

	def test_logout_page_work(self):
		url = reverse('sntVoshod:logout')
		req = self.client.get(url)
		self.assertEqual(302, req.status_code)

	def test_news_page_status_code(self):
		url = reverse('sntVoshod:news')
		req = self.client.get(url)
		self.assertEqual(200, req.status_code)