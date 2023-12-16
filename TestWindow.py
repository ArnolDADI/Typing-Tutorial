# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget, QLineEdit)

class Ui_TestWindow(object):
    def setupTestUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(758, 557)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labeHeaderTest = QLabel(Form, text = 'Typing Tutorial')
        self.labeHeaderTest.setObjectName(u"labeHeaderTest")
        self.labeHeaderTest.setMaximumSize(QSize(16777215, 100))
        self.labeHeaderTest.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout.addWidget(self.labeHeaderTest)

        self.horizonDestailsTest = QHBoxLayout()
        self.horizonDestailsTest.setObjectName(u"horizonDestailsTest")

        self.labelUserNameTest = QLabel(Form)
        self.labelUserNameTest.setObjectName(u"labelUserNameTest")
        self.labelUserNameTest.setStyleSheet(u"font: 24 italic 20pt \"Z003\";")

        self.horizonDestailsTest.addWidget(self.labelUserNameTest)

        self.labelTimeTest = QLabel(Form, text = ' 0.00sec') 
        self.labelTimeTest.setObjectName(u"labelTimeTest")

        self.horizonDestailsTest.addWidget(self.labelTimeTest)

        self.labelCPMTest = QLabel(Form, text = '0 CPM')
        self.labelCPMTest.setObjectName(u"labelCPMTest")

        self.horizonDestailsTest.addWidget(self.labelCPMTest)

        self.labelCharTest = QLabel(Form, text = '0 Characters')
        self.labelCharTest.setObjectName(u"labelCharTest")

        self.horizonDestailsTest.addWidget(self.labelCharTest)

        self.labelWPMTest = QLabel(Form, text = '0 WPM')
        self.labelWPMTest.setObjectName(u"labelWPMTest")

        self.horizonDestailsTest.addWidget(self.labelWPMTest)

        self.labelWordTest = QLabel(Form, text = '0 Words')
        self.labelWordTest.setObjectName(u"labelWordTest")

        self.horizonDestailsTest.addWidget(self.labelWordTest)

        self.labelWrongWordTest = QLabel(Form, text = '0 Words')
        self.labelWrongWordTest.setObjectName(u"labelWordTest")

        self.horizonDestailsTest.addWidget(self.labelWrongWordTest)

        self.labelWrongCharTest = QLabel(Form, text = '0 Chars')
        self.labelWrongCharTest.setObjectName(u"labelWordTest")

        self.horizonDestailsTest.addWidget(self.labelWrongCharTest)


        self.verticalLayout.addLayout(self.horizonDestailsTest)

        self.verticalSpacerUpperTest = QSpacerItem(20, 199, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerUpperTest)

        self.horizonCharTest = QHBoxLayout()
        self.horizonCharTest.setObjectName(u"horizonCharTest")
        self.labelChar_1 = QLabel(Form)
        self.labelChar_1.setObjectName(u"labelChar_1")

        self.horizonCharTest.addWidget(self.labelChar_1)

        self.labelChar_2 = QLabel(Form)
        self.labelChar_2.setObjectName(u"labelChar_2")

        self.horizonCharTest.addWidget(self.labelChar_2)

        self.labelChar_3 = QLabel(Form)
        self.labelChar_3.setObjectName(u"labelChar_3")

        self.horizonCharTest.addWidget(self.labelChar_3)

        self.labelChar_4 = QLabel(Form)
        self.labelChar_4.setObjectName(u"labelChar_4")

        self.horizonCharTest.addWidget(self.labelChar_4)

        self.labelChar_5 = QLabel(Form)
        self.labelChar_5.setObjectName(u"labelChar_5")

        self.horizonCharTest.addWidget(self.labelChar_5)

        self.labelChar_6 = QLabel(Form)
        self.labelChar_6.setObjectName(u"labelChar_6")

        self.horizonCharTest.addWidget(self.labelChar_6)

        self.labelChar_7 = QLabel(Form)
        self.labelChar_7.setObjectName(u"labelChar_7")

        self.horizonCharTest.addWidget(self.labelChar_7)

        self.labelChar_8 = QLabel(Form)
        self.labelChar_8.setObjectName(u"labelChar_8")

        self.horizonCharTest.addWidget(self.labelChar_8)

        self.labelChar_9 = QLabel(Form)
        self.labelChar_9.setObjectName(u"labelChar_9")

        self.horizonCharTest.addWidget(self.labelChar_9)

        self.labelChar_Main = QLabel(Form)
        self.labelChar_Main.setObjectName(u"labelChar_Main")
        

        self.horizonCharTest.addWidget(self.labelChar_Main)

        self.labelChar_11 = QLabel(Form)
        self.labelChar_11.setObjectName(u"labelChar_11")
        self.labelChar_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.525, y1:1, x2:0.509804, y2:0, stop:0 rgba(79, 231, 48, 177), stop:0.5 rgba(55, 163, 211, 224), stop:0.995098 rgba(0, 255, 67, 217));\n"
"font: 16pt \"Noto Sans\";")

        self.horizonCharTest.addWidget(self.labelChar_11)

        self.labelChar_12 = QLabel(Form)
        self.labelChar_12.setObjectName(u"labelChar_12")

        self.horizonCharTest.addWidget(self.labelChar_12)

        self.labelChar_13 = QLabel(Form)
        self.labelChar_13.setObjectName(u"labelChar_13")

        self.horizonCharTest.addWidget(self.labelChar_13)

        self.labelChar_14 = QLabel(Form)
        self.labelChar_14.setObjectName(u"labelChar_14")

        self.horizonCharTest.addWidget(self.labelChar_14)

        self.labelChar_15 = QLabel(Form)
        self.labelChar_15.setObjectName(u"labelChar_15")

        self.horizonCharTest.addWidget(self.labelChar_15)

        self.labelChar_16 = QLabel(Form)
        self.labelChar_16.setObjectName(u"labelChar_16")

        self.horizonCharTest.addWidget(self.labelChar_16)

        self.labelChar_17 = QLabel(Form)
        self.labelChar_17.setObjectName(u"labelChar_17")

        self.horizonCharTest.addWidget(self.labelChar_17)

        self.labelChar_18 = QLabel(Form)
        self.labelChar_18.setObjectName(u"labelChar_18")

        self.horizonCharTest.addWidget(self.labelChar_18)

        self.labelChar_19 = QLabel(Form)
        self.labelChar_19.setObjectName(u"labelChar_19")

        self.horizonCharTest.addWidget(self.labelChar_19)

        self.lineEditTest = QLineEdit(Form)
        self.lineEditTest.setFocus()
        self.lineEditTest.setVisible(False)


        self.verticalLayout.addLayout(self.horizonCharTest)

        self.verticalSpacerLowerTest = QSpacerItem(20, 199, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerLowerTest)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    # retranslateUi

