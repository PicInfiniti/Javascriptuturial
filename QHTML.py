import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
	def __init__(self, DB='StockData.db', parent = None):
		super(MainWindow, self).__init__(parent)
		with open("first.html") as File:
			File = File.read()
		self.label = QMessageBox()
		print (File)
		self.label.setText(File)

		Vlayout = QVBoxLayout() 
		Vlayout.addWidget(self.label) #add lable to Vlayout
		self.setLayout(Vlayout)


def main():
	app = QApplication(sys.argv)
	ex = MainWindow()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

