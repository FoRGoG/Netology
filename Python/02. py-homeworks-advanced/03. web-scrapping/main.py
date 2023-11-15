import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers_gen = Headers(os='win', browser='chrome')

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/',headers=headers_gen.generate())
html_data = response.text

main_soup = BeautifulSoup(html_data, 'lxml')
articles_list = main_soup.find('div', class_='tm-articles-list')
articles_tags = articles_list.find_all('article')

parsed_data = []

for article_tag in articles_tags:
    date_tag = article_tag.find('time')
    publish_time = date_tag['title'] # Дата заголовка

    header_tag = article_tag.find('h2')
    header = header_tag.text # Название заголовка

    link_tag = article_tag.find('a') # tag [href]
    link_relative = link_tag['href']
    link_absolute = f'https://habr.com{link_relative}' # Ссылка заголовка


    article_full_html = requests.get(link_absolute, headers=headers_gen.generate()).text
    article_full_soup = BeautifulSoup(article_full_html, 'lxml')

    text_tag = article_tag.find('div', class_='tm-article-body tm-article-snippet__lead')
    text_res = text_tag.text.strip() # Текст внутри заголовка
    for i in KEYWORDS:
        if i in text_res:
            parsed_data.append({
                'data': publish_time,
                'header': header,
                'link': link_absolute,
                'text': text_res
            })

for j in parsed_data:
    print({j['data']}, {j['header']}, {j['link']})



