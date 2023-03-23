from bs4 import BeautifulSoup
import requests
from URLs import Url1_flat, Url1_stove, Url1_garden, Url1_travel

def parsing1_flat():
    url = Url1_flat
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    