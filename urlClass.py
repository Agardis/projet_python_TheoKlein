import tldextract as tld
import requests

class url:
	def __init__(self, url):
		self.url = url

	def get_url(self):
		return self.url

	def get_html_from_url(self):
		return requests.get(self.url).text