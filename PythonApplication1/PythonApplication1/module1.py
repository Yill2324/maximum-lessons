import requests


from bs4 import BeautifulSoup
from datetime import datetime



url = "http://www.cbr.ru/scripts/XML_daily.asp?"


today = datetime.today()
today = today.strftime("%d/%m/%y")


payload = {"date_req": today}

response = requests.get(url, params = payload)

soup=BeautifulSoup(response.content, "lxml")


def getCourse(id):
    return str(soup.find("valete",{'id': id}).valute.text)



