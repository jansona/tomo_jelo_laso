from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader

import sys, os
from .ui_main import Ui_MainWindow
from encode_decode.simple_rsa import RSA
from utils.file_processor import conduct_file_encoded, conduct_file_decoded


class MainWindow(QMainWindow):

    def __init__(self, bit_width, suffix_name):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.rsa = RSA()
        self.bit_width = bit_width
        self.suffix_name = suffix_name

        self.ui.secretVisiable_chBox.clicked.connect(self.show_keys)
        self.ui.generate_pushBtn.clicked.connect(self.handle_generate)

        self.ui.openFile_ToolBtn.clicked.connect(self.open_file)
        self.ui.processTypeRatio_buttonGroup.buttonToggled.connect(self.switch_process_key_label)
        self.ui.process_pushBtn.clicked.connect(self.handle_process)

    def handle_generate(self):

        self.rsa.generate_key(self.bit_width)
        self.show_keys()

    def show_keys(self):

        if self.rsa.n is not None and self.rsa.e is not None:
            self.ui.n_lineEdit.setText(str(self.rsa.n))

        if self.rsa.e is not None:
            self.ui.e_lineEdit.setText(str(self.rsa.e))

        if self.rsa.d is not None:
            if self.ui.secretVisiable_chBox.checkState():
                self.ui.d_lineEdit.setText(str(self.rsa.d))
            else:
                self.ui.d_lineEdit.setText('*' * 6)

    def handle_process(self):

        # check the input is empty
        def handle_content_missing(content, message, title="Necessary Content Missing"):
            if content is None or content is "":
                QMessageBox().critical(self, title, message)
                return False
            return True

        source_file_path = self.ui.filePath_lineEdit.text()
        n_process_content = self.ui.n_process_lineEdit.text()
        key_content = self.ui.key_lineEdit.text()

        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encode":
            key_missing_message = "Please input the public key e."
        else:
            key_missing_message = "Please input the secret key d."

        for content, message in [(source_file_path, "Please input/select the valid path of file."),
                                 (n_process_content, "Please input the public number n."),
                                 (key_content, key_missing_message)]:
            if not handle_content_missing(content, message):
                return

        # check the input is valid
        if not os.path.exists(source_file_path):
            QMessageBox().critical(self, "File Not Exists", "Please input the right path of file.")

        n_process = int(n_process_content)
        key = int(key_content)

        # process
        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encode":
            target_file_path = source_file_path + self.suffix_name
            conduct_file_encoded(source_file_path, target_file_path, key, n_process, self.bit_width // 2)
        else:
            target_file_path = ".".join(source_file_path.split(".")[:-1])
            conduct_file_decoded(source_file_path, target_file_path, key, n_process, self.bit_width)

    def open_file(self):

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            self.ui.filePath_lineEdit.setText(file_names[0])

    def switch_process_key_label(self):

        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encode":
            self.ui.key_label.setText("Public Key E:")
        else:
            self.ui.key_label.setText("Secret Key D:")
