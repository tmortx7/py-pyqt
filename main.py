import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class WelcomeScreen(QDialog):
  def __init__(self):
    super(WelcomeScreen, self).__init__()
    loadUi("welcomescreen.ui", self)

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(400)
widget.setFixedWidth(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")