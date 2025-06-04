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

        wrapper = QVBoxLayout()
        self.setLayout(wrapper)
        
        coloredArea = QWidget()
        wrapper.addWidget(coloredArea)

        content = QVBoxLayout()
        coloredArea.setLayout(content)


        titleSection = QHBoxLayout()
        content.addLayout(titleSection)

        title = QLabel("EpiMorse")

        title.setStyleSheet("color: White")

        titleSection.addStretch()
        titleSection.addWidget(title)
        titleSection.addStretch()
        

        navigation = QHBoxLayout()
        content.addLayout(navigation)

        button1 = QPushButton("Traduction")
        button2 = QPushButton("Apprendre")
        button3 = QPushButton("Dictionnaire")

        button1.setStyleSheet("background-color: PowderBlue")
        button2.setStyleSheet("background-color: PowderBlue")
        button3.setStyleSheet("background-color: PowderBlue")

        navigation.addWidget(button1)
        navigation.addWidget(button2)
        navigation.addWidget(button3)


        coloredArea.setStyleSheet("background-color: DarkBlue;")

        wrapper.setContentsMargins(0, 0, 0, 0)

