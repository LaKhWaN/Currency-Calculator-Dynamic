from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *

app = QtWidgets.QApplication([])
window = uic.loadUi("E:\GitHub\Currency-Calculator-Dynamic\gui.ui")
window.show()
app.exec()