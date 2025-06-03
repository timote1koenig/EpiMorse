#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the MainMenu class
"""

from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QFont
from component.Form import Form

class MainMenu(QWidget):

    def __init__(self):
        super().__init__()
        form = Form()
        second_form = Form()

        title = QLabel("EpiMorse")
        title.setStyleSheet("font-size: 30px;")

        main_layout = QVBoxLayout()
        top_row = QHBoxLayout()
        middle_row = QHBoxLayout()
        down_row = QHBoxLayout()

        top_row.addStretch()
        top_row.addWidget(title)
        top_row.addStretch()

        middle_row.addWidget(form)

        down_row.addWidget(second_form)

        main_layout.addLayout(top_row)
        main_layout.addStretch()
        main_layout.addLayout(middle_row)
        main_layout.addStretch()
        main_layout.addLayout(down_row)
        main_layout.addStretch()

        self.setLayout(main_layout)
