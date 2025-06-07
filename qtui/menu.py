# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)
from qtui import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(330, 318))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"background-color: #C8C8C8;")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(330, 68))
        self.widget.setMaximumSize(QSize(330, 68))
        self.widget.setStyleSheet(u"background-color: #BBB1A7;")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout_3.addWidget(self.widget_4)

        self.Button_Windows = QWidget(self.centralwidget)
        self.Button_Windows.setObjectName(u"Button_Windows")
        self.Button_Windows.setMinimumSize(QSize(285, 65))
        self.Button_Windows.setMaximumSize(QSize(285, 65))
        self.Button_Windows.setStyleSheet(u"background-color: #BBB1A7;")
        self.verticalLayout = QVBoxLayout(self.Button_Windows)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.Button_Windows)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: black")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.Button_Windows, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.Button_MacOS = QWidget(self.centralwidget)
        self.Button_MacOS.setObjectName(u"Button_MacOS")
        self.Button_MacOS.setMinimumSize(QSize(285, 65))
        self.Button_MacOS.setMaximumSize(QSize(285, 65))
        self.Button_MacOS.setStyleSheet(u"background-color: #BBB1A7;")
        self.verticalLayout_2 = QVBoxLayout(self.Button_MacOS)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.Button_MacOS)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: black")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.Button_MacOS, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_3.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u043a\u043b\u0430\u0434\u043a\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MacOS", None))
    # retranslateUi

