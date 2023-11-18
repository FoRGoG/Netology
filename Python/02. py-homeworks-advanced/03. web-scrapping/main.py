import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

headers_gen = Headers(os='win', browser='chrome')

keywords = ['Django', 'Flask']
response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2/', headers=headers_gen.generate())
html_data = response.text

main_soup = BeautifulSoup(html_data, 'lxml')
articles_info = main_soup.find_all('div', class_='vacancy-serp-item__layout')
dictator = []
for article_info in articles_info:

    link_tag = article_info.find('a')
    link1_tag = link_tag['href'] # Здесь ссылка


    name_tag = article_info.find('h3')
    name1_tag = name_tag.text


    salary_tag = article_info.find_all('span',class_='bloko-header-section-2') # Зарплата
    if salary_tag:
         for number in salary_tag:
             salary0_tag = number.text
             salary1_tag = salary0_tag.replace(' ', ' ')
    else:
        salary1_tag = 'Зарплата не указана'


    company_tag = article_info.find_all('a', class_='bloko-link bloko-link_kind-tertiary')
    for i in company_tag:
        company0_tag = i.text
        company1_tag = company0_tag.replace('\xa0', ' ')


    city_tag = article_info.find_all('div', class_='bloko-text')
    st = []
    for x in city_tag:
        st.append(x.text.strip())
    city0_tag = st[1]
    city1_tag = city0_tag.replace('\xa0', ' ')

    page_link = link1_tag
    article_full_html = requests.get(link1_tag, headers=headers_gen.generate()).text
    article_full_soup = BeautifulSoup(article_full_html, 'lxml')

    article_full_desc = article_full_soup.find('div', class_='g-user-content')
    article_full_text = article_full_desc.text
    for keyword in keywords:
        if keyword in article_full_text:
            dictator.append({
            'Ссылка': link1_tag,
            'Зарплата': salary1_tag,
            'Название компании': company1_tag,
            'Город': city1_tag
            })


with open('result.json', 'w', encoding='utf-8') as file:
     file.write(json.dumps(dictator, ensure_ascii=False, indent=1))

