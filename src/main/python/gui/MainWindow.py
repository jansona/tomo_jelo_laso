from threading import Thread

from PySide2 import QtCore
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader

import sys, os, base64
from .ui_main import Ui_MainWindow
from encode_decode.simple_rsa import RSA
from utils.file_processor import conduct_file_processed


class ProcessThread(Thread):

    def __init__(self, source_file_path, target_file_path, e_or_d, n, bit_width, does_encrypt, signal):
        super().__init__()
        self.source_file_path = source_file_path
        self.target_file_path = target_file_path
        self.n = n
        self.e_or_d = e_or_d
        self.bit_width = bit_width
        self.does_encrypt = does_encrypt
        self.signal = signal

    def run(self):
        # 进行任务操作
        conduct_file_processed(self.source_file_path, self.target_file_path,
                               self.e_or_d, self.n, self.bit_width, self.does_encrypt, self.signal)


class MainWindow(QMainWindow):

    _process_signal = QtCore.Signal(float)

    def __init__(self, bit_width, suffix_name):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.rsa = RSA()
        self.bit_width = bit_width
        self.suffix_name = suffix_name
        self.public_key = None
        self.secret_key = None

        self.ui.secretVisiable_chBox.clicked.connect(self.show_keys)
        self.ui.generate_pushBtn.clicked.connect(self.handle_generate)

        self.ui.openFile_toolBtn.clicked.connect(self.open_file)
        self.ui.processTypeRatio_buttonGroup.buttonToggled.connect(self.switch_process_key_label)
        self.ui.process_pushBtn.clicked.connect(self.handle_process)

        self._process_signal.connect(self.handle_process_status)

    def handle_generate(self):

        self.rsa.generate_key(self.bit_width)
        self.show_keys()

    def show_keys(self):

        if self.rsa.n is not None and self.rsa.e is not None:
            public_key_plaintext = "{}-{}".format(self.rsa.n, self.rsa.e)
            self.public_key = base64.b64encode(public_key_plaintext.encode("utf-8"))
            self.ui.publicKey_lineEdit.setText(self.public_key.decode("utf-8"))

        if self.rsa.n is not None and self.rsa.d is not None:
            if self.ui.secretVisiable_chBox.checkState():
                secret_key_plaintext = "{}-{}".format(self.rsa.n, self.rsa.d)
                self.secret_key = base64.b64encode(secret_key_plaintext.encode("utf-8"))
                self.ui.secretKey_lineEdit.setText(self.secret_key.decode("utf-8"))
            else:
                self.ui.secretKey_lineEdit.setText('*' * 6)

    def handle_process(self):

        # check the input is empty
        def handle_content_missing(content, message, title="Necessary Content Missing"):
            if content is None or content is "":
                QMessageBox().critical(self, title, message)
                return False
            return True

        source_file_path = self.ui.filePath_lineEdit.text()
        key_content = self.ui.key_lineEdit.text()

        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encode":
            key_missing_message = "Please input the public key."
        else:
            key_missing_message = "Please input the secret key."

        for content, message in [(source_file_path, "Please input/select the valid path of file."),
                                 (key_content, key_missing_message)]:
            if not handle_content_missing(content, message):
                return

        # check the input is valid
        if not os.path.exists(source_file_path):
            QMessageBox().critical(self, "File Not Exists", "Please input the right path of file.")

        # parse key
        key_pair_str = base64.b64decode(key_content).decode("utf-8")
        n_str, e_or_d_str = key_pair_str.split("-")
        n = int(n_str)
        e_or_d = int(e_or_d_str)
        print(n, e_or_d)

        # process
        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encrypt":
            print("encrypt")
            target_file_path = source_file_path + self.suffix_name
            read_bit_width = self.bit_width // 2
            does_encrypt = True
        else:
            print("decrypt")
            target_file_path = ".".join(source_file_path.split(".")[:-1])
            read_bit_width = self.bit_width
            does_encrypt = False

        process_thread = ProcessThread(source_file_path, target_file_path, e_or_d, n,
                                       read_bit_width, does_encrypt, self._process_signal)
        process_thread.start()
        self.ui.process_pushBtn.setDisabled(True)

    def open_file(self):

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            self.ui.filePath_lineEdit.setText(file_names[0])

    def switch_process_key_label(self):

        if self.ui.processTypeRatio_buttonGroup.checkedButton().text() == "encrypt":
            self.ui.key_label.setText("Public Key:")
        else:
            self.ui.key_label.setText("Secret Key:")

    def handle_process_status(self, ratio):

        if ratio >= 0:
            self.ui.process_pushBtn.setText("{:.1f}%".format(ratio * 100))
        else:
            QMessageBox.information(self, "DONE!", "Process Finish.")
            self.ui.process_pushBtn.setText("PROCESS")
            self.ui.process_pushBtn.setEnabled(True)
