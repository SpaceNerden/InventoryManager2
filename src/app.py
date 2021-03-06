from appui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import database
import re

main_db = 'mainDatabase.csv'


class Application(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButtonEdit.clicked.connect(self.editItem)
        self.pushButtonNew.clicked.connect(self.newItem)

    def newItem(self):
        print("Calling NewItem")
        itemName = self.itemNameNew.text()
        itemName.strip()
        itemBrand = self.itemBrandNew.text()
        itemBrand.strip()
        itemCode = self.itemCodeNew.text()
        itemCode.strip()
        itemStock = self.itemStockNew.text()
        itemStock.strip()
        datet = self.itemDateNew.date().toPyDate()
        date = datet.strftime("%d/%m/%y")
        database.new_item(itemName, itemBrand, itemCode, itemStock, date)



    def editItem(self):
        print("Calling EditItem")
        itemCode = self.itemCodeEdit.text()
        re.sub(r"\d", "", itemCode)
        newNetStock = self.itemStockEdit.text()
        newNetStock.strip()
        datet = self.itemDateNew.date().toPyDate()
        date = datet.strftime("%d/%m/%y")
        database.edit_item(itemCode,newNetStock,date)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Application(MainWindow)

MainWindow.show()
app.exec_()
