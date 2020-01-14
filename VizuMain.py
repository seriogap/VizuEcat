import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

from VizuVizu import Ui_MainWindow
from VizuEcat import EcatParser


class VizuEcatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.filename = ""
        self.sdoList = [] # empty list
        self.addrSet = set() # unique list of objects
        self.setupUi(self)
        self.modifyUi()

    def modifyUi(self):
        self.importButton.clicked.connect(self.importButtonClicked)
        self.filterComboBox.currentIndexChanged.connect(self.addrFilter)

    def addrFilter(self, addr):
        addr = self.filterComboBox.currentText()

        if not addr.strip():
            self.printSdoTable(self.sdoList)
            return
        if not self.filename:
            return

        filterdList = []
        for sdo in self.sdoList:
            if addr in sdo['addr']:
                filterdList.append(sdo)

        self.printSdoTable(filterdList)

    def importButtonClicked(self):
        # open file
        dialog = QFileDialog()
        dialog.setWindowTitle('Open File')
        dialog.setNameFilter('json (*.json)')
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_() == QFileDialog.Accepted:
            self.filename = dialog.selectedFiles()[0]
            self.fileNameLabel.setText(self.filename)
            self.fileNameLabel.adjustSize()

        # parse the file
        parser = EcatParser(self.filename)
        parser.parse()

        # get the SDO list
        self.sdoList = parser.getSdoList()

        self.printSdoTable(self.sdoList)

    def printSdoTable(self, sdoList):
        # Clear the table
        self.sdoTableWidget.setRowCount(0)

        # print table header
        headerLabels = ['No', 'Addr', 'Index', 'SubIndex', 'Data']

        self.sdoTableWidget.setColumnCount(5)

        # set header and size
        self.sdoTableWidget.setHorizontalHeaderLabels(headerLabels)
        # self.sdoTableWidget.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        # self.sdoTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # self.sdoTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self.addrSet.clear()
        self.addrSet.add("")

        for sdoFrame in sdoList:
            rowPosition = self.sdoTableWidget.rowCount()
            self.sdoTableWidget.insertRow(rowPosition)

            self.sdoTableWidget.setItem(rowPosition, 0, QTableWidgetItem(sdoFrame['No']))
            self.sdoTableWidget.setItem(rowPosition, 1, QTableWidgetItem(sdoFrame['addr']))
            self.sdoTableWidget.setItem(rowPosition, 2, QTableWidgetItem(sdoFrame['index']))
            self.sdoTableWidget.setItem(rowPosition, 3, QTableWidgetItem(sdoFrame['subIndex']))
            self.sdoTableWidget.setItem(rowPosition, 4, QTableWidgetItem(sdoFrame['data']))

            self.addrSet.add(sdoFrame['addr'])

        self.filterComboBox.addItems(self.addrSet)


def main():
    app = QApplication(sys.argv)
    # create instance of VizuEcatWindow
    main = VizuEcatWindow()
    # show - start the GUI
    main.show()
    # controlled exit
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

