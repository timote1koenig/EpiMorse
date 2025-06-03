#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the main who managed EpiMorse
"""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from src.Window import Window
from src.page.MainMenu import MainMenu
from src.Header import Header

def Menu():
    app = QApplication([])

    window = Window()

    header = Header()

    page = MainMenu()


    window.setCentralWidget(container)

    window.show()
    app.exec()
    return 0


if __name__ == "__main__":
    sys.exit(Menu())

