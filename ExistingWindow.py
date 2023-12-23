# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ExistingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QMetaObject, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_ExistingWindow(object):
    def setupExUi(self, ExistingWindow):
        if not ExistingWindow.objectName():
            ExistingWindow.setObjectName(u"ExistingWindow")
        ExistingWindow.resize(738, 588)
        self.verticalLayout = QVBoxLayout(ExistingWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHeaderEx = QLabel(ExistingWindow, text='Typing Tutorial')
        self.labelHeaderEx.setObjectName(u"labelHeaderEx")
        self.labelHeaderEx.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout.addWidget(self.labelHeaderEx)

        self.verticalSpacerEx = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerEx)

        self.comboBoxEx = QComboBox(ExistingWindow)
        self.comboBoxEx.setObjectName(u"comboBoxEx")

        self.verticalLayout.addWidget(self.comboBoxEx)

        self.buttonContinueEx = QPushButton(ExistingWindow, text = 'Continue')
        self.buttonContinueEx.setObjectName(u"buttonContinueEx")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonContinueEx.sizePolicy().hasHeightForWidth())
        self.buttonContinueEx.setSizePolicy(sizePolicy)
        self.buttonContinueEx.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setPointSize(24)
        font.setItalic(True)
        self.buttonContinueEx.setFont(font)

        self.verticalLayout.addWidget(self.buttonContinueEx)

        self.horizonBottomEx = QHBoxLayout()
        self.horizonBottomEx.setObjectName(u"horizonBottomEx")
        self.buttonHomeEx = QPushButton(ExistingWindow, text= 'Home')
        self.buttonHomeEx.setObjectName(u"buttonHomeEx")
        sizePolicy.setHeightForWidth(self.buttonHomeEx.sizePolicy().hasHeightForWidth())
        self.buttonHomeEx.setSizePolicy(sizePolicy)
        self.buttonHomeEx.setMinimumSize(QSize(200, 200))
        self.buttonHomeEx.setFont(font)

        self.horizonBottomEx.addWidget(self.buttonHomeEx)

        self.buttonExitEx = QPushButton(ExistingWindow, text = 'Exit')
        self.buttonExitEx.setObjectName(u"buttonExitEx")
        sizePolicy.setHeightForWidth(self.buttonExitEx.sizePolicy().hasHeightForWidth())
        self.buttonExitEx.setSizePolicy(sizePolicy)
        self.buttonExitEx.setMinimumSize(QSize(200, 200))
        self.buttonExitEx.setFont(font)

        self.horizonBottomEx.addWidget(self.buttonExitEx)

        self.verticalLayout.addLayout(self.horizonBottomEx)

        QMetaObject.connectSlotsByName(ExistingWindow)
    # setupUi

