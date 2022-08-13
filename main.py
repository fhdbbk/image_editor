import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMenuBar, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        container = QWidget()
        layout = QGridLayout()
        container.setLayout(layout)

        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)

        actionFile = menubar.addMenu("File")
        actionFile.addAction("Open")
        actionFile.addAction("Save")
        actionFile.addSeparator()
        actionFile.addAction("Quit", self.close)

        menubar.addMenu("Help")

        self.setCentralWidget(container)

        self.resize(500, 500)
        self.move(100, 100)
        self.setWindowTitle('Editor')
        self.setWindowIcon(QIcon('images/icon.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    # sys.exit(app.exec_())