#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the main who managed EpiMorse
"""

import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from object.Window import Window

if __name__ == "__main__":
    app = QApplication([])
    
    window = Window()
    window.show()

    app.exec()  
