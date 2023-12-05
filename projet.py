import re
from bs4 import BeautifulSoup as bs
import tldextract as tld
import requests

def occurence (text):
	text = text.lower()
	only_words = re.sub(r'[^\w\s]', '', text)
	only_words = re.sub(r'[\r\t\n]', ' ', only_words)
	word_list = only_words.split(" ")
	word_count = {}
	for word in word_list:
		word_count[word] = word_count.get(word, 0) + 1
	return dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

def remove_parasites(word_count, parasites_list):
	for parasites in parasites_list:
		word_count.pop(parasites, None)
	return word_count

def get_parasites_list():
	with open('parasites.csv', 'r') as file:
		return [line.strip() for line in file]

def html_to_text(html):
	return bs(html, "html.parser").get_text()

def get_html_attribute(html, tag, attribute):
	result = []
	html_file = bs(html, "html.parser")
	for element in html_file.find_all(tag):
		result.append(element.get(attribute, None))
	return result

def get_domain(url):
	return tld.extract(url).domain

def sort_url_by_domain(domain, urls):
	result = ([],[])
	for url in urls:
		if (get_domain(url) == domain):
			result[0].append(url)
		else:
			result[1].append(url)
	return result

def get_html_from_url(url):
	return requests.get(url).text


url = input("Enter an URL: ")
print("url")
html = get_html_from_url(url)
words = occurence(html_to_text(html))
keywords = remove_parasites(words, get_parasites_list())
print("keywords : ") 
print(list(words.items())[0:3])

links = get_html_attribute(html, 'a', 'href')
sorted_links = sort_url_by_domain(get_domain(url), links)
print("backlinks : ")
print(len(sorted_links[0]))
print("outbound links : ")
print(len(sorted_links[1]))
alt_attributes = get_html_attribute(html, 'img', 'alt')