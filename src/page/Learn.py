#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the learning Pages
"""

from PyQt6.QtWidgets import QHBoxLayout, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from src.component.Form import Form
from src.component.Title import Title
from src.utils.RandomLetter import getRandomLetter

list = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

class learnCharacter(QWidget):
    def __init__(self):
        super().__init__()

        self.letter = getRandomLetter()

        page = QVBoxLayout()

        self.setLayout(page)

        self.charDisplay = Title(self.letter, None, 100)

        self.answer = Form()
        self.answer.setMaximumSize(100, 30)
        self.answer.enterPressed.connect(self.testValidity)

        answerWrapper = QHBoxLayout()
        answerWrapper.addStretch()
        answerWrapper.addWidget(self.answer)
        answerWrapper.addStretch()

        self.button = QPushButton("Valider")
        self.button.clicked.connect(self.testValidity)

        buttonWrapper = QHBoxLayout()
        buttonWrapper.addStretch()
        buttonWrapper.addWidget(self.button)
        buttonWrapper.addStretch()

        page.addStretch()
        page.addLayout(self.charDisplay)
        page.addStretch()
        page.addLayout(answerWrapper)
        page.addStretch()
        page.addLayout(buttonWrapper)
        page.addStretch()

        self.wrong = 0
        
    def testValidity(self):
        if (list.get(self.answer.getValue(), '') == self.letter):
            self.wrong = 0
            self.answer.setStyleSheet("background-color: GREEN;")
            self.button.setText("Next")
            self.button.clicked.disconnect()
            self.answer.enterPressed.disconnect()
            self.button.clicked.connect(self.next)
            self.answer.enterPressed.connect(self.next)
        else:
            if self.wrong >= 2:
                self.answer.setValue(list.get(self.letter, ''))
                self.answer.setStyleSheet("background-color: YELLOW;")
            else:
                self.wrong += 1
                self.answer.setStyleSheet("background-color: RED;")
    
    def next(self):
        self.letter = getRandomLetter()
        self.charDisplay.update(self.letter)
        self.answer.setStyleSheet("")
        self.answer.setValue("")
        self.button.setText("Valider")
        self.button.clicked.disconnect()
        self.answer.enterPressed.disconnect()
        self.button.clicked.connect(self.testValidity)
        self.answer.enterPressed.connect(self.testValidity)

                 
              




