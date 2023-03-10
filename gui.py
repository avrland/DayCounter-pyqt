import sys
import json
import time
import subprocess
import traceback
import asyncio
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QTextEdit
from PyQt5.QtCore import pyqtSlot, QDate, Qt
from PyQt5.QtGui import QPixmap, QColor
from backend import Backend

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        self.backend = Backend()
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("Main window")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 621, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 601, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 601, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setPlaceholderText("Select your date or one from listed event")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEnabled(True)
        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 601, 181))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 200, 301, 191))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget_5)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("border-style: none; background-color: transparent;") 
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.transparent))
        self.graphicsView.setScene(self.scene)
        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(320, 200, 291, 191))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.activateComboBox()
        self.createPopupInstance()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "DayCounter-pyqt"))
        self.label.setText(_translate("MainWindow", "It\'s been x days since"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "Choose event (or select your date):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main window"))
        self.label_3.setFont(QtGui.QFont('Arial',20))
        self.label_3.setText(_translate("MainWindow", "Marcin Popko"))
        self.addAboutMe()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About me"))
        # Load the PNG image and create a QPixmap from it
        pixmap = QtGui.QPixmap("graphics/me.jpg")
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmap_item)

    def addAboutMe(self):
        text = "Hello! I\'m From Bialystok, Poland I\'m interested in dancing, singing, coding \n crazy stuff (currently working as embedded dev. Feel free to e-mail me <a href=\"mailto:marcinpopko@outlook.com\">marcinpopko@outlook.com</a>)"
        self.label_4.setFont(QtGui.QFont('Arial', 8))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_4.setText(text)
        self.label_4.setWordWrap(True)

    def activateComboBox(self):
        self.comboBox.currentIndexChanged.connect(self.on_index_changed)
        self.comboBox.addItem("Your date - select from calendar")
        for i in self.backend.event_list:
            self.comboBox.addItem(i + " " + self.backend.get_event_date(i))
        self.comboBox.setCurrentIndex(1)

    @pyqtSlot(int)
    def on_index_changed(self,index):
        if index == 0:
            self.popup.show()
            self.comboBox.setEnabled(False)
        else:
            days, future = self.backend.get_days_from_event(self.backend.return_events_list()[index-1])
            if days == -1:
                self.label.setText( "Wrong date format of event " + self.backend.return_events_list()[index-1])
            else:
                if not future:
                    self.label.setText( "It\'s been " + str(days) + " days since " + self.backend.return_events_list()[index-1])
                else:
                    self.label.setText( "There are " + str(days) + " days from the date of " + self.backend.return_events_list()[index-1])

    '''
    Popup related stuff
    '''
    def createPopupInstance(self):
        self.popup = Ui_Form()
        self.popup.pushButton.clicked.connect(self.sendDateCloseWindow)
    def sendDateCloseWindow(self):
        selected_date = self.popup.calendarWidget.selectedDate()
        selected_date_str = selected_date.toString("dd.MM.yyyy")
        self.popup.close()
        days, future = self.backend.get_days_from_date(selected_date_str)
        if not future:
            self.label.setText( "It\'s been " + str(days) + " days since " + selected_date_str)
        else:
            self.label.setText( "There are " + str(days) + " days from the date of " + selected_date_str)
        self.comboBox.setEnabled(True)

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("self")
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        #self.calendarWidget.setMaximumDate(QDate.currentDate())
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 420, 621, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Select date"))
        self.pushButton.setText(_translate("Form", "Accept date"))