import requests
from bs4 import BeautifulSoup
import pprint
import bs4
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

respons = requests.get('https://habr.com/ru/all/')
if not respons.ok:
    raise Exception('respons not ok')

text = respons.text

soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')

for article in articles:
    for i in KEYWORDS:
        if i in article.text:
            time = article.find('span', class_='tm-article-snippet__datetime-published').text
            title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            href = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
            print(f'<{time}>-<{title}>-<https:/{href}>.')