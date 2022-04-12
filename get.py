import requests
from bs4 import BeautifulSoup
import json
import re

r = requests.get('https://yandex.ru/')
#print(r.text)

otvet_text = r.content
print(otvet_text)

zzz = otvet_text.json()

#(otvet_text)
#with open('primer.txt', 'w', encoding='utf-8') as f:
#    f.write(otvet_text)
#pattern = r'''<span class="news__item-content">Путин назвал происходящее на&nbsp;Украине трагедией</span>'''
#result = re.findall(pattern, otvet_text)
#print(result)

