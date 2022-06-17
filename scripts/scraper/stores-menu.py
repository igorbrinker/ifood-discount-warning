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
        #getting all the urls saved until the last id
        target_url = input_data[i]['url']
        driver.get(target_url)
        time.sleep(10)
        page = driver.page_source
        bfs = BeautifulSoup(page)
        lists = bfs.find_all('main', class_='main-layout')

        for list in lists:
            try:
                restaurant_name = list.find('h1', class_='merchant-info__title').text
                # print(restaurant_name)
                time.sleep(20)
                i+= 1

            except AttributeError:
                restaurant_name = list.find('h1', class_='market-header__title').text
                # print(restaurant_name)
                time.sleep(20)
                i+= 1
            
            data = {
                "restaurant_name": restaurant_name
            }

            output.append(data)

    with open('../../src/data/stores-menu/stores-menu.json', 'a+', encoding='utf8') as file:
        json.dump(output, file, ensure_ascii = False, indent = 4, sort_keys = True)

    driver.quit()
        
menu()