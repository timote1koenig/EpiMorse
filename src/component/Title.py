#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Title class
"""

from PyQt6.QtWidgets import QLabel, QHBoxLayout


class Title(QHBoxLayout):
    def __init__(self, text, color = "Black"):
        super().__init__()

        title = QLabel(text)

        title.setStyleSheet(f"color: {color};")
        
        self.addStretch()
        self.addWidget(title)
        self.addStretch()
