#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the main who managed EpiMorse
"""

import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QStackedWidget
from src.Window import Window
from src.Header import Header
from src.component.Stack import Stack

def Menu():
    app = QApplication([])

    window = Window()

    content = QWidget()
    window.setCentralWidget(content)

    
    layout = QGridLayout()
    content.setLayout(layout)

    header = Header()

    stack = Stack()
    
    header.connectButtonOne(stack.setTranslate)
    header.connectButtonTwo(stack.setLearnCharMorse)


    layout.addWidget(header, 0, 0)
    layout.addWidget(stack, 1, 0)

    layout.setRowStretch(0, 3)
    layout.setRowStretch(1, 20)

    layout.setContentsMargins(0, 0, 0, 0)

    window.show()
    app.exec()
    return 0


if __name__ == "__main__":
    sys.exit(Menu())

