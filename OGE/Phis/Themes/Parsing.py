from bs4 import BeautifulSoup
import requests
from OGE.Math.URLs import Url1_flat, Url1_stove, Url1_garden, Url1_travel, Url_1var

def parsing_Phis_value():
    url = 'https://phys-oge.sdamgia.ru/test?theme=19'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_value():
    print(i)
def parsing_Phis_formulas_values():
    url = 'https://phys-oge.sdamgia.ru/test?theme=32'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_formulas_values():
    print(i)
def parsing_Phis_temp_v1():
    url = 'https://phys-oge.sdamgia.ru/test?theme=7'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_temp_v1():
    print(i)
def parsing_Phis_temp_v2():
    url = 'https://phys-oge.sdamgia.ru/test?theme=8'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_temp_v2():
    print(i)
def parsing_Phis_effect():
    url = 'https://phys-oge.sdamgia.ru/test?theme=39'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_effect():
    print(i)
def parsing_Phis_dinamic():
    url = 'https://phys-oge.sdamgia.ru/test?theme=36'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_dinamic():
    print(i)
def parsing_Phis_wave():
    url = 'https://phys-oge.sdamgia.ru/test?theme=46'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_wave():
    print(i)
def parsing_Phis_temp_ex():
    url = 'https://phys-oge.sdamgia.ru/test?theme=37'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_temp_ex():
    print(i)
def parsing_Phis_electrostatic():
    url = 'https://phys-oge.sdamgia.ru/test?theme=44'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_electrostatic():
    print(i)
def parsing_Phis_radio():
    url = 'https://phys-oge.sdamgia.ru/test?theme=45'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_radio():
    print(i)
def parsing_Phis_temp_mech():
    url = 'https://phys-oge.sdamgia.ru/test?theme=34'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_temp_mech():
    print(i)
def parsing_Phis_op_electic():
    url = 'https://phys-oge.sdamgia.ru/test?theme=35'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_op_electic():
    print(i)
def parsing_Phis_graph():
    url = 'https://phys-oge.sdamgia.ru/test?theme=21'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_graph():
    print(i)
def parsing_Phis_diagram():
    url = 'https://phys-oge.sdamgia.ru/test?theme=42'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_diagram():
    print(i)
def parsing_Phis_scientific_knowledge():
    url = 'https://phys-oge.sdamgia.ru/test?theme=16'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_scientific_knowledge():
    print(i)
def parsing_Phis_laws():
    url = 'https://phys-oge.sdamgia.ru/test?theme=22'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_laws():
    print(i)
def parsing_Phis_exp_tusk():
    url = 'https://phys-oge.sdamgia.ru/test?theme=24'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_exp_tusk():
    print(i)
def parsing_Phis_matching_elements():
    url = 'https://phys-oge.sdamgia.ru/test?theme=38'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_matching_elements():
    print(i)
def parsing_Phis_txt_information():
    url = 'https://phys-oge.sdamgia.ru/test?theme=47'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_txt_information():
    print(i)
def parsing_Phis_usage_txt_inf():
    url = 'https://phys-oge.sdamgia.ru/test?theme=23'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_usage_txt_inf():
    print(i)
def parsing_Phis_quality_task_v1():
    url = 'https://phys-oge.sdamgia.ru/test?theme=48'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_quality_task_v1():
    print(i)
def parsing_Phis_quality_task_v2():
    url = 'https://phys-oge.sdamgia.ru/test?theme=25'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_quality_task_v2():
    print(i)
def parsing_Phis_calculation_task_v1():
    url = 'https://phys-oge.sdamgia.ru/test?theme=40'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_calculation_task_v1():
    print(i)
def parsing_Phis_calculation_task_v2():
    url = 'https://phys-oge.sdamgia.ru/test?theme=26'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_calculation_task_v2():
    print(i)
def parsing_Phis_calculation_task_v3():
    url = 'https://phys-oge.sdamgia.ru/test?theme=27'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='nobreak')
    quotes_text = []
    for quote in quotes:
        quotes_text.append(quote.text)
    return quotes_text


for i in parsing_Phis_calculation_task_v3():
    print(i)