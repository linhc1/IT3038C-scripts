import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://shop.atlassociety.org/collections/ebooks/products/pocket-guide-to-capitalism").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"h2 product-single__title"})
title = span.text
span = soup.find("span", {"id":"ProductPrice-7170998927449"})
price = span.text
span = soup.find("div", {"class":"product-single__description-full rte"})
description = span.text
print("Book %s has price %s" % (title, price))
print("The book description is: %s." % (description))

