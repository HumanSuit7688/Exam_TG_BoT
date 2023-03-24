from bs4 import BeautifulSoup
import requests
from OGE.IT.IT_URLs import Url_information_objects

def parsing_IT_information_objects():
    url = Url_information_objects
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all("div", class_="nobreak")
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text

for i in parsing_IT_information_objects():
    print(i)

