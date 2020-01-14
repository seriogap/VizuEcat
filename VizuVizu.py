# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VizuVizu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importButton = QtWidgets.QPushButton(self.centralwidget)
        self.importButton.setGeometry(QtCore.QRect(70, 60, 201, 91))
        self.importButton.setObjectName("importButton")
        self.fileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileNameLabel.setGeometry(QtCore.QRect(360, 70, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.sdoTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.sdoTableWidget.setGeometry(QtCore.QRect(60, 250, 951, 411))
        self.sdoTableWidget.setObjectName("sdoTableWidget")
        self.sdoTableWidget.setColumnCount(0)
        self.sdoTableWidget.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 160, 201, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.filterLabel.setFont(font)
        self.filterLabel.setObjectName("filterLabel")
        self.horizontalLayout.addWidget(self.filterLabel)
        self.filterComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.filterComboBox.setObjectName("filterComboBox")
        self.horizontalLayout.addWidget(self.filterComboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VizuEcat"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.fileNameLabel.setText(_translate("MainWindow", "fileName"))
        self.filterLabel.setText(_translate("MainWindow", "Filter:"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

