import requests
from bs4 import BeautifulSoup
from requests.models import ContentDecodingError

to_curr = input("Of Which country you want to know the currency:-> ")

url = (f"https://www.google.com/search?q={to_curr}+to+inr")

r = requests.get(url)

htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')
data = soup.find_all("div")
# print(data)
# exit()
f = open("content.txt","w")
f.write(str(soup.encode("utf-8")))
f.close()

f= open('content.txt','r')
lines = f.readlines()
f.close()

for line in lines:
    if "Indian Rupee" in line:
        data = line.split()
        print(f"{to_curr} in Indian Rupee = "+data[data.index("Indian")-1].split(">")[1])
        break
