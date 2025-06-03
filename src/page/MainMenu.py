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
from src.component.Form import Form

class MainMenu(QWidget):

    def __init__(self):
        super().__init__()
        form = Form()
        second_form = Form()


        main_layout = QHBoxLayout()

        main_layout.addWidget(form)
        main_layout.addWidget(second_form)

        self.setLayout(main_layout)
