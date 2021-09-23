import requests
from bs4 import BeautifulSoup
from requests.models import ContentDecodingError

# to_curr = input("Of Which country you want to know the currency:-> ")


# for i in to_curr :
#     if not i.isalpha() :
#         print("no currency found")
#         exit()



# url = (f"https://www.google.com/search?q={to_curr}+to+Bermudan Dollar")

# r = requests.get(url)

# htmlContent = r.content

# soup = BeautifulSoup(htmlContent,'html.parser')
# data = soup.find_all("div")

# f = open("content.txt","w")
# f.write(str(soup.encode("utf-8")))
# f.close()

# f= open('content.txt','r')
# lines = f.readlines()
# f.close()

# for line in lines:
#     if "Bermudan Dollar" in line:
#         data = line.split()
#         try:
#             valcurr=data[data.index("Indian")-1].split(">")[1]
#             print(f"{to_curr} in Indian Rupee = "+valcurr)
#             break

#         except Exception:
#                 print("no currency found")
#                 exit()

# ast=int(input(f"what do you want to do \n1 indian to {to_curr} \n2 {to_curr} to indian\n enter here:-> "))

# if ast==1:
#     x=int(input("enter total indian rupee domination:-> "))
#     concurr=x/float(valcurr)
#     print(str(round(concurr,2))+" "+to_curr)

# elif ast==2:
#     x=int(input(f"enter total {to_curr} domination:-> "))
#     concurr=x*float(valcurr)
#     print(str(round(concurr,2))+" "+"Indian Rupee")

def getVal(cont1,cont2):
    url = (f"https://www.google.com/search?q={cont1}+to+{cont2}")
    r = requests.get(url)

    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html.parser')
    data = soup.find_all("div")

    f = open("content.txt","w")
    f.write(str(soup.encode("utf-8")))
    f.close()

    f= open('content.txt','r')
    lines = f.read().split("</div>")
    f.close()
    for line in lines:
        if cont2 in line:
            print(line)
            print("pahunch gya")
            data = line.split()
            print(data)
            try:
                valcurr=data[data.index(cont1)-1].split(">")[1]
                # print(f"{cont2} in Indian Rupee = "+valcurr)
                print(valcurr)
                return valcurr

            except Exception:
                    print("no currency found")
                    exit()
if __name__ == "__main__":
    getVal("Algerian Dinar","Aruban Florin")