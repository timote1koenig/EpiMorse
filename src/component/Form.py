#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Form class
"""

from PyQt6.QtWidgets import QLineEdit, QVBoxLayout, QWidget

class Form(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.edit = QLineEdit()

        self.edit.setMinimumHeight(150)
        self.edit.setMinimumWidth(150)
        self.edit.setMaximumHeight(800)
        self.edit.setMaximumWidth(800)
        
        layout = QVBoxLayout()
        layout.addWidget(self.edit)

        self.setLayout(layout)

    def getValue(self):
        return self.edit.text()

    def setValue(self, value):
        self.edit.setText(value)


