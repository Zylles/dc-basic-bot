from bs4 import BeautifulSoup
import requests

#----------------------------------------DOLAR-----------------
url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

sayfa = requests.get(url1)

html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

dolar = html_sayfa.find("div",class_="YMlKec fxKbKc").getText()

roundeddolor = round(float(float(dolar.replace(",","."))),2)
#-----------------------------------------------EURO
url2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

sayfa2 = requests.get(url2)

html_sayfa2 = BeautifulSoup(sayfa2.content,"html.parser")

euro = html_sayfa2.find("div",class_="YMlKec fxKbKc").getText()

roundeeuro = round(float(float(euro.replace(",","."))),2)

print(dolar+" "+ euro)