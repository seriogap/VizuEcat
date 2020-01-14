from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("VizuEcat")

        self.counter = 0
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("button")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.counter += 1
        self.label.setText("You pressed the button #" + str(self.counter))
        self.update()

    #
    def update(self):
        self.label.adjustSize()


def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
