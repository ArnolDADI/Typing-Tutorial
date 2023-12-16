# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeWindow.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupHomeUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(788, 624)
        self.verticalLayout = QVBoxLayout(HomeWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labeHeaderHomel = QLabel(HomeWindow)
        self.labeHeaderHomel.setObjectName(u"labeHeaderHomel")
        self.labeHeaderHomel.setMaximumSize(QSize(16777215, 100))
        self.labeHeaderHomel.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout.addWidget(self.labeHeaderHomel)

        self.verticalSpacerHome = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerHome)

        self.horizonTop = QHBoxLayout()
        self.horizonTop.setObjectName(u"horizonTop")
        self.buttonNewHome = QPushButton(HomeWindow)
        self.buttonNewHome.setObjectName(u"buttonNewHome")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewHome.sizePolicy().hasHeightForWidth())
        self.buttonNewHome.setSizePolicy(sizePolicy)
        self.buttonNewHome.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setPointSize(24)
        font.setItalic(True)
        self.buttonNewHome.setFont(font)

        self.horizonTop.addWidget(self.buttonNewHome)

        self.buttonContinueHome = QPushButton(HomeWindow)
        self.buttonContinueHome.setObjectName(u"buttonContinueHome")
        sizePolicy.setHeightForWidth(self.buttonContinueHome.sizePolicy().hasHeightForWidth())
        self.buttonContinueHome.setSizePolicy(sizePolicy)
        self.buttonContinueHome.setMinimumSize(QSize(200, 200))
        self.buttonContinueHome.setFont(font)

        self.horizonTop.addWidget(self.buttonContinueHome)

        self.buttonExisitingHome = QPushButton(HomeWindow)
        self.buttonExisitingHome.setObjectName(u"buttonExisitingHome")
        sizePolicy.setHeightForWidth(self.buttonExisitingHome.sizePolicy().hasHeightForWidth())
        self.buttonExisitingHome.setSizePolicy(sizePolicy)
        self.buttonExisitingHome.setMinimumSize(QSize(200, 200))
        self.buttonExisitingHome.setFont(font)

        self.horizonTop.addWidget(self.buttonExisitingHome)


        self.verticalLayout.addLayout(self.horizonTop)

        self.horizonBottom = QHBoxLayout()
        self.horizonBottom.setObjectName(u"horizonBottom")
        self.buttonSettingsHome = QPushButton(HomeWindow)
        self.buttonSettingsHome.setObjectName(u"buttonSettingsHome")
        sizePolicy.setHeightForWidth(self.buttonSettingsHome.sizePolicy().hasHeightForWidth())
        self.buttonSettingsHome.setSizePolicy(sizePolicy)
        self.buttonSettingsHome.setMinimumSize(QSize(200, 200))
        self.buttonSettingsHome.setFont(font)

        self.horizonBottom.addWidget(self.buttonSettingsHome)

        self.buttonThemHome = QPushButton(HomeWindow)
        self.buttonThemHome.setObjectName(u"buttonThemHome")
        sizePolicy.setHeightForWidth(self.buttonThemHome.sizePolicy().hasHeightForWidth())
        self.buttonThemHome.setSizePolicy(sizePolicy)
        self.buttonThemHome.setMinimumSize(QSize(200, 200))
        self.buttonThemHome.setFont(font)

        self.horizonBottom.addWidget(self.buttonThemHome)

        self.buttonEcitHome = QPushButton(HomeWindow)
        self.buttonEcitHome.setObjectName(u"buttonEcitHome")
        sizePolicy.setHeightForWidth(self.buttonEcitHome.sizePolicy().hasHeightForWidth())
        self.buttonEcitHome.setSizePolicy(sizePolicy)
        self.buttonEcitHome.setMinimumSize(QSize(200, 200))
        self.buttonEcitHome.setFont(font)

        self.horizonBottom.addWidget(self.buttonEcitHome)


        self.verticalLayout.addLayout(self.horizonBottom)


        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"Form", None))
        self.labeHeaderHomel.setText(QCoreApplication.translate("HomeWindow", u"Typing Tutorial", None))
        self.buttonNewHome.setText(QCoreApplication.translate("HomeWindow", u"Create New Profile", None))
        self.buttonContinueHome.setText(QCoreApplication.translate("HomeWindow", u"Continue", None))
        self.buttonExisitingHome.setText(QCoreApplication.translate("HomeWindow", u"Select existing", None))
        self.buttonSettingsHome.setText(QCoreApplication.translate("HomeWindow", u"Settings", None))
        self.buttonThemHome.setText(QCoreApplication.translate("HomeWindow", u"Toggle Theme", None))
        self.buttonEcitHome.setText(QCoreApplication.translate("HomeWindow", u"Exit", None))
    # retranslateUi

