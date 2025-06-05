#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Translate Page
"""

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from src.component.Form import Form
from src.component.Title import Title
from src.page.Dictionnary import fromMorse, fromLetter

class Translate(QWidget):

    def __init__(self):
        super().__init__()

        page = QHBoxLayout()

        leftSection = QVBoxLayout()
        self.srcForm = Form()
        leftSection.addLayout(Title("Texte"))
        leftSection.addWidget(self.srcForm)

        rightSection = QVBoxLayout()
        self.destForm = Form()
        rightSection.addLayout(Title("Morse"))
        rightSection.addWidget(self.destForm)

        page.addLayout(leftSection)
        page.addLayout(rightSection)
        self.setLayout(page)

        self.srcForm.edit.textChanged.connect(self.src_changed)
        self.destForm.edit.textChanged.connect(self.dest_changed)

        self.updating = False

    def src_changed(self):
        if self.updating:
            return
        self.updating = True
        self.destForm.setValue(toLetter(self.srcForm.getValue()))
        self.updating = False

    def dest_changed(self):
        if self.updating:
            return
        self.updating = True
        self.srcForm.setValue(toMorse(self.destForm.getValue()))
        self.updating = False

def is_morse(s):
    allowed = {'.', '-', ' '}
    return all(c in allowed for c in s.strip()) and any(c in '.-' for c in s)


def toMorse(text):
    text = text.strip().replace("  ", " / ")
    symbols = text.split()

    result = []
    for symbol in symbols:
        if symbol == '/':
            result.append(' ')
        else:
            result.append(fromMorse.get(symbol, ''))
    return ''.join(result)

def toLetter(text):
    return ''.join(fromLetter.get(char, '') for char in text)

