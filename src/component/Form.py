#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Form class
"""

from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtGui import QTextCursor


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.edit = QTextEdit()
        self.edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

    def getValue(self):
        return self.edit.toPlainText()

    def setValue(self, value):
        self.edit.setText(value)


