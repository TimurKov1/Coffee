import sys
import sqlite3
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QTableWidgetItem

titles = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса', 'Цена', 'Объем упаковки']


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(titles)
        for i in range(len(titles)):
            self.table.horizontalHeaderItem(i).setToolTip(titles[i])
        self.show_coffee()

    def show_coffee(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = list(sorted(cur.execute(f"""SELECT * FROM Coffees""").fetchall(), key=lambda x: x[0]))

        for i in range(len(data)):
            self.table.setRowCount(i + 1)
            for j in range(len(titles)):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())