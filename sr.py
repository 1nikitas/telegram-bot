from aiogram import Bot, Dispatcher, types, executor
from bs4 import BeautifulSoup
import requests
def to_num(string):
    num = ""
    for i in str(string):
        if i.isdigit():
            num+=i
    return num

url = "https://www.wildberries.ru/catalog/12403169/detail.aspx?targetUrl=MI"
request = requests.get(url)
page = BeautifulSoup(request.text, "lxml").find("span", class_="price-block__final-price")
res = str(199990)

if to_num(page.text) == res:
    print("1")