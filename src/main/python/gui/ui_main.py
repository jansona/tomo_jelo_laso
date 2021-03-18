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
        MainWindow.resize(420, 254)
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
        self.secretKey_lineEdit = QLineEdit(self.key_tab)
        self.secretKey_lineEdit.setObjectName(u"secretKey_lineEdit")
        self.secretKey_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.secretKey_lineEdit, 2, 1, 1, 1)

        self.secretVisiable_chBox = QCheckBox(self.key_tab)
        self.secretVisiable_chBox.setObjectName(u"secretVisiable_chBox")

        self.gridLayout.addWidget(self.secretVisiable_chBox, 3, 1, 1, 1)

        self.publicKey_lineEdit = QLineEdit(self.key_tab)
        self.publicKey_lineEdit.setObjectName(u"publicKey_lineEdit")
        self.publicKey_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.publicKey_lineEdit, 0, 1, 1, 1)

        self.secretKey_label = QLabel(self.key_tab)
        self.secretKey_label.setObjectName(u"secretKey_label")

        self.gridLayout.addWidget(self.secretKey_label, 2, 0, 1, 1)

        self.line = QFrame(self.key_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

        self.line_2 = QFrame(self.key_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.publicKey_label = QLabel(self.key_tab)
        self.publicKey_label.setObjectName(u"publicKey_label")

        self.gridLayout.addWidget(self.publicKey_label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.generate_pushBtn = QPushButton(self.key_tab)
        self.generate_pushBtn.setObjectName(u"generate_pushBtn")

        self.verticalLayout.addWidget(self.generate_pushBtn)

        self.tabWidget.addTab(self.key_tab, "")
        self.code_tab = QWidget()
        self.code_tab.setObjectName(u"code_tab")
        self.verticalLayout_3 = QVBoxLayout(self.code_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ratio_groupBox = QGroupBox(self.code_tab)
        self.ratio_groupBox.setObjectName(u"ratio_groupBox")
        self.ratio_groupBox.setStyleSheet(u"")
        self.ratio_groupBox.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.ratio_groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.ratio_groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.encrypt_ratioBtn = QRadioButton(self.ratio_groupBox)
        self.processTypeRatio_buttonGroup = QButtonGroup(MainWindow)
        self.processTypeRatio_buttonGroup.setObjectName(u"processTypeRatio_buttonGroup")
        self.processTypeRatio_buttonGroup.addButton(self.encrypt_ratioBtn)
        self.encrypt_ratioBtn.setObjectName(u"encrypt_ratioBtn")
        self.encrypt_ratioBtn.setEnabled(True)
        self.encrypt_ratioBtn.setChecked(True)

        self.horizontalLayout.addWidget(self.encrypt_ratioBtn)

        self.decrypt_ratioBtn = QRadioButton(self.ratio_groupBox)
        self.processTypeRatio_buttonGroup.addButton(self.decrypt_ratioBtn)
        self.decrypt_ratioBtn.setObjectName(u"decrypt_ratioBtn")

        self.horizontalLayout.addWidget(self.decrypt_ratioBtn)


        self.verticalLayout_3.addWidget(self.ratio_groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.from_label = QLabel(self.code_tab)
        self.from_label.setObjectName(u"from_label")

        self.horizontalLayout_2.addWidget(self.from_label)

        self.fromFilePath_lineEdit = QLineEdit(self.code_tab)
        self.fromFilePath_lineEdit.setObjectName(u"fromFilePath_lineEdit")

        self.horizontalLayout_2.addWidget(self.fromFilePath_lineEdit)

        self.openFromFile_toolBtn = QToolButton(self.code_tab)
        self.openFromFile_toolBtn.setObjectName(u"openFromFile_toolBtn")

        self.horizontalLayout_2.addWidget(self.openFromFile_toolBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.to_label = QLabel(self.code_tab)
        self.to_label.setObjectName(u"to_label")

        self.horizontalLayout_3.addWidget(self.to_label)

        self.toFilePath_lineEdit = QLineEdit(self.code_tab)
        self.toFilePath_lineEdit.setObjectName(u"toFilePath_lineEdit")

        self.horizontalLayout_3.addWidget(self.toFilePath_lineEdit)

        self.openToFile_toolButton = QToolButton(self.code_tab)
        self.openToFile_toolButton.setObjectName(u"openToFile_toolButton")

        self.horizontalLayout_3.addWidget(self.openToFile_toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.key_label = QLabel(self.code_tab)
        self.key_label.setObjectName(u"key_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.key_label)

        self.key_lineEdit = QLineEdit(self.code_tab)
        self.key_lineEdit.setObjectName(u"key_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.key_lineEdit)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.process_pushBtn = QPushButton(self.code_tab)
        self.process_pushBtn.setObjectName(u"process_pushBtn")

        self.verticalLayout_3.addWidget(self.process_pushBtn)

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
        self.secretVisiable_chBox.setText(QCoreApplication.translate("MainWindow", u"secret key visiable", None))
        self.secretKey_label.setText(QCoreApplication.translate("MainWindow", u"Secret Key:", None))
        self.publicKey_label.setText(QCoreApplication.translate("MainWindow", u"Public Key:", None))
        self.generate_pushBtn.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.key_tab), QCoreApplication.translate("MainWindow", u"key generation", None))
        self.ratio_groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"*Action:", None))
        self.encrypt_ratioBtn.setText(QCoreApplication.translate("MainWindow", u"encrypt", None))
        self.decrypt_ratioBtn.setText(QCoreApplication.translate("MainWindow", u"decrypt", None))
        self.from_label.setText(QCoreApplication.translate("MainWindow", u"From(File):", None))
        self.openFromFile_toolBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.to_label.setText(QCoreApplication.translate("MainWindow", u"To(Dir):", None))
        self.openToFile_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"Public Key:", None))
        self.process_pushBtn.setText(QCoreApplication.translate("MainWindow", u"PROCESS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.code_tab), QCoreApplication.translate("MainWindow", u"encrypt/decrypt", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

