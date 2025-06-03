#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Header class
"""

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt

class Header(QWidget):

    def __init__(self):
        super().__init__()

        content = QVBoxLayout()
        titleSection = QHBoxLayout()
        navigation = QHBoxLayout()

        content.addLayout(titleSection)
        content.addLayout(navigation)

        title = QLabel("EpiMorse")

        titleSection.addStretch()
        titleSection.addWidget(title)
        titleSection.addStretch()

        button1 = QPushButton()
        button2 = QPushButton()
        button3 = QPushButton()

        navigation.addWidget(button1)
        navigation.addWidget(button2)
        navigation.addWidget(button3)

        self.setLayout(content)