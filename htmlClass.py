from bs4 import BeautifulSoup as bs

class html:

	def __init__(self, html):
		self.html_text = html

	def html_to_text(self):
		return bs(self.html_text, "html.parser").get_text()

	def get_html_attribute(self, tag, attribute):
		result = []
		html_file = bs(self.html_text, "html.parser")
		for element in html_file.find_all(tag):
			result.append(element.get(attribute))
		return result