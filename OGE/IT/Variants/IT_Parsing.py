from bs4 import BeautifulSoup
import requests
from OGE.IT.IT_URLs import Url_var1

def parsing_IT_var1():
    url = Url_var1
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all("div", class_="nobreak")
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text

for i in parsing_IT_var1():
    print(i)