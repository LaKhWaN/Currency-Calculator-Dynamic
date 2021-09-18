import requests
from bs4 import BeautifulSoup
from requests.models import ContentDecodingError

to_curr = input("To which currency you want to convert:-> ")

url = (f"https://www.google.com/search?q={to_curr}+to+inr")

r = requests.get(url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')
f = open("content.txt","w")
f.write(str(soup))
f.close()

f= open('content.txt','r')
lines = f.readlines()
f.close()

# for line in lines:
#     if "Indian Rupee" in line:
#         data = line.split()
#         # print(data)
#         value = ""
#         for char in str(data[data.index("Indian")-1]):
#             if char.isdigit() or char == ".":
#                 value += char
#         print(float(value))
#         break