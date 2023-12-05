import re
import tldextract as tld
import tkinter as tk
import requests
from urlClass import url
from htmlClass import html
from parasitesClass import parasites



def occurence (text):
	text = text.lower()
	only_words = re.sub(r'[^\w\s]', '', text)
	only_words = re.sub(r'[\r\t\n]', ' ', only_words)
	word_list = only_words.split(" ")
	word_count = {}
	for word in word_list:
		word_count[word] = word_count.get(word, 0) + 1
	return dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

def sort_url_by_domain(domain, urls):
	result = ([],[])
	for url in urls:
		if (get_domain(url) == domain):
			result[0].append(url)
		else:
			result[1].append(url)
	return result

def get_domain(url):
		return tld.extract(url).domain

if __name__ == "__main__":
	rt = tk.Tk()
	rt.title("ESO")
	entry = tk.Entry(rt)
	entry.grid(row=0, column=0)
	entry.insert(10)
	rt.mainloop()



	url_object = url(input("Enter an URL: "))
	html_object = html(url_object.get_html_from_url())
	words = occurence(html_object.html_to_text())
	parasites_object = parasites('parasites.csv')
	keywords = parasites_object.remove_parasites(words)
	print("keywords : ") 
	print(list(words.items())[0:3])

	links = html_object.get_html_attribute('a', 'href')
	sorted_links = sort_url_by_domain(get_domain(url_object.get_url()), links)
	print("backlinks : ")
	print(len(sorted_links[0]))	
	print("outbound links : ")
	print(len(sorted_links[1]))
	alt_attributes = html_object.get_html_attribute('img', 'alt')