# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 242)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.key_tab = QWidget()
        self.key_tab.setObjectName(u"key_tab")
        self.verticalLayout = QVBoxLayout(self.key_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.d_label = QLabel(self.key_tab)
        self.d_label.setObjectName(u"d_label")

        self.gridLayout.addWidget(self.d_label, 3, 0, 1, 1)

        self.n_label = QLabel(self.key_tab)
        self.n_label.setObjectName(u"n_label")

        self.gridLayout.addWidget(self.n_label, 0, 0, 1, 1)

        self.e_lineEdit = QLineEdit(self.key_tab)
        self.e_lineEdit.setObjectName(u"e_lineEdit")

        self.gridLayout.addWidget(self.e_lineEdit, 1, 1, 1, 1)

        self.d_lineEdit = QLineEdit(self.key_tab)
        self.d_lineEdit.setObjectName(u"d_lineEdit")

        self.gridLayout.addWidget(self.d_lineEdit, 3, 1, 1, 1)

        self.secret_visiable_chBox = QCheckBox(self.key_tab)
        self.secret_visiable_chBox.setObjectName(u"secret_visiable_chBox")

        self.gridLayout.addWidget(self.secret_visiable_chBox, 4, 1, 1, 1)

        self.e_label = QLabel(self.key_tab)
        self.e_label.setObjectName(u"e_label")

        self.gridLayout.addWidget(self.e_label, 1, 0, 1, 1)

        self.n_lineEdit = QLineEdit(self.key_tab)
        self.n_lineEdit.setObjectName(u"n_lineEdit")

        self.gridLayout.addWidget(self.n_lineEdit, 0, 1, 1, 1)

        self.line = QFrame(self.key_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)

        self.line_2 = QFrame(self.key_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(self.key_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.tabWidget.addTab(self.key_tab, "")
        self.code_tab = QWidget()
        self.code_tab.setObjectName(u"code_tab")
        self.verticalLayout_3 = QVBoxLayout(self.code_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filePath_lineEdit = QLineEdit(self.code_tab)
        self.filePath_lineEdit.setObjectName(u"filePath_lineEdit")

        self.horizontalLayout_2.addWidget(self.filePath_lineEdit)

        self.openFile_ToolBtn = QToolButton(self.code_tab)
        self.openFile_ToolBtn.setObjectName(u"openFile_ToolBtn")

        self.horizontalLayout_2.addWidget(self.openFile_ToolBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.n_label_2 = QLabel(self.code_tab)
        self.n_label_2.setObjectName(u"n_label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.n_label_2)

        self.key_label = QLabel(self.code_tab)
        self.key_label.setObjectName(u"key_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.key_label)

        self.n_lineEdit_2 = QLineEdit(self.code_tab)
        self.n_lineEdit_2.setObjectName(u"n_lineEdit_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.n_lineEdit_2)

        self.key_lineEdit = QLineEdit(self.code_tab)
        self.key_lineEdit.setObjectName(u"key_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.key_lineEdit)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.encode_ratioBtn = QRadioButton(self.code_tab)
        self.encode_ratioBtn.setObjectName(u"encode_ratioBtn")
        self.encode_ratioBtn.setEnabled(True)
        self.encode_ratioBtn.setChecked(True)

        self.horizontalLayout.addWidget(self.encode_ratioBtn)

        self.decode_ratioBtn = QRadioButton(self.code_tab)
        self.decode_ratioBtn.setObjectName(u"decode_ratioBtn")

        self.horizontalLayout.addWidget(self.decode_ratioBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.code_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.code_tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 22))
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"tomo jelo laso", None))
        self.d_label.setText(QCoreApplication.translate("MainWindow", u"Secret Key D:", None))
        self.n_label.setText(QCoreApplication.translate("MainWindow", u"Public Number N:", None))
        self.secret_visiable_chBox.setText(QCoreApplication.translate("MainWindow", u"secret key visiable", None))
        self.e_label.setText(QCoreApplication.translate("MainWindow", u"Public Key E:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.key_tab), QCoreApplication.translate("MainWindow", u"key generation", None))
        self.openFile_ToolBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.n_label_2.setText(QCoreApplication.translate("MainWindow", u"Public Number N:", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"Public Key E:", None))
        self.encode_ratioBtn.setText(QCoreApplication.translate("MainWindow", u"encode", None))
        self.decode_ratioBtn.setText(QCoreApplication.translate("MainWindow", u"decode", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PROCESS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.code_tab), QCoreApplication.translate("MainWindow", u"encode/decode", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

