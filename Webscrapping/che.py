import re
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
r= requests.get("https://buraqstore.com/product-category/women/bottoms/")
s=soup(r.content,'lxml')
productlist = s.find_all('li',{"class": "item"})


hh=[]
x=[]
for item in productlist:
    for link2 in item.find_all('span', {"class": "price"}):
        hh.append(link2.get_text().strip())

# for al in hh:
#     if(re.split("\s", al) == True):
#         hh.pop(al)
#     else:
#         x.append(al)
# print("list",x)
# print(hh)
for i, j in enumerate(hh):
    front, mid, end = j.partition(' ')
    x.append(front)

print("xlist",x)
