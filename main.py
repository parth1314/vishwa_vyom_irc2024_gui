#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from cam_feed import Ui_MainWindow  # Import the generated UI class
import subprocess
import sys

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Add your application logic here

        self.pushButton.clicked.connect(self.launch_py_file)

    def launch_py_file(self):
        py_file_path = './image_s.py'
        try:
            # Launch the .py file using subprocess
            subprocess.Popen(['python3', py_file_path])
        except Exception as e:
            print(f"Error launching .py file: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
