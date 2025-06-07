# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from qtui import res_rc

class Ui_MainWindowK2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #C8C8C8")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 600))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"background-color: #C8C8C8")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.button_container = QWidget(self.centralwidget)
        self.button_container.setObjectName(u"button_container")
        self.button_container.setStyleSheet(u"border: none")
        self.horizontalLayout_7 = QHBoxLayout(self.button_container)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Button_keyboard = QPushButton(self.button_container)
        self.Button_keyboard.setObjectName(u"Button_keyboard")
        self.Button_keyboard.setMinimumSize(QSize(40, 30))
        self.Button_keyboard.setMaximumSize(QSize(40, 30))
        self.Button_keyboard.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_keyboard.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/keyboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_keyboard.setIcon(icon)
        self.Button_keyboard.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Button_keyboard)

        self.Button_reset = QPushButton(self.button_container)
        self.Button_reset.setObjectName(u"Button_reset")
        self.Button_reset.setMinimumSize(QSize(30, 30))
        self.Button_reset.setMaximumSize(QSize(40, 16777215))
        self.Button_reset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_reset.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/rotate-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_reset.setIcon(icon1)
        self.Button_reset.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Button_reset)


        self.verticalLayout_3.addWidget(self.button_container, 0, Qt.AlignmentFlag.AlignRight)

        self.keyboard_container = QWidget(self.centralwidget)
        self.keyboard_container.setObjectName(u"keyboard_container")
        self.keyboard_container.setStyleSheet(u"border: 0px solid black")
        self.verticalLayout = QVBoxLayout(self.keyboard_container)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, -1, 30, -1)
        self.widget = QWidget(self.keyboard_container)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.widget)

        self.keyboard = QWidget(self.keyboard_container)
        self.keyboard.setObjectName(u"keyboard")
        self.keyboard.setMinimumSize(QSize(900, 300))
        self.keyboard.setMaximumSize(QSize(900, 400))
        self.keyboard.setStyleSheet(u"background-color: #BBB1A7; border: none; border-radius: 20px")
        self.verticalLayout_4 = QVBoxLayout(self.keyboard)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 30, 6, 6)
        self.horizontalWidget = QWidget(self.keyboard)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setStyleSheet(u"border-radius: 0 px;")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.key_Esc = QWidget(self.horizontalWidget)
        self.key_Esc.setObjectName(u"key_Esc")
        self.key_Esc.setMinimumSize(QSize(42, 42))
        self.key_Esc.setMaximumSize(QSize(42, 42))
        self.key_Esc.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_77 = QGridLayout(self.key_Esc)
        self.gridLayout_77.setSpacing(0)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_77.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.key_Esc)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_77.addWidget(self.label_172, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_Esc)

        self.key_f1 = QWidget(self.horizontalWidget)
        self.key_f1.setObjectName(u"key_f1")
        self.key_f1.setMinimumSize(QSize(42, 42))
        self.key_f1.setMaximumSize(QSize(42, 42))
        self.key_f1.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.key_f1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_160 = QLabel(self.key_f1)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMaximumSize(QSize(13, 13))
        self.label_160.setStyleSheet(u"border: none;  background: transparent")
        self.label_160.setPixmap(QPixmap(u":/newPrefix/sun-dim.svg"))
        self.label_160.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_160, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_159 = QLabel(self.key_f1)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setStyleSheet(u"border: none;  background: transparent")
        self.label_159.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_159, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_4.addWidget(self.key_f1)

        self.key_f2 = QWidget(self.horizontalWidget)
        self.key_f2.setObjectName(u"key_f2")
        self.key_f2.setMinimumSize(QSize(42, 42))
        self.key_f2.setMaximumSize(QSize(42, 42))
        self.key_f2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.key_f2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_223 = QLabel(self.key_f2)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setMaximumSize(QSize(20, 20))
        self.label_223.setStyleSheet(u"border: none;  background: transparent")
        self.label_223.setPixmap(QPixmap(u":/newPrefix/sun.svg"))
        self.label_223.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_223, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_173 = QLabel(self.key_f2)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_5.addWidget(self.label_173)


        self.horizontalLayout_4.addWidget(self.key_f2)

        self.key_f3 = QWidget(self.horizontalWidget)
        self.key_f3.setObjectName(u"key_f3")
        self.key_f3.setMinimumSize(QSize(42, 42))
        self.key_f3.setMaximumSize(QSize(42, 42))
        self.key_f3.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.key_f3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_224 = QLabel(self.key_f3)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMaximumSize(QSize(20, 20))
        self.label_224.setStyleSheet(u"border: none;  background: transparent")
        self.label_224.setPixmap(QPixmap(u":/newPrefix/layout-dashboard.svg"))
        self.label_224.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_224, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_174 = QLabel(self.key_f3)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_6.addWidget(self.label_174)


        self.horizontalLayout_4.addWidget(self.key_f3)

        self.key_f4 = QWidget(self.horizontalWidget)
        self.key_f4.setObjectName(u"key_f4")
        self.key_f4.setMinimumSize(QSize(42, 42))
        self.key_f4.setMaximumSize(QSize(42, 42))
        self.key_f4.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.key_f4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_225 = QLabel(self.key_f4)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setMaximumSize(QSize(20, 20))
        self.label_225.setStyleSheet(u"border: none;  background: transparent")
        self.label_225.setPixmap(QPixmap(u":/newPrefix/grip-horizontal.svg"))
        self.label_225.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_225, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_175 = QLabel(self.key_f4)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_7.addWidget(self.label_175)


        self.horizontalLayout_4.addWidget(self.key_f4)

        self.key_f5 = QWidget(self.horizontalWidget)
        self.key_f5.setObjectName(u"key_f5")
        self.key_f5.setMinimumSize(QSize(42, 42))
        self.key_f5.setMaximumSize(QSize(42, 42))
        self.key_f5.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.key_f5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_176 = QLabel(self.key_f5)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_8.addWidget(self.label_176, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_4.addWidget(self.key_f5)

        self.key_f6 = QWidget(self.horizontalWidget)
        self.key_f6.setObjectName(u"key_f6")
        self.key_f6.setMinimumSize(QSize(42, 42))
        self.key_f6.setMaximumSize(QSize(42, 42))
        self.key_f6.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.key_f6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.label_177 = QLabel(self.key_f6)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_9.addWidget(self.label_177, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_4.addWidget(self.key_f6)

        self.key_f7 = QWidget(self.horizontalWidget)
        self.key_f7.setObjectName(u"key_f7")
        self.key_f7.setMinimumSize(QSize(42, 42))
        self.key_f7.setMaximumSize(QSize(42, 42))
        self.key_f7.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.key_f7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_226 = QLabel(self.key_f7)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setMaximumSize(QSize(20, 20))
        self.label_226.setStyleSheet(u"border: none;  background: transparent")
        self.label_226.setPixmap(QPixmap(u":/newPrefix/rewind.svg"))
        self.label_226.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_226, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_178 = QLabel(self.key_f7)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_10.addWidget(self.label_178)


        self.horizontalLayout_4.addWidget(self.key_f7)

        self.key_f8 = QWidget(self.horizontalWidget)
        self.key_f8.setObjectName(u"key_f8")
        self.key_f8.setMinimumSize(QSize(42, 42))
        self.key_f8.setMaximumSize(QSize(42, 42))
        self.key_f8.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.key_f8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.label_227 = QLabel(self.key_f8)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setMaximumSize(QSize(20, 20))
        self.label_227.setStyleSheet(u"border: none;  background: transparent")
        self.label_227.setPixmap(QPixmap(u":/newPrefix/pause.svg"))
        self.label_227.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_227, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_179 = QLabel(self.key_f8)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_11.addWidget(self.label_179)


        self.horizontalLayout_4.addWidget(self.key_f8)

        self.key_f9 = QWidget(self.horizontalWidget)
        self.key_f9.setObjectName(u"key_f9")
        self.key_f9.setMinimumSize(QSize(42, 42))
        self.key_f9.setMaximumSize(QSize(42, 42))
        self.key_f9.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.key_f9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.label_228 = QLabel(self.key_f9)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setMaximumSize(QSize(20, 20))
        self.label_228.setStyleSheet(u"border: none;  background: transparent")
        self.label_228.setPixmap(QPixmap(u":/newPrefix/fast-forward.svg"))
        self.label_228.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_228, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_180 = QLabel(self.key_f9)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_12.addWidget(self.label_180)


        self.horizontalLayout_4.addWidget(self.key_f9)

        self.key_f10 = QWidget(self.horizontalWidget)
        self.key_f10.setObjectName(u"key_f10")
        self.key_f10.setMinimumSize(QSize(42, 42))
        self.key_f10.setMaximumSize(QSize(42, 42))
        self.key_f10.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.key_f10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_229 = QLabel(self.key_f10)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setMaximumSize(QSize(20, 20))
        self.label_229.setStyleSheet(u"border: none;  background: transparent")
        self.label_229.setPixmap(QPixmap(u":/newPrefix/volume.svg"))
        self.label_229.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_229, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_181 = QLabel(self.key_f10)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_13.addWidget(self.label_181)


        self.horizontalLayout_4.addWidget(self.key_f10)

        self.key_f10_2 = QWidget(self.horizontalWidget)
        self.key_f10_2.setObjectName(u"key_f10_2")
        self.key_f10_2.setMinimumSize(QSize(42, 42))
        self.key_f10_2.setMaximumSize(QSize(42, 42))
        self.key_f10_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.key_f10_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.label_230 = QLabel(self.key_f10_2)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setMaximumSize(QSize(20, 20))
        self.label_230.setStyleSheet(u"border: none;  background: transparent")
        self.label_230.setPixmap(QPixmap(u":/newPrefix/volume-1.svg"))
        self.label_230.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_230, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_182 = QLabel(self.key_f10_2)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_14.addWidget(self.label_182)


        self.horizontalLayout_4.addWidget(self.key_f10_2)

        self.key_f12 = QWidget(self.horizontalWidget)
        self.key_f12.setObjectName(u"key_f12")
        self.key_f12.setMinimumSize(QSize(42, 42))
        self.key_f12.setMaximumSize(QSize(42, 42))
        self.key_f12.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.key_f12)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_231 = QLabel(self.key_f12)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setMaximumSize(QSize(20, 20))
        self.label_231.setStyleSheet(u"border: none;  background: transparent")
        self.label_231.setPixmap(QPixmap(u":/newPrefix/volume-2.svg"))
        self.label_231.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_231, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_183 = QLabel(self.key_f12)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_15.addWidget(self.label_183)


        self.horizontalLayout_4.addWidget(self.key_f12)

        self.key_Backspace = QWidget(self.horizontalWidget)
        self.key_Backspace.setObjectName(u"key_Backspace")
        self.key_Backspace.setMinimumSize(QSize(48, 42))
        self.key_Backspace.setMaximumSize(QSize(48, 42))
        self.key_Backspace.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_105 = QGridLayout(self.key_Backspace)
        self.gridLayout_105.setSpacing(0)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.gridLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_214 = QLabel(self.key_Backspace)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setStyleSheet(u"border: none;  background: transparent")
        self.label_214.setPixmap(QPixmap(u":/newPrefix/arrow-big-up-dash.svg"))

        self.gridLayout_105.addWidget(self.label_214, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.key_Backspace)

        self.key_f13 = QWidget(self.horizontalWidget)
        self.key_f13.setObjectName(u"key_f13")
        self.key_f13.setMinimumSize(QSize(42, 42))
        self.key_f13.setMaximumSize(QSize(42, 42))
        self.key_f13.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_90 = QGridLayout(self.key_f13)
        self.gridLayout_90.setSpacing(0)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_195 = QLabel(self.key_f13)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_90.addWidget(self.label_195, 2, 0, 1, 2)

        self.label_196 = QLabel(self.key_f13)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_90.addWidget(self.label_196, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f13)

        self.key_f14 = QWidget(self.horizontalWidget)
        self.key_f14.setObjectName(u"key_f14")
        self.key_f14.setMinimumSize(QSize(42, 42))
        self.key_f14.setMaximumSize(QSize(42, 42))
        self.key_f14.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_91 = QGridLayout(self.key_f14)
        self.gridLayout_91.setSpacing(0)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_197 = QLabel(self.key_f14)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_91.addWidget(self.label_197, 2, 0, 1, 2)

        self.label_208 = QLabel(self.key_f14)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_91.addWidget(self.label_208, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f14)

        self.key_f15 = QWidget(self.horizontalWidget)
        self.key_f15.setObjectName(u"key_f15")
        self.key_f15.setMinimumSize(QSize(42, 42))
        self.key_f15.setMaximumSize(QSize(42, 42))
        self.key_f15.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_92 = QGridLayout(self.key_f15)
        self.gridLayout_92.setSpacing(0)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_211 = QLabel(self.key_f15)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_92.addWidget(self.label_211, 2, 0, 1, 2)

        self.label_212 = QLabel(self.key_f15)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_92.addWidget(self.label_212, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f15)

        self.key_f16 = QWidget(self.horizontalWidget)
        self.key_f16.setObjectName(u"key_f16")
        self.key_f16.setMinimumSize(QSize(42, 42))
        self.key_f16.setMaximumSize(QSize(42, 42))
        self.key_f16.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_106 = QGridLayout(self.key_f16)
        self.gridLayout_106.setSpacing(0)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.gridLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_213 = QLabel(self.key_f16)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_106.addWidget(self.label_213, 2, 0, 1, 2)

        self.label_215 = QLabel(self.key_f16)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_106.addWidget(self.label_215, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f16)

        self.key_f17 = QWidget(self.horizontalWidget)
        self.key_f17.setObjectName(u"key_f17")
        self.key_f17.setMinimumSize(QSize(42, 42))
        self.key_f17.setMaximumSize(QSize(42, 42))
        self.key_f17.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_107 = QGridLayout(self.key_f17)
        self.gridLayout_107.setSpacing(0)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.gridLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_216 = QLabel(self.key_f17)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_107.addWidget(self.label_216, 2, 0, 1, 2)

        self.label_217 = QLabel(self.key_f17)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_107.addWidget(self.label_217, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f17)

        self.key_f18 = QWidget(self.horizontalWidget)
        self.key_f18.setObjectName(u"key_f18")
        self.key_f18.setMinimumSize(QSize(42, 42))
        self.key_f18.setMaximumSize(QSize(42, 42))
        self.key_f18.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_108 = QGridLayout(self.key_f18)
        self.gridLayout_108.setSpacing(0)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.gridLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_218 = QLabel(self.key_f18)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_108.addWidget(self.label_218, 2, 0, 1, 2)

        self.label_219 = QLabel(self.key_f18)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_108.addWidget(self.label_219, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f18)

        self.key_f16_2 = QWidget(self.horizontalWidget)
        self.key_f16_2.setObjectName(u"key_f16_2")
        self.key_f16_2.setMinimumSize(QSize(42, 42))
        self.key_f16_2.setMaximumSize(QSize(42, 42))
        self.key_f16_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_109 = QGridLayout(self.key_f16_2)
        self.gridLayout_109.setSpacing(0)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.gridLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_220 = QLabel(self.key_f16_2)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_109.addWidget(self.label_220, 2, 0, 1, 2)

        self.label_221 = QLabel(self.key_f16_2)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_109.addWidget(self.label_221, 3, 2, 1, 1)


        self.horizontalLayout_4.addWidget(self.key_f16_2)


        self.verticalLayout_4.addWidget(self.horizontalWidget)

        self.horizontalWidget_2 = QWidget(self.keyboard)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.key_tilda = QWidget(self.horizontalWidget_2)
        self.key_tilda.setObjectName(u"key_tilda")
        self.key_tilda.setMinimumSize(QSize(42, 42))
        self.key_tilda.setMaximumSize(QSize(42, 42))
        self.key_tilda.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_21 = QGridLayout(self.key_tilda)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.key_tilda)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_21.addWidget(self.label_22, 3, 2, 1, 1)

        self.label_26 = QLabel(self.key_tilda)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_21.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_30 = QLabel(self.key_tilda)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_21.addWidget(self.label_30, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_tilda)

        self.key_t_1 = QWidget(self.horizontalWidget_2)
        self.key_t_1.setObjectName(u"key_t_1")
        self.key_t_1.setMinimumSize(QSize(42, 42))
        self.key_t_1.setMaximumSize(QSize(42, 42))
        self.key_t_1.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_22 = QGridLayout(self.key_t_1)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.key_t_1)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_22.addWidget(self.label_38, 3, 0, 1, 1)

        self.label_50 = QLabel(self.key_t_1)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_22.addWidget(self.label_50, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_1)

        self.key_t_2 = QWidget(self.horizontalWidget_2)
        self.key_t_2.setObjectName(u"key_t_2")
        self.key_t_2.setMinimumSize(QSize(42, 42))
        self.key_t_2.setMaximumSize(QSize(42, 42))
        self.key_t_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_23 = QGridLayout(self.key_t_2)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.key_t_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_23.addWidget(self.label_59, 3, 2, 1, 1)

        self.label_60 = QLabel(self.key_t_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_23.addWidget(self.label_60, 3, 0, 1, 1)

        self.label_61 = QLabel(self.key_t_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_23.addWidget(self.label_61, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_2)

        self.key_t_3 = QWidget(self.horizontalWidget_2)
        self.key_t_3.setObjectName(u"key_t_3")
        self.key_t_3.setMinimumSize(QSize(42, 42))
        self.key_t_3.setMaximumSize(QSize(42, 42))
        self.key_t_3.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_24 = QGridLayout(self.key_t_3)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.key_t_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_24.addWidget(self.label_62, 3, 2, 1, 1)

        self.label_63 = QLabel(self.key_t_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_24.addWidget(self.label_63, 3, 0, 1, 1)

        self.label_64 = QLabel(self.key_t_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_24.addWidget(self.label_64, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_3)

        self.key_t_4 = QWidget(self.horizontalWidget_2)
        self.key_t_4.setObjectName(u"key_t_4")
        self.key_t_4.setMinimumSize(QSize(42, 42))
        self.key_t_4.setMaximumSize(QSize(42, 42))
        self.key_t_4.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_25 = QGridLayout(self.key_t_4)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.key_t_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_25.addWidget(self.label_65, 3, 2, 1, 1)

        self.label_66 = QLabel(self.key_t_4)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_25.addWidget(self.label_66, 3, 0, 1, 1)

        self.label_67 = QLabel(self.key_t_4)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_25.addWidget(self.label_67, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_4)

        self.key_t_5 = QWidget(self.horizontalWidget_2)
        self.key_t_5.setObjectName(u"key_t_5")
        self.key_t_5.setMinimumSize(QSize(42, 42))
        self.key_t_5.setMaximumSize(QSize(42, 42))
        self.key_t_5.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_26 = QGridLayout(self.key_t_5)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.key_t_5)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_26.addWidget(self.label_69, 3, 0, 1, 1)

        self.label_70 = QLabel(self.key_t_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_26.addWidget(self.label_70, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_5)

        self.key_t_6 = QWidget(self.horizontalWidget_2)
        self.key_t_6.setObjectName(u"key_t_6")
        self.key_t_6.setMinimumSize(QSize(42, 42))
        self.key_t_6.setMaximumSize(QSize(42, 42))
        self.key_t_6.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_27 = QGridLayout(self.key_t_6)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.key_t_6)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_27.addWidget(self.label_71, 3, 2, 1, 1)

        self.label_72 = QLabel(self.key_t_6)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_27.addWidget(self.label_72, 3, 0, 1, 1)

        self.label_73 = QLabel(self.key_t_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_27.addWidget(self.label_73, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_6)

        self.key_t_7 = QWidget(self.horizontalWidget_2)
        self.key_t_7.setObjectName(u"key_t_7")
        self.key_t_7.setMinimumSize(QSize(42, 42))
        self.key_t_7.setMaximumSize(QSize(42, 42))
        self.key_t_7.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_28 = QGridLayout(self.key_t_7)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.key_t_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_28.addWidget(self.label_74, 3, 2, 1, 1)

        self.label_75 = QLabel(self.key_t_7)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_28.addWidget(self.label_75, 3, 0, 1, 1)

        self.label_76 = QLabel(self.key_t_7)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_28.addWidget(self.label_76, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_7)

        self.key_t_8 = QWidget(self.horizontalWidget_2)
        self.key_t_8.setObjectName(u"key_t_8")
        self.key_t_8.setMinimumSize(QSize(42, 42))
        self.key_t_8.setMaximumSize(QSize(42, 42))
        self.key_t_8.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_29 = QGridLayout(self.key_t_8)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.key_t_8)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_29.addWidget(self.label_78, 3, 0, 1, 1)

        self.label_79 = QLabel(self.key_t_8)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_29.addWidget(self.label_79, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_8)

        self.key_t_9 = QWidget(self.horizontalWidget_2)
        self.key_t_9.setObjectName(u"key_t_9")
        self.key_t_9.setMinimumSize(QSize(42, 42))
        self.key_t_9.setMaximumSize(QSize(42, 42))
        self.key_t_9.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_30 = QGridLayout(self.key_t_9)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.key_t_9)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_30.addWidget(self.label_80, 3, 0, 1, 1)

        self.label_81 = QLabel(self.key_t_9)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_30.addWidget(self.label_81, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_9)

        self.key_t_0 = QWidget(self.horizontalWidget_2)
        self.key_t_0.setObjectName(u"key_t_0")
        self.key_t_0.setMinimumSize(QSize(42, 42))
        self.key_t_0.setMaximumSize(QSize(42, 42))
        self.key_t_0.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_31 = QGridLayout(self.key_t_0)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.key_t_0)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_31.addWidget(self.label_83, 2, 0, 1, 1)

        self.label_82 = QLabel(self.key_t_0)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_31.addWidget(self.label_82, 3, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_t_0)

        self.key_underscore = QWidget(self.horizontalWidget_2)
        self.key_underscore.setObjectName(u"key_underscore")
        self.key_underscore.setMinimumSize(QSize(42, 42))
        self.key_underscore.setMaximumSize(QSize(42, 42))
        self.key_underscore.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_32 = QGridLayout(self.key_underscore)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.key_underscore)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_32.addWidget(self.label_84, 3, 0, 1, 1)

        self.label_85 = QLabel(self.key_underscore)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_32.addWidget(self.label_85, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_underscore)

        self.key_plus = QWidget(self.horizontalWidget_2)
        self.key_plus.setObjectName(u"key_plus")
        self.key_plus.setMinimumSize(QSize(42, 42))
        self.key_plus.setMaximumSize(QSize(42, 42))
        self.key_plus.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_33 = QGridLayout(self.key_plus)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.key_plus)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_33.addWidget(self.label_87, 2, 0, 1, 1)

        self.label_86 = QLabel(self.key_plus)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_33.addWidget(self.label_86, 3, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_plus)

        self.key_Delete_2 = QWidget(self.horizontalWidget_2)
        self.key_Delete_2.setObjectName(u"key_Delete_2")
        self.key_Delete_2.setMinimumSize(QSize(48, 42))
        self.key_Delete_2.setMaximumSize(QSize(48, 42))
        self.key_Delete_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_104 = QGridLayout(self.key_Delete_2)
        self.gridLayout_104.setSpacing(0)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gridLayout_104.setContentsMargins(0, 0, 0, 0)
        self.label_166 = QLabel(self.key_Delete_2)
        self.label_166.setObjectName(u"label_166")

        self.gridLayout_104.addWidget(self.label_166, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_Delete_2)

        self.key_Fn = QWidget(self.horizontalWidget_2)
        self.key_Fn.setObjectName(u"key_Fn")
        self.key_Fn.setMinimumSize(QSize(42, 42))
        self.key_Fn.setMaximumSize(QSize(42, 42))
        self.key_Fn.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_93 = QGridLayout(self.key_Fn)
        self.gridLayout_93.setSpacing(0)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_198 = QLabel(self.key_Fn)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_93.addWidget(self.label_198, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_Fn)

        self.key_Home = QWidget(self.horizontalWidget_2)
        self.key_Home.setObjectName(u"key_Home")
        self.key_Home.setMinimumSize(QSize(42, 42))
        self.key_Home.setMaximumSize(QSize(42, 42))
        self.key_Home.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_94 = QGridLayout(self.key_Home)
        self.gridLayout_94.setSpacing(0)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.gridLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_199 = QLabel(self.key_Home)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_94.addWidget(self.label_199, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_Home)

        self.key_PageUp = QWidget(self.horizontalWidget_2)
        self.key_PageUp.setObjectName(u"key_PageUp")
        self.key_PageUp.setMinimumSize(QSize(42, 42))
        self.key_PageUp.setMaximumSize(QSize(42, 42))
        self.key_PageUp.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_16 = QGridLayout(self.key_PageUp)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 5, 5, 5)
        self.label_53 = QLabel(self.key_PageUp)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"border: none; background: transparent")
        self.label_53.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_53, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_PageUp)

        self.key_Clear = QWidget(self.horizontalWidget_2)
        self.key_Clear.setObjectName(u"key_Clear")
        self.key_Clear.setMinimumSize(QSize(42, 42))
        self.key_Clear.setMaximumSize(QSize(42, 42))
        self.key_Clear.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_96 = QGridLayout(self.key_Clear)
        self.gridLayout_96.setSpacing(0)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.gridLayout_96.setContentsMargins(5, 5, 5, 5)
        self.label_201 = QLabel(self.key_Clear)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setStyleSheet(u"border: none; background: transparent")
        self.label_201.setWordWrap(True)

        self.gridLayout_96.addWidget(self.label_201, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.key_Clear)

        self.key_equal = QWidget(self.horizontalWidget_2)
        self.key_equal.setObjectName(u"key_equal")
        self.key_equal.setMinimumSize(QSize(42, 42))
        self.key_equal.setMaximumSize(QSize(42, 42))
        self.key_equal.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_110 = QGridLayout(self.key_equal)
        self.gridLayout_110.setSpacing(0)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_222 = QLabel(self.key_equal)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_110.addWidget(self.label_222, 2, 0, 1, 2)


        self.horizontalLayout_5.addWidget(self.key_equal)

        self.widget_7 = QWidget(self.horizontalWidget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.widget_7)

        self.key_division = QWidget(self.horizontalWidget_2)
        self.key_division.setObjectName(u"key_division")
        self.key_division.setMinimumSize(QSize(42, 42))
        self.key_division.setMaximumSize(QSize(42, 42))
        self.key_division.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_97 = QGridLayout(self.key_division)
        self.gridLayout_97.setSpacing(0)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_202 = QLabel(self.key_division)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_97.addWidget(self.label_202, 2, 0, 1, 2)


        self.horizontalLayout_5.addWidget(self.key_division)


        self.verticalLayout_4.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_3 = QWidget(self.keyboard)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setStyleSheet(u"border-radius: 0px;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.key_Tab = QWidget(self.horizontalWidget_3)
        self.key_Tab.setObjectName(u"key_Tab")
        self.key_Tab.setMinimumSize(QSize(0, 42))
        self.key_Tab.setMaximumSize(QSize(16777215, 42))
        self.key_Tab.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_18 = QGridLayout(self.key_Tab)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.key_Tab)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_18.addWidget(self.label_58, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_Tab)

        self.key_Q = QWidget(self.horizontalWidget_3)
        self.key_Q.setObjectName(u"key_Q")
        self.key_Q.setMinimumSize(QSize(42, 42))
        self.key_Q.setMaximumSize(QSize(42, 42))
        self.key_Q.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_2 = QGridLayout(self.key_Q)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.key_Q)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_2.addWidget(self.label_5, 3, 2, 1, 1)

        self.label_7 = QLabel(self.key_Q)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_8 = QLabel(self.key_Q)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_Q)

        self.key_W = QWidget(self.horizontalWidget_3)
        self.key_W.setObjectName(u"key_W")
        self.key_W.setMinimumSize(QSize(42, 42))
        self.key_W.setMaximumSize(QSize(42, 42))
        self.key_W.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_12 = QGridLayout(self.key_W)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.key_W)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_12.addWidget(self.label_45, 3, 2, 1, 1)

        self.label_47 = QLabel(self.key_W)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_12.addWidget(self.label_47, 3, 0, 1, 1)

        self.label_48 = QLabel(self.key_W)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_12.addWidget(self.label_48, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_W)

        self.key_E = QWidget(self.horizontalWidget_3)
        self.key_E.setObjectName(u"key_E")
        self.key_E.setMinimumSize(QSize(42, 42))
        self.key_E.setMaximumSize(QSize(42, 42))
        self.key_E.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_4 = QGridLayout(self.key_E)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.key_E)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_4.addWidget(self.label_13, 3, 2, 1, 1)

        self.label_15 = QLabel(self.key_E)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_16 = QLabel(self.key_E)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_E)

        self.key_R = QWidget(self.horizontalWidget_3)
        self.key_R.setObjectName(u"key_R")
        self.key_R.setMinimumSize(QSize(42, 42))
        self.key_R.setMaximumSize(QSize(42, 42))
        self.key_R.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_5 = QGridLayout(self.key_R)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.key_R)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_5.addWidget(self.label_17, 3, 2, 1, 1)

        self.label_19 = QLabel(self.key_R)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_5.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_20 = QLabel(self.key_R)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_5.addWidget(self.label_20, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_R)

        self.key_T = QWidget(self.horizontalWidget_3)
        self.key_T.setObjectName(u"key_T")
        self.key_T.setMinimumSize(QSize(42, 42))
        self.key_T.setMaximumSize(QSize(42, 42))
        self.key_T.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_7 = QGridLayout(self.key_T)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.key_T)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_7.addWidget(self.label_25, 3, 2, 1, 1)

        self.label_27 = QLabel(self.key_T)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_7.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_28 = QLabel(self.key_T)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_7.addWidget(self.label_28, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_T)

        self.key_Y = QWidget(self.horizontalWidget_3)
        self.key_Y.setObjectName(u"key_Y")
        self.key_Y.setMinimumSize(QSize(42, 42))
        self.key_Y.setMaximumSize(QSize(42, 42))
        self.key_Y.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_6 = QGridLayout(self.key_Y)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.key_Y)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_6.addWidget(self.label_21, 3, 2, 1, 1)

        self.label_23 = QLabel(self.key_Y)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_6.addWidget(self.label_23, 3, 0, 1, 1)

        self.label_24 = QLabel(self.key_Y)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_6.addWidget(self.label_24, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_Y)

        self.key_U = QWidget(self.horizontalWidget_3)
        self.key_U.setObjectName(u"key_U")
        self.key_U.setMinimumSize(QSize(42, 42))
        self.key_U.setMaximumSize(QSize(42, 42))
        self.key_U.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_3 = QGridLayout(self.key_U)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.key_U)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_3.addWidget(self.label_9, 3, 2, 1, 1)

        self.label_12 = QLabel(self.key_U)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_11 = QLabel(self.key_U)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_U)

        self.key_I = QWidget(self.horizontalWidget_3)
        self.key_I.setObjectName(u"key_I")
        self.key_I.setMinimumSize(QSize(42, 42))
        self.key_I.setMaximumSize(QSize(42, 42))
        self.key_I.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout = QGridLayout(self.key_I)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.key_I)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.key_I)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_4 = QLabel(self.key_I)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_I)

        self.key_O = QWidget(self.horizontalWidget_3)
        self.key_O.setObjectName(u"key_O")
        self.key_O.setMinimumSize(QSize(42, 42))
        self.key_O.setMaximumSize(QSize(42, 42))
        self.key_O.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_8 = QGridLayout(self.key_O)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.key_O)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_8.addWidget(self.label_29, 3, 2, 1, 1)

        self.label_31 = QLabel(self.key_O)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_8.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.key_O)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_8.addWidget(self.label_32, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_O)

        self.key_P = QWidget(self.horizontalWidget_3)
        self.key_P.setObjectName(u"key_P")
        self.key_P.setMinimumSize(QSize(42, 42))
        self.key_P.setMaximumSize(QSize(42, 42))
        self.key_P.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_9 = QGridLayout(self.key_P)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.key_P)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_9.addWidget(self.label_36, 2, 0, 1, 1)

        self.label_35 = QLabel(self.key_P)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_9.addWidget(self.label_35, 3, 0, 1, 1)

        self.label_33 = QLabel(self.key_P)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_9.addWidget(self.label_33, 3, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_P)

        self.key_l_bracket = QWidget(self.horizontalWidget_3)
        self.key_l_bracket.setObjectName(u"key_l_bracket")
        self.key_l_bracket.setMinimumSize(QSize(42, 42))
        self.key_l_bracket.setMaximumSize(QSize(42, 42))
        self.key_l_bracket.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_10 = QGridLayout(self.key_l_bracket)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.key_l_bracket)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_10.addWidget(self.label_37, 3, 2, 1, 1)

        self.label_39 = QLabel(self.key_l_bracket)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_10.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_40 = QLabel(self.key_l_bracket)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_10.addWidget(self.label_40, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_l_bracket)

        self.key_R_bracket = QWidget(self.horizontalWidget_3)
        self.key_R_bracket.setObjectName(u"key_R_bracket")
        self.key_R_bracket.setMinimumSize(QSize(42, 42))
        self.key_R_bracket.setMaximumSize(QSize(42, 42))
        self.key_R_bracket.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_11 = QGridLayout(self.key_R_bracket)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.key_R_bracket)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_11.addWidget(self.label_41, 3, 2, 1, 1)

        self.label_44 = QLabel(self.key_R_bracket)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_11.addWidget(self.label_44, 2, 0, 1, 1)

        self.label_43 = QLabel(self.key_R_bracket)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_11.addWidget(self.label_43, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_R_bracket)

        self.key_backslash = QWidget(self.horizontalWidget_3)
        self.key_backslash.setObjectName(u"key_backslash")
        self.key_backslash.setMinimumSize(QSize(42, 42))
        self.key_backslash.setMaximumSize(QSize(42, 42))
        self.key_backslash.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_13 = QGridLayout(self.key_backslash)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.key_backslash)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_13.addWidget(self.label_52, 2, 2, 1, 1)

        self.label_49 = QLabel(self.key_backslash)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_13.addWidget(self.label_49, 3, 2, 1, 1)

        self.label_51 = QLabel(self.key_backslash)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_13.addWidget(self.label_51, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_backslash)

        self.key_Delete = QWidget(self.horizontalWidget_3)
        self.key_Delete.setObjectName(u"key_Delete")
        self.key_Delete.setMinimumSize(QSize(42, 42))
        self.key_Delete.setMaximumSize(QSize(42, 42))
        self.key_Delete.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_14 = QGridLayout(self.key_Delete)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.key_Delete)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_14.addWidget(self.label_56, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_Delete)

        self.key_End = QWidget(self.horizontalWidget_3)
        self.key_End.setObjectName(u"key_End")
        self.key_End.setMinimumSize(QSize(42, 42))
        self.key_End.setMaximumSize(QSize(42, 42))
        self.key_End.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_15 = QGridLayout(self.key_End)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.key_End)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_15.addWidget(self.label_57, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_End)

        self.key_PageDown = QWidget(self.horizontalWidget_3)
        self.key_PageDown.setObjectName(u"key_PageDown")
        self.key_PageDown.setMinimumSize(QSize(42, 42))
        self.key_PageDown.setMaximumSize(QSize(42, 42))
        self.key_PageDown.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_95 = QGridLayout(self.key_PageDown)
        self.gridLayout_95.setSpacing(0)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(5, 5, 5, 5)
        self.label_200 = QLabel(self.key_PageDown)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setStyleSheet(u"border: none; background: transparent")
        self.label_200.setWordWrap(True)

        self.gridLayout_95.addWidget(self.label_200, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_PageDown)

        self.key_seven = QWidget(self.horizontalWidget_3)
        self.key_seven.setObjectName(u"key_seven")
        self.key_seven.setMinimumSize(QSize(42, 42))
        self.key_seven.setMaximumSize(QSize(42, 42))
        self.key_seven.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_17 = QGridLayout(self.key_seven)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.key_seven)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_17.addWidget(self.label_14, 2, 0, 1, 2)

        self.label_10 = QLabel(self.key_seven)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_17.addWidget(self.label_10, 3, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_seven)

        self.key_eight = QWidget(self.horizontalWidget_3)
        self.key_eight.setObjectName(u"key_eight")
        self.key_eight.setMinimumSize(QSize(42, 42))
        self.key_eight.setMaximumSize(QSize(42, 42))
        self.key_eight.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_19 = QGridLayout(self.key_eight)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.key_eight)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_19.addWidget(self.label_46, 2, 0, 1, 2)

        self.label_42 = QLabel(self.key_eight)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_19.addWidget(self.label_42, 3, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.key_eight)

        self.key_nine = QWidget(self.horizontalWidget_3)
        self.key_nine.setObjectName(u"key_nine")
        self.key_nine.setMinimumSize(QSize(42, 42))
        self.key_nine.setMaximumSize(QSize(42, 42))
        self.key_nine.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_20 = QGridLayout(self.key_nine)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.key_nine)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_20.addWidget(self.label_55, 2, 0, 1, 3)

        self.label_54 = QLabel(self.key_nine)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_20.addWidget(self.label_54, 3, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.key_nine)

        self.key_multiplication = QWidget(self.horizontalWidget_3)
        self.key_multiplication.setObjectName(u"key_multiplication")
        self.key_multiplication.setMinimumSize(QSize(42, 42))
        self.key_multiplication.setMaximumSize(QSize(42, 42))
        self.key_multiplication.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_98 = QGridLayout(self.key_multiplication)
        self.gridLayout_98.setSpacing(0)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gridLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_203 = QLabel(self.key_multiplication)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_98.addWidget(self.label_203, 2, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.key_multiplication)


        self.verticalLayout_4.addWidget(self.horizontalWidget_3)

        self.horizontalWidget_4 = QWidget(self.keyboard)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setStyleSheet(u"border-radius: 0px")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.key_Capslock = QWidget(self.horizontalWidget_4)
        self.key_Capslock.setObjectName(u"key_Capslock")
        self.key_Capslock.setMinimumSize(QSize(71, 42))
        self.key_Capslock.setMaximumSize(QSize(71, 42))
        self.key_Capslock.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_34 = QGridLayout(self.key_Capslock)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.key_Capslock)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_34.addWidget(self.label_18, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_Capslock)

        self.key_A = QWidget(self.horizontalWidget_4)
        self.key_A.setObjectName(u"key_A")
        self.key_A.setMinimumSize(QSize(42, 42))
        self.key_A.setMaximumSize(QSize(42, 42))
        self.key_A.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_35 = QGridLayout(self.key_A)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.key_A)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_35.addWidget(self.label_6, 3, 2, 1, 1)

        self.label_34 = QLabel(self.key_A)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_35.addWidget(self.label_34, 3, 0, 1, 1)

        self.label_68 = QLabel(self.key_A)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_35.addWidget(self.label_68, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_A)

        self.key_S = QWidget(self.horizontalWidget_4)
        self.key_S.setObjectName(u"key_S")
        self.key_S.setMinimumSize(QSize(42, 42))
        self.key_S.setMaximumSize(QSize(42, 42))
        self.key_S.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_36 = QGridLayout(self.key_S)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.key_S)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_36.addWidget(self.label_77, 3, 2, 1, 1)

        self.label_88 = QLabel(self.key_S)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_36.addWidget(self.label_88, 3, 0, 1, 1)

        self.label_89 = QLabel(self.key_S)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_36.addWidget(self.label_89, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_S)

        self.key_D = QWidget(self.horizontalWidget_4)
        self.key_D.setObjectName(u"key_D")
        self.key_D.setMinimumSize(QSize(42, 42))
        self.key_D.setMaximumSize(QSize(42, 42))
        self.key_D.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_37 = QGridLayout(self.key_D)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.key_D)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_37.addWidget(self.label_91, 3, 0, 1, 1)

        self.label_92 = QLabel(self.key_D)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_37.addWidget(self.label_92, 2, 0, 1, 1)

        self.label_90 = QLabel(self.key_D)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_37.addWidget(self.label_90, 3, 2, 1, 1)


        self.horizontalLayout.addWidget(self.key_D)

        self.key_F = QWidget(self.horizontalWidget_4)
        self.key_F.setObjectName(u"key_F")
        self.key_F.setMinimumSize(QSize(42, 42))
        self.key_F.setMaximumSize(QSize(42, 42))
        self.key_F.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_38 = QGridLayout(self.key_F)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.key_F)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_38.addWidget(self.label_93, 3, 2, 1, 1)

        self.label_94 = QLabel(self.key_F)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_38.addWidget(self.label_94, 3, 0, 1, 1)

        self.label_95 = QLabel(self.key_F)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_38.addWidget(self.label_95, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_F)

        self.key_G = QWidget(self.horizontalWidget_4)
        self.key_G.setObjectName(u"key_G")
        self.key_G.setMinimumSize(QSize(42, 42))
        self.key_G.setMaximumSize(QSize(42, 42))
        self.key_G.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_39 = QGridLayout(self.key_G)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_97 = QLabel(self.key_G)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_39.addWidget(self.label_97, 3, 0, 1, 1)

        self.label_96 = QLabel(self.key_G)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_39.addWidget(self.label_96, 3, 2, 1, 1)

        self.label_98 = QLabel(self.key_G)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_39.addWidget(self.label_98, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_G)

        self.key_H = QWidget(self.horizontalWidget_4)
        self.key_H.setObjectName(u"key_H")
        self.key_H.setMinimumSize(QSize(42, 42))
        self.key_H.setMaximumSize(QSize(42, 42))
        self.key_H.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_40 = QGridLayout(self.key_H)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.key_H)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_40.addWidget(self.label_99, 3, 2, 1, 1)

        self.label_100 = QLabel(self.key_H)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_40.addWidget(self.label_100, 3, 0, 1, 1)

        self.label_101 = QLabel(self.key_H)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_40.addWidget(self.label_101, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_H)

        self.key_J = QWidget(self.horizontalWidget_4)
        self.key_J.setObjectName(u"key_J")
        self.key_J.setMinimumSize(QSize(42, 42))
        self.key_J.setMaximumSize(QSize(42, 42))
        self.key_J.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_41 = QGridLayout(self.key_J)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.key_J)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_41.addWidget(self.label_102, 3, 2, 1, 1)

        self.label_103 = QLabel(self.key_J)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_41.addWidget(self.label_103, 3, 0, 1, 1)

        self.label_104 = QLabel(self.key_J)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_41.addWidget(self.label_104, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_J)

        self.key_K = QWidget(self.horizontalWidget_4)
        self.key_K.setObjectName(u"key_K")
        self.key_K.setMinimumSize(QSize(42, 42))
        self.key_K.setMaximumSize(QSize(42, 42))
        self.key_K.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_42 = QGridLayout(self.key_K)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_105 = QLabel(self.key_K)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_42.addWidget(self.label_105, 3, 2, 1, 1)

        self.label_106 = QLabel(self.key_K)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_42.addWidget(self.label_106, 3, 0, 1, 1)

        self.label_107 = QLabel(self.key_K)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_42.addWidget(self.label_107, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_K)

        self.key_L = QWidget(self.horizontalWidget_4)
        self.key_L.setObjectName(u"key_L")
        self.key_L.setMinimumSize(QSize(42, 42))
        self.key_L.setMaximumSize(QSize(42, 42))
        self.key_L.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_43 = QGridLayout(self.key_L)
        self.gridLayout_43.setSpacing(0)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.key_L)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_43.addWidget(self.label_108, 3, 2, 1, 1)

        self.label_109 = QLabel(self.key_L)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_43.addWidget(self.label_109, 3, 0, 1, 1)

        self.label_110 = QLabel(self.key_L)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_43.addWidget(self.label_110, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_L)

        self.key_colon = QWidget(self.horizontalWidget_4)
        self.key_colon.setObjectName(u"key_colon")
        self.key_colon.setMinimumSize(QSize(42, 42))
        self.key_colon.setMaximumSize(QSize(42, 42))
        self.key_colon.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_44 = QGridLayout(self.key_colon)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.key_colon)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_44.addWidget(self.label_111, 3, 2, 1, 1)

        self.label_112 = QLabel(self.key_colon)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_44.addWidget(self.label_112, 3, 0, 1, 1)

        self.label_113 = QLabel(self.key_colon)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_44.addWidget(self.label_113, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_colon)

        self.key_backtick = QWidget(self.horizontalWidget_4)
        self.key_backtick.setObjectName(u"key_backtick")
        self.key_backtick.setMinimumSize(QSize(42, 42))
        self.key_backtick.setMaximumSize(QSize(42, 42))
        self.key_backtick.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_45 = QGridLayout(self.key_backtick)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_115 = QLabel(self.key_backtick)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_45.addWidget(self.label_115, 3, 0, 1, 1)

        self.label_116 = QLabel(self.key_backtick)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_45.addWidget(self.label_116, 2, 0, 1, 1)

        self.label_114 = QLabel(self.key_backtick)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_45.addWidget(self.label_114, 3, 2, 1, 1)


        self.horizontalLayout.addWidget(self.key_backtick)

        self.key_Return = QWidget(self.horizontalWidget_4)
        self.key_Return.setObjectName(u"key_Return")
        self.key_Return.setMinimumSize(QSize(61, 42))
        self.key_Return.setMaximumSize(QSize(61, 42))
        self.key_Return.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_46 = QGridLayout(self.key_Return)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.key_Return)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_46.addWidget(self.label_117, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_Return)

        self.widget_4 = QWidget(self.horizontalWidget_4)
        self.widget_4.setObjectName(u"widget_4")

        self.horizontalLayout.addWidget(self.widget_4)

        self.key_four = QWidget(self.horizontalWidget_4)
        self.key_four.setObjectName(u"key_four")
        self.key_four.setMinimumSize(QSize(42, 42))
        self.key_four.setMaximumSize(QSize(42, 42))
        self.key_four.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_47 = QGridLayout(self.key_four)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.key_four)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_47.addWidget(self.label_118, 1, 0, 1, 2)

        self.label_119 = QLabel(self.key_four)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_47.addWidget(self.label_119, 2, 2, 1, 1)


        self.horizontalLayout.addWidget(self.key_four)

        self.key_five = QWidget(self.horizontalWidget_4)
        self.key_five.setObjectName(u"key_five")
        self.key_five.setMinimumSize(QSize(42, 42))
        self.key_five.setMaximumSize(QSize(42, 42))
        self.key_five.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_48 = QGridLayout(self.key_five)
        self.gridLayout_48.setSpacing(0)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.key_five)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_48.addWidget(self.label_121, 3, 2, 1, 1)

        self.label_120 = QLabel(self.key_five)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_48.addWidget(self.label_120, 2, 0, 1, 2)


        self.horizontalLayout.addWidget(self.key_five)

        self.key_six = QWidget(self.horizontalWidget_4)
        self.key_six.setObjectName(u"key_six")
        self.key_six.setMinimumSize(QSize(42, 42))
        self.key_six.setMaximumSize(QSize(42, 42))
        self.key_six.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_49 = QGridLayout(self.key_six)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_122 = QLabel(self.key_six)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_49.addWidget(self.label_122, 2, 0, 1, 2)

        self.label_123 = QLabel(self.key_six)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_49.addWidget(self.label_123, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.key_six)

        self.key_minus = QWidget(self.horizontalWidget_4)
        self.key_minus.setObjectName(u"key_minus")
        self.key_minus.setMinimumSize(QSize(42, 42))
        self.key_minus.setMaximumSize(QSize(42, 42))
        self.key_minus.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_99 = QGridLayout(self.key_minus)
        self.gridLayout_99.setSpacing(0)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.gridLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_204 = QLabel(self.key_minus)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_99.addWidget(self.label_204, 2, 0, 1, 2)


        self.horizontalLayout.addWidget(self.key_minus)


        self.verticalLayout_4.addWidget(self.horizontalWidget_4)

        self.horizontalWidget_5 = QWidget(self.keyboard)
        self.horizontalWidget_5.setObjectName(u"horizontalWidget_5")
        self.horizontalWidget_5.setStyleSheet(u"border-radius: 0px")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.key_Shift = QWidget(self.horizontalWidget_5)
        self.key_Shift.setObjectName(u"key_Shift")
        self.key_Shift.setMinimumSize(QSize(87, 42))
        self.key_Shift.setMaximumSize(QSize(87, 42))
        self.key_Shift.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_50 = QGridLayout(self.key_Shift)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_124 = QLabel(self.key_Shift)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMaximumSize(QSize(16777215, 16777215))
        self.label_124.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_50.addWidget(self.label_124, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_Shift)

        self.key_Z = QWidget(self.horizontalWidget_5)
        self.key_Z.setObjectName(u"key_Z")
        self.key_Z.setMinimumSize(QSize(42, 42))
        self.key_Z.setMaximumSize(QSize(42, 42))
        self.key_Z.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_51 = QGridLayout(self.key_Z)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_125 = QLabel(self.key_Z)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_51.addWidget(self.label_125, 3, 2, 1, 1)

        self.label_126 = QLabel(self.key_Z)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_51.addWidget(self.label_126, 3, 0, 1, 1)

        self.label_127 = QLabel(self.key_Z)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_51.addWidget(self.label_127, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_Z)

        self.key_X = QWidget(self.horizontalWidget_5)
        self.key_X.setObjectName(u"key_X")
        self.key_X.setMinimumSize(QSize(42, 42))
        self.key_X.setMaximumSize(QSize(42, 42))
        self.key_X.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_52 = QGridLayout(self.key_X)
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_128 = QLabel(self.key_X)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_52.addWidget(self.label_128, 3, 2, 1, 1)

        self.label_129 = QLabel(self.key_X)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_52.addWidget(self.label_129, 3, 0, 1, 1)

        self.label_130 = QLabel(self.key_X)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_52.addWidget(self.label_130, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_X)

        self.key_C = QWidget(self.horizontalWidget_5)
        self.key_C.setObjectName(u"key_C")
        self.key_C.setMinimumSize(QSize(42, 42))
        self.key_C.setMaximumSize(QSize(42, 42))
        self.key_C.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_53 = QGridLayout(self.key_C)
        self.gridLayout_53.setSpacing(0)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_131 = QLabel(self.key_C)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_53.addWidget(self.label_131, 3, 2, 1, 1)

        self.label_132 = QLabel(self.key_C)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_53.addWidget(self.label_132, 3, 0, 1, 1)

        self.label_133 = QLabel(self.key_C)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_53.addWidget(self.label_133, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_C)

        self.key_V = QWidget(self.horizontalWidget_5)
        self.key_V.setObjectName(u"key_V")
        self.key_V.setMinimumSize(QSize(42, 42))
        self.key_V.setMaximumSize(QSize(42, 42))
        self.key_V.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_54 = QGridLayout(self.key_V)
        self.gridLayout_54.setSpacing(0)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_134 = QLabel(self.key_V)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_54.addWidget(self.label_134, 3, 2, 1, 1)

        self.label_135 = QLabel(self.key_V)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_54.addWidget(self.label_135, 3, 0, 1, 1)

        self.label_136 = QLabel(self.key_V)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_54.addWidget(self.label_136, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_V)

        self.key_B = QWidget(self.horizontalWidget_5)
        self.key_B.setObjectName(u"key_B")
        self.key_B.setMinimumSize(QSize(42, 42))
        self.key_B.setMaximumSize(QSize(42, 42))
        self.key_B.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_55 = QGridLayout(self.key_B)
        self.gridLayout_55.setSpacing(0)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_137 = QLabel(self.key_B)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_55.addWidget(self.label_137, 3, 2, 1, 1)

        self.label_138 = QLabel(self.key_B)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_55.addWidget(self.label_138, 3, 0, 1, 1)

        self.label_139 = QLabel(self.key_B)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_55.addWidget(self.label_139, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_B)

        self.key_N = QWidget(self.horizontalWidget_5)
        self.key_N.setObjectName(u"key_N")
        self.key_N.setMinimumSize(QSize(42, 42))
        self.key_N.setMaximumSize(QSize(42, 42))
        self.key_N.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_56 = QGridLayout(self.key_N)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_140 = QLabel(self.key_N)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_56.addWidget(self.label_140, 3, 2, 1, 1)

        self.label_141 = QLabel(self.key_N)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_56.addWidget(self.label_141, 3, 0, 1, 1)

        self.label_142 = QLabel(self.key_N)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_56.addWidget(self.label_142, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_N)

        self.key_M = QWidget(self.horizontalWidget_5)
        self.key_M.setObjectName(u"key_M")
        self.key_M.setMinimumSize(QSize(42, 42))
        self.key_M.setMaximumSize(QSize(42, 42))
        self.key_M.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_57 = QGridLayout(self.key_M)
        self.gridLayout_57.setSpacing(0)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_143 = QLabel(self.key_M)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_57.addWidget(self.label_143, 3, 2, 1, 1)

        self.label_144 = QLabel(self.key_M)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_57.addWidget(self.label_144, 3, 0, 1, 1)

        self.label_145 = QLabel(self.key_M)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_57.addWidget(self.label_145, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_M)

        self.key_comma = QWidget(self.horizontalWidget_5)
        self.key_comma.setObjectName(u"key_comma")
        self.key_comma.setMinimumSize(QSize(42, 42))
        self.key_comma.setMaximumSize(QSize(42, 42))
        self.key_comma.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_58 = QGridLayout(self.key_comma)
        self.gridLayout_58.setSpacing(0)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_146 = QLabel(self.key_comma)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_58.addWidget(self.label_146, 3, 2, 1, 1)

        self.label_147 = QLabel(self.key_comma)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_58.addWidget(self.label_147, 3, 0, 1, 1)

        self.label_comma = QLabel(self.key_comma)
        self.label_comma.setObjectName(u"label_comma")
        self.label_comma.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_58.addWidget(self.label_comma, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_comma)

        self.key_point = QWidget(self.horizontalWidget_5)
        self.key_point.setObjectName(u"key_point")
        self.key_point.setMinimumSize(QSize(42, 42))
        self.key_point.setMaximumSize(QSize(42, 42))
        self.key_point.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_59 = QGridLayout(self.key_point)
        self.gridLayout_59.setSpacing(0)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_148 = QLabel(self.key_point)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_59.addWidget(self.label_148, 3, 2, 1, 1)

        self.label_149 = QLabel(self.key_point)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_59.addWidget(self.label_149, 3, 0, 1, 1)

        self.label_comma_2 = QLabel(self.key_point)
        self.label_comma_2.setObjectName(u"label_comma_2")
        self.label_comma_2.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_59.addWidget(self.label_comma_2, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_point)

        self.key_slash = QWidget(self.horizontalWidget_5)
        self.key_slash.setObjectName(u"key_slash")
        self.key_slash.setMinimumSize(QSize(42, 42))
        self.key_slash.setMaximumSize(QSize(42, 42))
        self.key_slash.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_60 = QGridLayout(self.key_slash)
        self.gridLayout_60.setSpacing(0)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_150 = QLabel(self.key_slash)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_60.addWidget(self.label_150, 3, 2, 1, 1)

        self.label_151 = QLabel(self.key_slash)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_60.addWidget(self.label_151, 3, 0, 1, 1)

        self.label_comma_3 = QLabel(self.key_slash)
        self.label_comma_3.setObjectName(u"label_comma_3")
        self.label_comma_3.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_60.addWidget(self.label_comma_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.key_slash)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_60.addWidget(self.label_2, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_slash)

        self.key_Shift_2 = QWidget(self.horizontalWidget_5)
        self.key_Shift_2.setObjectName(u"key_Shift_2")
        self.key_Shift_2.setMinimumSize(QSize(87, 42))
        self.key_Shift_2.setMaximumSize(QSize(87, 42))
        self.key_Shift_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_61 = QGridLayout(self.key_Shift_2)
        self.gridLayout_61.setSpacing(0)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_152 = QLabel(self.key_Shift_2)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_61.addWidget(self.label_152, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_Shift_2)

        self.widget_6 = QWidget(self.horizontalWidget_5)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_2.addWidget(self.widget_6)

        self.key_up = QWidget(self.horizontalWidget_5)
        self.key_up.setObjectName(u"key_up")
        self.key_up.setMinimumSize(QSize(42, 42))
        self.key_up.setMaximumSize(QSize(42, 42))
        self.key_up.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_73 = QGridLayout(self.key_up)
        self.gridLayout_73.setSpacing(0)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_168 = QLabel(self.key_up)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setStyleSheet(u"border: none;  background: transparent")
        self.label_168.setPixmap(QPixmap(u":/newPrefix/arrow-up.svg"))

        self.gridLayout_73.addWidget(self.label_168, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.key_up)

        self.widget_5 = QWidget(self.horizontalWidget_5)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.key_one = QWidget(self.horizontalWidget_5)
        self.key_one.setObjectName(u"key_one")
        self.key_one.setMinimumSize(QSize(42, 42))
        self.key_one.setMaximumSize(QSize(42, 42))
        self.key_one.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_62 = QGridLayout(self.key_one)
        self.gridLayout_62.setSpacing(0)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_153 = QLabel(self.key_one)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_62.addWidget(self.label_153, 2, 0, 1, 2)

        self.label_154 = QLabel(self.key_one)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_62.addWidget(self.label_154, 3, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_one)

        self.key_two = QWidget(self.horizontalWidget_5)
        self.key_two.setObjectName(u"key_two")
        self.key_two.setMinimumSize(QSize(42, 42))
        self.key_two.setMaximumSize(QSize(42, 42))
        self.key_two.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_63 = QGridLayout(self.key_two)
        self.gridLayout_63.setSpacing(0)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_155 = QLabel(self.key_two)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_63.addWidget(self.label_155, 2, 0, 1, 2)

        self.label_156 = QLabel(self.key_two)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_63.addWidget(self.label_156, 3, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_two)

        self.key_three = QWidget(self.horizontalWidget_5)
        self.key_three.setObjectName(u"key_three")
        self.key_three.setMinimumSize(QSize(42, 42))
        self.key_three.setMaximumSize(QSize(42, 42))
        self.key_three.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_64 = QGridLayout(self.key_three)
        self.gridLayout_64.setSpacing(0)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.key_three)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_64.addWidget(self.label_157, 2, 0, 1, 2)

        self.label_158 = QLabel(self.key_three)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_64.addWidget(self.label_158, 3, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.key_three)

        self.key_plus_2 = QWidget(self.horizontalWidget_5)
        self.key_plus_2.setObjectName(u"key_plus_2")
        self.key_plus_2.setMinimumSize(QSize(42, 42))
        self.key_plus_2.setMaximumSize(QSize(42, 42))
        self.key_plus_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_103 = QGridLayout(self.key_plus_2)
        self.gridLayout_103.setSpacing(0)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.label_210 = QLabel(self.key_plus_2)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_103.addWidget(self.label_210, 2, 0, 1, 2)


        self.horizontalLayout_2.addWidget(self.key_plus_2)


        self.verticalLayout_4.addWidget(self.horizontalWidget_5)

        self.horizontalWidget_6 = QWidget(self.keyboard)
        self.horizontalWidget_6.setObjectName(u"horizontalWidget_6")
        self.horizontalWidget_6.setStyleSheet(u"border-radius: 0px")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.key_Control = QWidget(self.horizontalWidget_6)
        self.key_Control.setObjectName(u"key_Control")
        self.key_Control.setMinimumSize(QSize(49, 42))
        self.key_Control.setMaximumSize(QSize(49, 42))
        self.key_Control.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.key_Control)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.label_232 = QLabel(self.key_Control)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setMaximumSize(QSize(20, 20))
        self.label_232.setStyleSheet(u"border: none;  background: transparent")
        self.label_232.setPixmap(QPixmap(u":/newPrefix/chevron-up.svg"))
        self.label_232.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_232)

        self.label_161 = QLabel(self.key_Control)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_16.addWidget(self.label_161)


        self.horizontalLayout_6.addWidget(self.key_Control)

        self.key_Option = QWidget(self.horizontalWidget_6)
        self.key_Option.setObjectName(u"key_Option")
        self.key_Option.setMinimumSize(QSize(49, 42))
        self.key_Option.setMaximumSize(QSize(49, 42))
        self.key_Option.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.key_Option)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.label_233 = QLabel(self.key_Option)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMaximumSize(QSize(20, 20))
        self.label_233.setStyleSheet(u"border: none;  background: transparent")
        self.label_233.setPixmap(QPixmap(u":/newPrefix/option.svg"))
        self.label_233.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_233)

        self.label_162 = QLabel(self.key_Option)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_17.addWidget(self.label_162)


        self.horizontalLayout_6.addWidget(self.key_Option)

        self.key_Command = QWidget(self.horizontalWidget_6)
        self.key_Command.setObjectName(u"key_Command")
        self.key_Command.setMinimumSize(QSize(60, 42))
        self.key_Command.setMaximumSize(QSize(60, 42))
        self.key_Command.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_18 = QVBoxLayout(self.key_Command)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.label_234 = QLabel(self.key_Command)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMaximumSize(QSize(20, 20))
        self.label_234.setStyleSheet(u"border: none;  background: transparent")
        self.label_234.setPixmap(QPixmap(u":/newPrefix/command.svg"))
        self.label_234.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_234)

        self.label_163 = QLabel(self.key_Command)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_18.addWidget(self.label_163)


        self.horizontalLayout_6.addWidget(self.key_Command)

        self.key_Space = QWidget(self.horizontalWidget_6)
        self.key_Space.setObjectName(u"key_Space")
        self.key_Space.setMinimumSize(QSize(278, 42))
        self.key_Space.setMaximumSize(QSize(278, 42))
        self.key_Space.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_68 = QGridLayout(self.key_Space)
        self.gridLayout_68.setSpacing(0)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.key_Space)

        self.key_Command_2 = QWidget(self.horizontalWidget_6)
        self.key_Command_2.setObjectName(u"key_Command_2")
        self.key_Command_2.setMinimumSize(QSize(60, 42))
        self.key_Command_2.setMaximumSize(QSize(60, 42))
        self.key_Command_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.key_Command_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.label_235 = QLabel(self.key_Command_2)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setMaximumSize(QSize(20, 20))
        self.label_235.setStyleSheet(u"border: none;  background: transparent")
        self.label_235.setPixmap(QPixmap(u":/newPrefix/command.svg"))
        self.label_235.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_235)

        self.label_164 = QLabel(self.key_Command_2)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_19.addWidget(self.label_164)


        self.horizontalLayout_6.addWidget(self.key_Command_2)

        self.key_Option_2 = QWidget(self.horizontalWidget_6)
        self.key_Option_2.setObjectName(u"key_Option_2")
        self.key_Option_2.setMinimumSize(QSize(49, 42))
        self.key_Option_2.setMaximumSize(QSize(49, 42))
        self.key_Option_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.key_Option_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.label_237 = QLabel(self.key_Option_2)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setMaximumSize(QSize(20, 20))
        self.label_237.setStyleSheet(u"border: none;  background: transparent")
        self.label_237.setPixmap(QPixmap(u":/newPrefix/option.svg"))
        self.label_237.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_237)

        self.label_167 = QLabel(self.key_Option_2)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_21.addWidget(self.label_167)


        self.horizontalLayout_6.addWidget(self.key_Option_2)

        self.key_Control_2 = QWidget(self.horizontalWidget_6)
        self.key_Control_2.setObjectName(u"key_Control_2")
        self.key_Control_2.setMinimumSize(QSize(49, 42))
        self.key_Control_2.setMaximumSize(QSize(49, 42))
        self.key_Control_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.key_Control_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.label_236 = QLabel(self.key_Control_2)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setMaximumSize(QSize(20, 20))
        self.label_236.setStyleSheet(u"border: none;  background: transparent")
        self.label_236.setPixmap(QPixmap(u":/newPrefix/chevron-up.svg"))
        self.label_236.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_236)

        self.label_165 = QLabel(self.key_Control_2)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setStyleSheet(u"border: none;  background: transparent")

        self.verticalLayout_20.addWidget(self.label_165)


        self.horizontalLayout_6.addWidget(self.key_Control_2)

        self.key_left = QWidget(self.horizontalWidget_6)
        self.key_left.setObjectName(u"key_left")
        self.key_left.setMinimumSize(QSize(42, 42))
        self.key_left.setMaximumSize(QSize(42, 42))
        self.key_left.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_74 = QGridLayout(self.key_left)
        self.gridLayout_74.setSpacing(0)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setContentsMargins(0, 0, 0, 0)
        self.label_169 = QLabel(self.key_left)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setStyleSheet(u"border: none;  background: transparent")
        self.label_169.setPixmap(QPixmap(u":/newPrefix/arrow-left.svg"))

        self.gridLayout_74.addWidget(self.label_169, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.key_left)

        self.key_down = QWidget(self.horizontalWidget_6)
        self.key_down.setObjectName(u"key_down")
        self.key_down.setMinimumSize(QSize(42, 42))
        self.key_down.setMaximumSize(QSize(42, 42))
        self.key_down.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_75 = QGridLayout(self.key_down)
        self.gridLayout_75.setSpacing(0)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.gridLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_170 = QLabel(self.key_down)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setStyleSheet(u"border: none;  background: transparent")
        self.label_170.setPixmap(QPixmap(u":/newPrefix/arrow-down.svg"))

        self.gridLayout_75.addWidget(self.label_170, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.key_down)

        self.key_right = QWidget(self.horizontalWidget_6)
        self.key_right.setObjectName(u"key_right")
        self.key_right.setMinimumSize(QSize(42, 42))
        self.key_right.setMaximumSize(QSize(42, 42))
        self.key_right.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_76 = QGridLayout(self.key_right)
        self.gridLayout_76.setSpacing(0)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.key_right)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setStyleSheet(u"border: none;  background: transparent")
        self.label_171.setPixmap(QPixmap(u":/newPrefix/arrow-right.svg"))

        self.gridLayout_76.addWidget(self.label_171, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.key_right)

        self.key_Ins = QWidget(self.horizontalWidget_6)
        self.key_Ins.setObjectName(u"key_Ins")
        self.key_Ins.setMinimumSize(QSize(84, 42))
        self.key_Ins.setMaximumSize(QSize(84, 42))
        self.key_Ins.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_100 = QGridLayout(self.key_Ins)
        self.gridLayout_100.setSpacing(0)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_206 = QLabel(self.key_Ins)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setStyleSheet(u"border: none; background: transparent")

        self.gridLayout_100.addWidget(self.label_206, 3, 0, 1, 1)

        self.label_207 = QLabel(self.key_Ins)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_100.addWidget(self.label_207, 2, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.key_Ins)

        self.key_Del = QWidget(self.horizontalWidget_6)
        self.key_Del.setObjectName(u"key_Del")
        self.key_Del.setMinimumSize(QSize(42, 42))
        self.key_Del.setMaximumSize(QSize(42, 42))
        self.key_Del.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_101 = QGridLayout(self.key_Del)
        self.gridLayout_101.setSpacing(0)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.gridLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_209 = QLabel(self.key_Del)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_101.addWidget(self.label_209, 2, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.key_Del)

        self.key_Enter_2 = QWidget(self.horizontalWidget_6)
        self.key_Enter_2.setObjectName(u"key_Enter_2")
        self.key_Enter_2.setMinimumSize(QSize(42, 42))
        self.key_Enter_2.setMaximumSize(QSize(42, 42))
        self.key_Enter_2.setStyleSheet(u"border: 1px solid black;\n"
"background-color: #D9D9D9; \n"
"border-radius: 5px;\n"
" color: black; \n"
"")
        self.gridLayout_102 = QGridLayout(self.key_Enter_2)
        self.gridLayout_102.setSpacing(0)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.gridLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_205 = QLabel(self.key_Enter_2)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setStyleSheet(u"border: none;  background: transparent")

        self.gridLayout_102.addWidget(self.label_205, 2, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.key_Enter_2)


        self.verticalLayout_4.addWidget(self.horizontalWidget_6)


        self.verticalLayout.addWidget(self.keyboard, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_3 = QWidget(self.keyboard_container)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.keyboard_container)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 10)

        self.verticalLayout_3.addWidget(self.keyboard_container)

        self.verticalLayout_3.setStretch(1, 25)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button_keyboard.setText("")
        self.Button_reset.setText("")
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"  Esc", None))
        self.label_160.setText("")
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.label_223.setText("")
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"    F2", None))
        self.label_224.setText("")
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"    F3", None))
        self.label_225.setText("")
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"    F4", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"    F5", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"    F6", None))
        self.label_226.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"    F7", None))
        self.label_227.setText("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"    F8", None))
        self.label_228.setText("")
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"    F9", None))
        self.label_229.setText("")
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"    F10", None))
        self.label_230.setText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"    F11", None))
        self.label_231.setText("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"    F12", None))
        self.label_214.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"    F13", None))
        self.label_196.setText("")
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"    F14", None))
        self.label_208.setText("")
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"    F15", None))
        self.label_212.setText("")
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"    F16", None))
        self.label_215.setText("")
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"    F17", None))
        self.label_217.setText("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"    F18", None))
        self.label_219.setText("")
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"    F18", None))
        self.label_221.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u" \u0419", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"    '", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"   ~", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"   1", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"    !", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"  \"", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"   2", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"  @", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u" \u2116", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"   3", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"  #", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"  ;", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"   4", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"   $", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"   5", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"   %", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"  :", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"   6", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"  ^", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"  ?", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"   7", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"  &", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"   8", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"   *", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"   9", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"   (", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"   )", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"   0", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"   -", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"   _", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"   +", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"   =", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"    Fn", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Page Up", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"     =", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"      /", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"   Tab", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" \u0419", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"  Q", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"  \u0426", None))
        self.label_47.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"  W", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"  \u0423", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"   E", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"  \u041a", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"  R", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"  \u0415", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"  T", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u" \u041d", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"   Y", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  \u0413", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"  U", None))
        self.label_11.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"   I", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0428", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0429", None))
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"  O", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"  P", None))
        self.label_35.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"  \u0417", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"  \u0425", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"  {", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"  \u042a", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"  }", None))
        self.label_43.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"  |", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"  \\", None))
        self.label_51.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"   End", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Page Down", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"     7", None))
        self.label_10.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"     8", None))
        self.label_42.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"     9", None))
        self.label_54.setText("")
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"      *", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"  Caps lock", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" \u0424", None))
        self.label_34.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"  A", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u" \u042b", None))
        self.label_88.setText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"  S", None))
        self.label_91.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"  D", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u" \u0412", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u" \u0410", None))
        self.label_94.setText("")
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"   F", None))
        self.label_97.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u" \u041f", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"  G", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u" \u0420", None))
        self.label_100.setText("")
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"  H", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u" \u041e", None))
        self.label_103.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"   J", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"  \u041b", None))
        self.label_106.setText("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"  K", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u" \u0414", None))
        self.label_109.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"   L", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u" \u0416", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"   ;", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"   :", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"   '", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"   \"", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"  \u042d", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"   Return", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"     4", None))
        self.label_119.setText("")
        self.label_121.setText("")
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"     5", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"     6", None))
        self.label_123.setText("")
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"      -", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"  Shift", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"  \u042f", None))
        self.label_126.setText("")
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"   Z", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"  \u0427", None))
        self.label_129.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"   X", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"  \u0421", None))
        self.label_132.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"  C", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"  \u041c", None))
        self.label_135.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"  V", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"  \u0418", None))
        self.label_138.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"  B", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"  \u0422", None))
        self.label_141.setText("")
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"  N", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"  \u042c", None))
        self.label_144.setText("")
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"  M", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"  \u0411", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"   ,", None))
        self.label_comma.setText(QCoreApplication.translate("MainWindow", u"  <", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u" \u042e", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"   .", None))
        self.label_comma_2.setText(QCoreApplication.translate("MainWindow", u"  >", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"   .", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"   /", None))
        self.label_comma_3.setText(QCoreApplication.translate("MainWindow", u"   ?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  ,", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"  Shift", None))
        self.label_168.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"     1", None))
        self.label_154.setText("")
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"     2", None))
        self.label_156.setText("")
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"     3", None))
        self.label_158.setText("")
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"     +", None))
        self.label_232.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindow", u" Control", None))
        self.label_233.setText("")
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.label_234.setText("")
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.label_235.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.label_237.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.label_236.setText("")
        self.label_165.setText(QCoreApplication.translate("MainWindow", u" Control", None))
        self.label_169.setText("")
        self.label_170.setText("")
        self.label_171.setText("")
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"   Ins", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"   0", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"      .", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"   Enter", None))
    # retranslateUi

