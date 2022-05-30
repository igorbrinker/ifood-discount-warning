from bs4 import BeautifulSoup
import requests
from csv import writer

def restaurants():
    url = "https://www.ifood.com.br/delivery/canoas-RS"
    page = requests.get(url)
    print(page, " for url", url)

    bfs = BeautifulSoup(page.content, 'html.parser')
    lists = bfs.find_all('li', class_='restaurants-list__item-wrapper')

    i = 0

    for list in lists:
        name = list.find('span', class_='restaurant-name').text.replace('\n', '')
        kind = list.find('div', class_='restaurant-card__info').text.replace('\n', '')
        target_url = 'https://www.ifood.com.br' + list.find('a', class_='restaurant-card__link').get('href')

        i = i + 1
        print('\n--------------------')
        print('\n' + name)
        print(kind)
        print(target_url)

    print('\nRestaurant count:', i)    

restaurants()
