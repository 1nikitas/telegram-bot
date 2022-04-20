from aiogram import Bot, Dispatcher, types, executor
from bs4 import BeautifulSoup
import requests
import time
bot = Bot(token="5133571136:AAE63xZLAWigiSklG_ctyz10dfLNXliMRyQ")
dp = Dispatcher(bot)

def to_num(string):
    num = ""
    for i in str(string):
        if i.isdigit():
            num+=i
    return num


@dp.message_handler(text='/go')
async def sending(message: types.Message):
    url = "https://www.wildberries.ru/catalog/12403169/detail.aspx?targetUrl=MI"
    request = requests.get(url)
    page = BeautifulSoup(request.text, "lxml").find("span", class_="price-block__final-price")
    res = str(199990)
    while True:
        if res == to_num(page.text):
            pass
        else:
            await message.answer(f'New price: {to_num(page.text)}')
            time.sleep(100)



if __name__ == "__main__":
    executor.start_polling(dp)