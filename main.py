from dbfunctions import database_exist_check, create_connection
from settings import *
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
    """Functions that creates main application window and establishes connection to database."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    create_connection(database_file)
    sys.exit(app.exec())


if __name__ == '__main__':
    if database_exist_check(database_file):
        main()
    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
