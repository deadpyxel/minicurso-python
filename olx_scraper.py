import requests
from bs4 import BeautifulSoup
import csv

# URL inicial apra o nosso crawler
start_url = 'https://www.olx.com.br/imoveis?q=Presidente+Prudente'

# requisitamos a página web
page = requests.get(start_url).text
soup = BeautifulSoup(page, 'html.parser')

# titulo do anuncio
title_box = soup.find_all('h2', attrs={'class': 'OLXad-list-title'})
# Preco
price_box = soup.find_all('p', attrs={'class': 'OLXad-list-price'})
# Detalhes
details_box = soup.find_all('p', attrs={'class': 'text detail-specific'})
# categoria
category_box = soup.find_all('p', attrs={'class': 'text detail-category'})

for title_ele, price_ele, details_ele, cat_ele in zip(
        title_box, price_box, details_box, category_box):
    # remove html tags
    title = title_ele.text.strip()
    price = price_ele.text.strip()
    detail = details_ele.text.strip()
    detail = ''.join(detail.split('\n'))
    detail = ''.join(detail.split('\t'))
    category = cat_ele.text.strip()
    category = ''.join(category.split('\n'))
    category = ''.join(category.split('\t'))
    print(
        f'Title: {title}, Price: {price}, Details: {detail}, Cat: {category}'
    )
    with open('house_list.csv', 'a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([title, price, detail, category])