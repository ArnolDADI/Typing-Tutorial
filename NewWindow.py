# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_NewWindow(object):
    def setupNewUi(self, NewWindow):
        if not NewWindow.objectName():
            NewWindow.setObjectName(u"NewWindow")
        NewWindow.resize(819, 599)
        self.verticalLayout = QVBoxLayout(NewWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.labelHeaderNew = QLabel(NewWindow)
        self.labelHeaderNew.setObjectName(u"labelHeaderNew")
        self.labelHeaderNew.setMaximumSize(QSize(16777215, 100))
        self.labelHeaderNew.setText('Typing Tut')
        self.labelHeaderNew.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout.addWidget(self.labelHeaderNew)

        self.verticalSpacerNew = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerNew)

        self.lineEditNew = QLineEdit(NewWindow)
        self.lineEditNew.setObjectName(u"lineEditNew")

        self.verticalLayout.addWidget(self.lineEditNew)

        self.labelWarnNew = QLabel(NewWindow, text = '')
        self.labelWarnNew.setObjectName(u"labelWarnNew")
        self.labelWarnNew.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.labelWarnNew)

        self.buttonContinueNew = QPushButton(NewWindow ,text= 'Continue')
        self.buttonContinueNew.setObjectName(u"buttonContinueNew")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonContinueNew.sizePolicy().hasHeightForWidth())
        self.buttonContinueNew.setSizePolicy(sizePolicy)
        self.buttonContinueNew.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setPointSize(24)
        font.setItalic(True)
        self.buttonContinueNew.setFont(font)

        self.verticalLayout.addWidget(self.buttonContinueNew)

        self.horizonBottom = QHBoxLayout()
        self.horizonBottom.setObjectName(u"horizonBottom")

        self.buttonHomeNew = QPushButton(NewWindow, text = 'Home')
        self.buttonHomeNew.setObjectName(u"buttonHomeNew")
        sizePolicy.setHeightForWidth(self.buttonHomeNew.sizePolicy().hasHeightForWidth())
        self.buttonHomeNew.setSizePolicy(sizePolicy)
        self.buttonHomeNew.setMinimumSize(QSize(200, 200))
        self.buttonHomeNew.setFont(font)

        self.horizonBottom.addWidget(self.buttonHomeNew)

        self.buttonExitNew = QPushButton(NewWindow, text = 'Exit')
        self.buttonExitNew.setObjectName(u"buttonExitNew")
        sizePolicy.setHeightForWidth(self.buttonExitNew.sizePolicy().hasHeightForWidth())
        self.buttonExitNew.setSizePolicy(sizePolicy)
        self.buttonExitNew.setMinimumSize(QSize(200, 200))
        self.buttonExitNew.setFont(font)

        self.horizonBottom.addWidget(self.buttonExitNew)

        self.verticalLayout.addLayout(self.horizonBottom)

        QMetaObject.connectSlotsByName(NewWindow)
    # setupUi


