#general imports
from distutils.log import error
from genericpath import exists
from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import re

def menu():
    with open('../../src/data/stores-collection/stores.json', 'r', encoding='utf8') as input:
       input_data = json.load(input)

    i = 0

    for data in input_data:
        try:
            i = i + 1
            #getting all the urls saved until the last id
            url = input_data[i-1]['url']
            page = requests.get(url)
            print(page, " for url", url)
            bfs = BeautifulSoup(page.content, 'html.parser')
        except:
            print(error)
        
menu()