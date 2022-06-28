#general imports
from genericpath import exists
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import requests
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def menu():
    with open('../../src/data/stores-collection/stores.json', 'r', encoding='utf8') as input:
       input_data = json.load(input)

    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    i = 0

    output = []

    while i < (len(input_data)):
    # while i < 1:
        #getting all the urls saved until the last id
        target_url = input_data[i]['store_url']
        store_id = input_data[i]['store_id']
        driver.get(target_url)
        time.sleep(10)
        page = driver.page_source
        bfs = BeautifulSoup(page, features='lxml')
        lists = bfs.find_all('main', class_='main-layout')

        for list in lists:

            products = []
            product_id = 0

            try:
                store_name = list.find('h1', class_='merchant-info__title').text
                fast_menu = list.find_all('div', class_='restaurant__fast-menu')
                time.sleep(3)

                print(store_name)

                for menus in fast_menu:
                    menu = menus.find_all('div', class_='restaurant-menu-group')
                    print(len(menu))
                    time.sleep(3)
                
                    for item in menu:
                        menu_sections = item.find_all('div', class_='dish-card-wrapper')
                        for item_section in menu_sections:
                            try:
                                product_name = item_section.find('h3', class_='dish-card__description').text
                            except AttributeError:
                                product_name = ''
                            try:
                                product_description = item_section.find('span', class_='dish-card__details').text
                            except AttributeError:
                                product_description = ''
                            try:
                                product_price = item_section.find('span', class_='dish-card__price').text
                            except AttributeError:
                                product_price = ''

                            product = {
                                "product_id": product_id,
                                "product_name": product_name,
                                "product_description": product_description , 
                                "product_price":product_price
                            }

                            products.append(product)
                            
                            product_id+= 1
                
                print(products)

                time.sleep(5)
                    
                i+= 1

            except AttributeError:
                try:
                    store_name = list.find('h1', class_='market-header__title').text
                except AttributeError:
                    store_name = ''

                # print(restaurant_name)
                # time.sleep(5)
                i+= 1

            data = {
                "store_id": store_id,
                "store_name": store_name,
                "store_products": products
            }


            output.append(data)

    with open('../../src/data/stores-menu/stores-menu.json', 'a+', encoding='utf8') as file:
        json.dump(output, file, ensure_ascii = False, indent = 6, sort_keys = True)

    driver.quit()
        
menu()