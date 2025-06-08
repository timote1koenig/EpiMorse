#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the file for the Stack command
"""

from PyQt6.QtWidgets import QStackedWidget
from src.page.Learn import learnCharacter, learnText
from src.page.Translate import Translate
from src.utils.RandomLetter import getRandomLetter, getRandomMorse


class Stack(QStackedWidget):
    
    def __init__(self):
        super().__init__()

        self.learnCharMorse = learnCharacter(getRandomMorse) # write letter
        self.learnCharLetter = learnCharacter(getRandomLetter) # write morse
        self.learnTextMorse = learnText(True) # write morse ?
        self.learnTextLetter = learnText(False) # write letter
        self.translate = Translate()

        self.addWidget(self.learnCharMorse)
        self.addWidget(self.learnCharLetter)
        self.addWidget(self.learnTextMorse)
        self.addWidget(self.learnTextLetter)
        self.addWidget(self.translate)

    def setTranslate(self):
        self.setCurrentWidget(self.translate)
    
    def setLearnCharMorse(self):
        self.setCurrentWidget(self.learnCharMorse)