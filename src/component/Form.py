#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Form class
"""

from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal


class Form(QWidget):
    enterPressed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.edit = QTextEdit()
        self.edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

        self.edit.installEventFilter(self)

    def getValue(self):
        return self.edit.toPlainText()

    def setValue(self, value):
        self.edit.setText(value)

    def eventFilter(self, source, event):
        if source == self.edit and event.type() == event.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                self.enterPressed.emit()
                return True
        return super().eventFilter(source, event)
