#general imports
from genericpath import exists
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import requests
import re

drive = webdriver.Chrome(executable_path=r'../../src/media/chromedriver-102.exe')

def menu():
    with open('../../src/data/stores-collection/stores.json', 'r', encoding='utf8') as input:
       input_data = json.load(input)

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    # i = 0

    output = []

    # while i < (len(input_data)):
        # print(i)
        #getting all the urls saved until the last id
    target_url = input_data[1]['url']
    driver.get(target_url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    bfs = BeautifulSoup(page.content, 'html.parser')
    lists = bfs.find_all('div')

    print(target_url, '\n\n\n\n\n\n\n\n')
    print(lists, '\n')

        # for list in lists:
        #     name = list.find('h1', class_='merchant-info__title').text.replace('\n', ' ')
        #     print(name)

        # i+= 1

        
menu()