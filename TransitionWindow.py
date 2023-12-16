# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransitionWindow.ui'
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

class Ui_Trans(object):
    def setupTransUi(self, Trans):
        if not Trans.objectName():
            Trans.setObjectName(u"Trans")
        Trans.resize(775, 498)
        self.verticalLayout = QVBoxLayout(Trans)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labeHeaderTrans = QLabel(Trans)
        self.labeHeaderTrans.setObjectName(u"labeHeaderTrans")
        self.labeHeaderTrans.setMaximumSize(QSize(16777215, 100))
        self.labeHeaderTrans.setStyleSheet(u"font: 57 italic 48pt \"Z003\";")

        self.verticalLayout.addWidget(self.labeHeaderTrans)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelDetailsTrans = QLabel(Trans)
        self.labelDetailsTrans.setObjectName(u"labelDetailsTrans")

        self.horizontalLayout.addWidget(self.labelDetailsTrans)

        self.label_2 = QLabel(Trans)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizonTop = QHBoxLayout()
        self.horizonTop.setObjectName(u"horizonTop")

        self.buttonRestartTrans = QPushButton(Trans, text = 'Restart')
        self.buttonRestartTrans.setObjectName(u"buttonRestartTrans")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRestartTrans.sizePolicy().hasHeightForWidth())
        self.buttonRestartTrans.setSizePolicy(sizePolicy)
        self.buttonRestartTrans.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamilies([u"Z003"])
        font.setPointSize(24)
        font.setItalic(True)
        self.buttonRestartTrans.setFont(font)

        self.horizonTop.addWidget(self.buttonRestartTrans)

        self.buttonContinueTrans = QPushButton(Trans, text = 'Continue')
        self.buttonContinueTrans.setObjectName(u"buttonContinueTrans")
        sizePolicy.setHeightForWidth(self.buttonContinueTrans.sizePolicy().hasHeightForWidth())
        self.buttonContinueTrans.setSizePolicy(sizePolicy)
        self.buttonContinueTrans.setMinimumSize(QSize(200, 200))
        self.buttonContinueTrans.setFont(font)

        self.horizonTop.addWidget(self.buttonContinueTrans)

        self.buttonHomeTrans = QPushButton(Trans, text = 'Home')
        self.buttonHomeTrans.setObjectName(u"buttonHomeTrans")
        sizePolicy.setHeightForWidth(self.buttonHomeTrans.sizePolicy().hasHeightForWidth())
        self.buttonHomeTrans.setSizePolicy(sizePolicy)
        self.buttonHomeTrans.setMinimumSize(QSize(200, 200))
        self.buttonHomeTrans.setFont(font)

        self.horizonTop.addWidget(self.buttonHomeTrans)


        self.verticalLayout.addLayout(self.horizonTop)

        QMetaObject.connectSlotsByName(Trans)
    # setupUi


