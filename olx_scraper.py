import requests
from bs4 import BeautifulSoup

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
title_box = soup.find('p', attrs={'class': 'OLXad-list-price'})
title = title_box.text.strip() # remoção de tags HTML
print(title)

# Detalhes
title_box = soup.find('p', attrs={'class': 'text detail-specific'})
title = title_box.text.strip() # remoção de tags HTML
print(title)

# Regiao
title_box = soup.find('p', attrs={'class': 'text detail-region'})
title = title_box.text.strip() # remoção de tags HTML
print(title)

# categoria
title_box = soup.find('p', attrs={'class': 'text detail-category'})
title = title_box.text.strip() # remoção de tags HTML
print(title)