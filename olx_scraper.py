import requests
from bs4 import BeautifulSoup
import csv

# URL inicial apra o nosso crawler
start_url = 'https://www.olx.com.br/imoveis?q=Presidente+Prudente'

# requisitamos a página web
page = requests.get(start_url).text

soup = BeautifulSoup(page, 'html.parser')

# titulo do anuncio
title_box = soup.find('h2', attrs={'class': 'OLXad-list-title'})
title = title_box.text.strip() # remoção de tags HTML
print(title)

# Preco
price_box = soup.find('p', attrs={'class': 'OLXad-list-price'})
price = price_box.text.strip() # remoção de tags HTML
print(price)

# Detalhes
details_box = soup.find('p', attrs={'class': 'text detail-specific'})
details = details_box.text.strip() # remoção de tags HTML
print(details)

# Regiao
region_box = soup.find('p', attrs={'class': 'text detail-region'})
region = region_box.text.strip() # remoção de tags HTML
print(region)

# categoria
category_box = soup.find('p', attrs={'class': 'text detail-category'})
category = category_box.text.strip() # remoção de tags HTML
print(category)

with open('houses.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([title, price, details, region, category])