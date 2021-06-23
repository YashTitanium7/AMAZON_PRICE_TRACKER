import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/AMD-Ryzen-3700X-Processor-100000071BOX/dp/B07SXMZLPK/ref=sr_1_4?crid=3FQHSUBM82JRX&dchild=1&keywords=ryzen+7+5800x&qid=1624446165&sprefix=ryzen+7+%2Caps%2C350&sr=8-4'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

productTitle = soup.find(id="productTitle").get_text()
# print(productTitle.strip())
productPrice = soup.find(id="priceblock_ourprice").get_text()
productPrice = productPrice.replace('₹','')
productPrice = productPrice.replace(' ','')
productPrice = productPrice.replace(',','')
convertedPrice = int(productPrice[1:6])
print(convertedPrice)
