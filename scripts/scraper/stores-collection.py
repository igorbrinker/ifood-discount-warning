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
        i = i + 1
        print(name)

    print('Restaurant count:', i)    

restaurants()
