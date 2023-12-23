import sys

from PySide6 import QtWidgets
from widget import Widget

from theme import theme

from checkFiles import CheckFiles
#CheckFiles()

app = QtWidgets.QApplication(sys.argv)

window = Widget()

theme(app)

window.show()

app.exec()