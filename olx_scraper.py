import requests
from bs4 import BeautifulSoup
import csv

# URL inicial apra o nosso crawler
start_url = 'https://www.olx.com.br/imoveis?q=Presidente+Prudente'

def get_last_page_index(start_url):
    page = requests.get(start_url).text
    soup = BeautifulSoup(page, 'html.parser')

    last_page_link = soup.find('a', {'class': 'link', 'title': 'Última página'})
    last_page_link = last_page_link['href']
    last_page_id = last_page_link.split('q=')[0]
    last_page_id = last_page_id.split('?o=')[1][:-1]

    return last_page_id

def crawl_results(start_url):

    page_id = get_last_page_index(start_url)
    for i in range(int(page_id)):
        print(f'Processando pagina {i}...')
        url = start_url.split('?')
        url = f'{url[0]}?o={i}&{url[1]}'
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
            
            with open('house_list.csv', 'a') as f:
                print(f'Salvando registros encontrados...')
                csv_writer = csv.writer(f)
                csv_writer.writerow([title, price, detail, category])

    print(f'Todas as páginas foram processadas!')

crawl_results(start_url)