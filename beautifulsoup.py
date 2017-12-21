# def get_image(url):
#     import requests
#     from bs4 import BeautifulSoup 
#     soup=BeautifulSoup(open('index.html'))
#     print(soup)

import requests
from bs4 import BeautifulSoup
import re

soup=BeautifulSoup(open('index.html'),'html.parser')
# print(soup.prettify())
# print(soup.title)
# for ele in soup.head.stripped_strings:
#     print(ele)
# print(list(soup.a.next_siblings))
# print(list(soup.body.next_elements))
# print(soup.find_all(['a','title']))

def func(tag):
    return tag.has_attr('class')

print(soup.select('a')[0].get_text())
