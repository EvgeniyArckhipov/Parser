import requests
from bs4 import BeautifulSoup
import json

URL= 'https://auto.ru/sankt-peterburg/cars/audi/all/'
HEADERS = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser') #здесь html.parser-аргумент нужен, для того чтобы BS4 понимал с каким параметром он работает
    #items = soup.find_all('a', class_='ListingItem__main') #получаем каждое объявление по отдельности
    #pp = json.load(get_html(URL))
    #print(soup)
    #print(pp)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.content)

    else:
        print('Error')

parse()