from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow, QApplication

import sys
from gui.MainWindow import MainWindow
from gui.ui_main import Ui_MainWindow
from encode_decode.simple_rsa import RSA


BIT_WIDTH = 16
SUFFIX_NAME = ".tjl"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow(BIT_WIDTH, SUFFIX_NAME)
    ex.show()
    app.exec_()
