from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
import requests
from bs4 import BeautifulSoup
from requests.models import ContentDecodingError

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
            # print(line)
            # data = line.split()
            print(line)
            # for i in data:
            #     print(i)
            #     if cont2 in i:
            #         print(i)
            try:
                valcurr=data[data.index(cont1)-1].split(">")[1]
                # print(f"{cont2} in Indian Rupee = "+valcurr)
                print(valcurr)
                return valcurr

            except Exception:
                    pass
    return "NOT WORKING"

app = QtWidgets.QApplication([])
window = uic.loadUi("E:\GitHub\Currency-Calculator-Dynamic\gui.ui")
f = open("country.txt","r")
window.dropDown1.addItem("Select")
window.dropDown2.addItem("Select")
for i in f.readlines():
    window.dropDown1.addItem(i)
    window.dropDown2.addItem(i)
intOnly = QDoubleValidator()
window.lineEdit.setValidator(intOnly)
def main():
    window.pushButton.clicked.connect(changeBtn)

def changeBtn():
    # text = window.textEdit.toPlainText()
    # print(text)
    # window.textEdit_2.setPlainText("Ok working")
    # print(window.dropDown1.currentText())
    # val1 = window.textEdit.toPlainText()
    # val2 = window.textEdit_2.toPlainText()
    cont1 = window.dropDown1.currentText()
    cont2 = window.dropDown2.currentText()
    print(getVal(cont1.rstrip(),cont2.rstrip()))
    

main()
window.show()
app.exec()