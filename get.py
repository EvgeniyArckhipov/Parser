import requests
from bs4 import BeautifulSoup
import json
import re

r = requests.get('https://www.fontanka.ru/incidents/')
otvet_text = r.text
# print(type(otvet_text))
# def zapis_site():
#     with open('copy_site.txt', 'w', encoding='utf-8') as f:
#         f.write(otvet_text)
#
# with open('copy_site.txt', encoding='utf-8') as site:
#     q = site.read()
soup = BeautifulSoup(otvet_text, 'lxml')
h3 = soup.h3
po_vsemu = soup.findAll('h3')
zagalovki = []
for i in po_vsemu:
    zagalovki.append(i.text)
print('\n'.join(zagalovki))