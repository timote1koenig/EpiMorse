#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the Window class
"""

from PyQt6.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window from another file")
        self.resize(1920, 1080)
        