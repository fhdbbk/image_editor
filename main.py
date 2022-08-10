import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        menubar = QtWidgets.QMenuBar()
        layout.addWidget(menubar, 0, 0)

        actionFile = menubar.addMenu("File")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addSeparator()
        actionFile.addAction("Quit", self.close)

        menubar.addMenu("Help")

        self.resize(500, 500)
        self.move(100, 100)
        self.setWindowTitle('Editor')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())