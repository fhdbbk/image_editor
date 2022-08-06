import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()

windows.resize(500,500)
windows.move(100,100)
windows.setWindowTitle('Editor')
windows.setWindowIcon(QtGui.QIcon('images/icon.png'))
windows.show()
sys.exit(app.exec_())