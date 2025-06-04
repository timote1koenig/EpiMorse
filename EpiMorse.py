#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the main who managed EpiMorse
"""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QGridLayout, QWidget
from PyQt6.QtCore import Qt
from src.Window import Window
from src.page.MainMenu import MainMenu
from src.Header import Header

def Menu():
    app = QApplication([])

    window = Window()

    content = QWidget()
    window.setCentralWidget(content)

    layout = QGridLayout()
    content.setLayout(layout)

    header = Header()

    main = MainMenu()

    layout.addWidget(header, 0, 0, 1, 2)
    layout.addWidget(main, 1, 0)

    layout.setRowStretch(1, 1)

    layout.setContentsMargins(0, 0, 0, 0)

    window.show()
    app.exec()
    return 0


if __name__ == "__main__":
    sys.exit(Menu())

