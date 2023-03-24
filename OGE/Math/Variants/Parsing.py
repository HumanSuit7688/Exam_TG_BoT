from bs4 import BeautifulSoup
import requests
from OGE.Math.URLs import Url1_flat, Url1_stove, Url1_garden, Url1_travel, Url_1var

def parsing_var1():
    url = Url_1var
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_var1():
    print(i)
