# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    status_bar = QStatusBar()
    line_edit

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        label = QLabel("button", self)
        label.move(20, 60)

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

        # myWindow.line_edit.move(20, 100)
        self.line_edit.move(20, 100)
        self.line_edit.textChanged.connect(self.line_edit_change)

        self.setStatusBar(self.status_bar)

    def line_edit_change(self):
        self.status_bar.showMessage(self.line_edit.text())

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
