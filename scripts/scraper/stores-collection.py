from genericpath import exists
from bs4 import BeautifulSoup
import json
import requests
import re

def restaurants():
    url = "https://www.ifood.com.br/delivery/canoas-RS"
    page = requests.get(url)

    bfs = BeautifulSoup(page.content, 'html.parser')
    lists = bfs.find_all('li', class_='restaurants-list__item-wrapper')

    i = 0

    output = []

    for list in lists:
        name = list.find('span', class_='restaurant-name').text.replace('\n', '')
        kind = list.find('div', class_='restaurant-card__info').text.replace('\n', '')
        target_url = 'https://www.ifood.com.br' + list.find('a', class_='restaurant-card__link').get('href')
        
        i+= 1

        data = {
            'id': i,
            'name': name,
            'kind': kind,
            'url': target_url
        }

        output.append(data)


    with open('../../src/data/stores-collection/stores.json', 'a+', encoding='utf8') as file:
        json.dump(output, file, ensure_ascii = False, indent = 4, sort_keys = True)

    print('\nRestaurant count:', i) 


restaurants()
