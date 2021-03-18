from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow, QApplication

import sys
from gui.MainWindow import MainWindow


KEY_BIT_WIDTH = 16
SUFFIX_NAME = ".tjl"

if __name__ == '__main__':
    appctxt = ApplicationContext()
    ex = MainWindow(KEY_BIT_WIDTH, SUFFIX_NAME)
    ex.show()
    sys.exit(appctxt.app.exec_())
