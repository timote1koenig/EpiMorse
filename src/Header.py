#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Header class
"""

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from src.component.Title import Title

class Header(QWidget):

    def __init__(self):
        super().__init__()

        wrapper = QVBoxLayout()
        self.setLayout(wrapper)
        
        coloredArea = QWidget()
        wrapper.addWidget(coloredArea)

        content = QVBoxLayout()
        coloredArea.setLayout(content)


        titleSection = Title("EpiMorse", "White", 50)
        content.addLayout(titleSection)
        

        navigation = QHBoxLayout()
        content.addLayout(navigation)

        self.button1 = QPushButton("Traduction")
        self.button2 = QPushButton("Apprendre")
        self.button3 = QPushButton("Dictionnaire")

        self.button1.setStyleSheet("background-color: PowderBlue")
        self.button2.setStyleSheet("background-color: PowderBlue")
        self.button3.setStyleSheet("background-color: PowderBlue")

        navigation.addWidget(self.button1)
        navigation.addWidget(self.button2)
        navigation.addWidget(self.button3)


        coloredArea.setStyleSheet("background-color: DarkBlue;")

        wrapper.setContentsMargins(0, 0, 0, 0)
    
    def connectButtonOne(self, command):
        self.button1.clicked.connect(command)

    def connectButtonTwo(self, command):
        self.button2.clicked.connect(command)
    
    def connectButtonThree(self, command):
        self.button3.clicked.connect(command)
