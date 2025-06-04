#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the MainMenu class
"""

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from src.component.Form import Form

class MainMenu(QWidget):

    def __init__(self):
        super().__init__()

        forms = QHBoxLayout()

        leftSection = QVBoxLayout

        rightForm = Form()
        leftForm = Form()

        forms.addWidget(rightForm)
        forms.addWidget(leftForm)

        self.setLayout(forms)
