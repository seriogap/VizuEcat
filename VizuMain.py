import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

from VizuVizu import Ui_MainWindow
from VizuEcat import EcatParser


class VizuEcatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.filename = ""
        self.sdoList = []  # empty SDO list
        self.pdoList = []  # empty PDO list
        self.addrSet = set()  # unique list of objects
        self.clearFlag = False
        self.setupUi(self)
        self.modifyUi()

    def modifyUi(self):
        self.importButton.clicked.connect(self.importButtonClicked)
        self.filterComboBox.currentIndexChanged.connect(self.addrFilter)
        self.bigEndianCheckBox.stateChanged.connect(self.refreshTable)

    def refreshTable(self):
        self.addrFilter(0)

    def addrFilter(self, num):
        addr = self.filterComboBox.currentText()

        if self.clearFlag:
            return
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

        self.pdoList = parser.getPdoList()

        # get the SDO list
        self.sdoList = parser.getSdoList()

        self.printSdoTable(self.sdoList)
        self.clearFlag = True
        self.filterComboBox.clear()
        self.filterComboBox.addItems(self.addrSet)
        self.clearFlag = False

    def printSdoTable(self, sdoList):
        # Clear the table
        self.sdoTableWidget.setRowCount(0)

        # print table header
        headerLabels = ['No', 'Addr', 'Index', 'SubIndex', "Sdo type", 'Data']

        self.sdoTableWidget.setColumnCount(6)

        # set header and size
        self.sdoTableWidget.setHorizontalHeaderLabels(headerLabels)
        # self.sdoTableWidget.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        # self.sdoTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # self.sdoTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        frameList = []

        for sdoFrame in sdoList:
            rowPosition = self.sdoTableWidget.rowCount()
            self.sdoTableWidget.insertRow(rowPosition)

            self.sdoTableWidget.setItem(rowPosition, 0, QTableWidgetItem(sdoFrame['No']))
            self.sdoTableWidget.setItem(rowPosition, 1, QTableWidgetItem(sdoFrame['addr']))
            self.sdoTableWidget.setItem(rowPosition, 2, QTableWidgetItem(sdoFrame['index']))
            self.sdoTableWidget.setItem(rowPosition, 3, QTableWidgetItem(sdoFrame['subIndex']))
            self.sdoTableWidget.setItem(rowPosition, 4, QTableWidgetItem(sdoFrame['sdoType']))

            data = str(sdoFrame['data']).replace("0x", "")
            if self.bigEndianCheckBox.isChecked():
                if not "No" in data:
                    # Revert each two bytes in a string to get big endian format
                    data = data.replace(":", "")
                    data = ":".join(reversed([data[i:i + 2] for i in range(0, len(data), 2)]))

            self.sdoTableWidget.setItem(rowPosition, 5, QTableWidgetItem(data))

            # self.addrSet.add(sdoFrame['addr'])
            frameList.append(sdoFrame['addr'])

        frameList.sort()
        self.addrSet.clear()
        self.addrSet.add("")
        self.addrSet.update(frameList)


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
