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
    def __init__(self, text, color = "Black", size = 14):
        super().__init__()

        self.title = QLabel(text)

        self.title.setStyleSheet(f"color: {color}; font-size: {size}px;")
        
        self.addStretch()
        self.addWidget(self.title)
        self.addStretch()
    
    def update(self, text):
        self.title.setText(text)
