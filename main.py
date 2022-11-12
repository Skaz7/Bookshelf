from settings import database_exist_check, connect_to_database
from time import sleep
from ui_mainscreen import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import sys
import pytest


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    connect_to_database()
    sys.exit(app.exec())


if __name__ == '__main__':
    if database_exist_check():
        main()
    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
