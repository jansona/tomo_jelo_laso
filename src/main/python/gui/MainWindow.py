from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtUiTools import QUiLoader

import sys
from .ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
