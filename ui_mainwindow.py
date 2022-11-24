# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"智能伴驾机器人")
        MainWindow.resize(1920, 1080)
        self.actionOpen_camera = QAction(MainWindow)
        self.actionOpen_camera.setObjectName(u"actionOpen_camera")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1000, 1000))
        self.label.setMaximumSize(QSize(1000, 1000))
        self.label.setStyleSheet('''
        border: 2px solid #000000;
        border-radius: 8px;
        margin-left:1ex;
        font-size:10px;
        color:red;
        ''')
        self.horizontalLayout.addWidget(self.label)

        # 添加一个标题栏目
        self.verticalLayout_top = QVBoxLayout()
        self.verticalLayout_top.setObjectName(u"verticalLayout_top")
        self.horizontalLayout_top = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_top.setObjectName(u"horizontalLayout_top")
        self.label_top = QLabel(self.centralwidget)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setMinimumSize(QSize(3840, 100))
        self.label_top.setMinimumSize(QSize(3840, 100))
        self.label_top.setStyleSheet("font-size:20px;color:red;margin-left:3200px;margin-top:40px;padding-left:2000px;font-weight:bolder;")
        self.horizontalLayout_top.addWidget(self.label_top)
        self.verticalLayout_top.addLayout(self.horizontalLayout_top)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(600, 140))
        self.label_2.setMaximumSize(QSize(600, 140))
        self.label_2.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(600, 140))
        self.label_10.setStyleSheet("font-size:20px;color:#000000;")

        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(600, 140))
        self.label_3.setStyleSheet("font-size:20px;color:#000000;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(600, 140))
        self.label_4.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(600, 140))
        self.label_5.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(600, 140))
        self.label_9.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_4.addWidget(self.label_9)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(600, 140))
        self.label_6.setStyleSheet("font-size:20px;color:#000000;")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(600, 140))
        self.label_7.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(600, 140))
        self.label_8.setStyleSheet("font-size:20px;color:#000000;")
        self.horizontalLayout_3.addWidget(self.label_8)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(1000, 200))

        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionOpen_camera)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_camera.setText(QCoreApplication.translate("MainWindow", u"Open camera", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Open", None))
    # retranslateUi

    # 消息框显示函数
    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
