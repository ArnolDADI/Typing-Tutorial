# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProfileWindow(object):
    def setupProfileUi(self, ProfileWindow):
        if not ProfileWindow.objectName():
            ProfileWindow.setObjectName(u"ProfileWindow")
        ProfileWindow.resize(824, 598)
        self.verticalLayout_2 = QVBoxLayout(ProfileWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelWelcomeProfile = QLabel(ProfileWindow)
        self.labelWelcomeProfile.setObjectName(u"labelWelcomeProfile")
        self.labelWelcomeProfile.setMaximumSize(QSize(16777215, 100))
        self.labelWelcomeProfile.move(100,10)
        self.labelWelcomeProfile.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout_2.addWidget(self.labelWelcomeProfile)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ProfileWindow, text = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12")
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonContinueProfile = QPushButton(ProfileWindow, text = 'Continue')
        self.buttonContinueProfile.setObjectName(u"buttonContinueProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonContinueProfile.sizePolicy().hasHeightForWidth())
        self.buttonContinueProfile.setSizePolicy(sizePolicy)
        self.buttonContinueProfile.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setPointSize(24)
        font.setItalic(True)
        self.buttonContinueProfile.setFont(font)

        self.verticalLayout.addWidget(self.buttonContinueProfile)

        self.buttonInfoProfile = QPushButton(ProfileWindow, text = 'Details')
        self.buttonInfoProfile.setObjectName(u"buttonInfoProfile")
        sizePolicy.setHeightForWidth(self.buttonInfoProfile.sizePolicy().hasHeightForWidth())
        self.buttonInfoProfile.setSizePolicy(sizePolicy)
        self.buttonInfoProfile.setMinimumSize(QSize(200, 200))
        self.buttonInfoProfile.setFont(font)

        self.verticalLayout.addWidget(self.buttonInfoProfile)

        self.buttonExitProfile = QPushButton(ProfileWindow,text = 'Exit')
        self.buttonExitProfile.setObjectName(u"buttonExitProfile")
        sizePolicy.setHeightForWidth(self.buttonExitProfile.sizePolicy().hasHeightForWidth())
        self.buttonExitProfile.setSizePolicy(sizePolicy)
        self.buttonExitProfile.setMinimumSize(QSize(200, 200))
        self.buttonExitProfile.setFont(font)

        self.verticalLayout.addWidget(self.buttonExitProfile)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        QMetaObject.connectSlotsByName(ProfileWindow)
    # setupUi
