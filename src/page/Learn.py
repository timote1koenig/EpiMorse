#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the learning Pages
"""

import random
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QPushButton, QVBoxLayout
from src.component.Form import Form
from src.component.Title import Title
from src.page.Translate import toMorse, toLetter

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
    def __init__(self, function):
        super().__init__()

        self.random = function

        self.letter = self.random()

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
        value = list.get(self.answer.getValue().upper(), '')
        if (value == self.letter):
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
        self.letter = self.random()
        self.charDisplay.update(self.letter)
        self.answer.setStyleSheet("")
        self.answer.setValue("")
        self.button.setText("Valider")
        self.button.clicked.disconnect()
        self.answer.enterPressed.disconnect()
        self.button.clicked.connect(self.testValidity)
        self.answer.enterPressed.connect(self.testValidity)

textSentence = [
"Le code source est heberge sur GitHub",
"Python est un langage tres apprecie pour l intelligence artificielle",
"Une boucle infinie peut faire planter ton programme",
"Il a debogue l application toute la nuit",
"La fonction renvoie une erreur 500 sur le serveur",
"Le backend communique avec une base de donnees PostgreSQL",
"Le frontend utilise React pour afficher l interface",
"On utilise des API REST pour echanger les donnees",
"Ce framework facilite le developpement web",
"Le projet est containerise avec Docker",
"Le mot de passe doit contenir au moins huit caracteres",
"La connexion est securisee par un certificat SSL",
"Il a lance un scan de ports sur le reseau",
"L attaque a ete bloquee par le pare feu",
"Le systeme utilise une authentification a deux facteurs",
"L adresse IP du client est dynamique",
"Le trafic reseau est surveille en temps reel",
"Une faille XSS a ete detectee dans le formulaire",
"Le chiffrement RSA protege les communications",
"Les logs montrent une tentative d intrusion",
"L algorithme de machine learning predit le comportement des utilisateurs",
"Le modele a ete entraine sur un jeu de donnees massif",
"La reconnaissance vocale fonctionne en temps reel",
"Le reseau de neurones converge apres plusieurs epoques",
"Les donnees sont nettoyees avant l analyse",
"Le chatbot repond avec des phrases naturelles",
"Les resultats sont visualises avec des graphiques interactifs",
"L IA classe les images automatiquement",
"Il utilise GPT pour generer du texte",
"Le modele detecte les anomalies dans les transactions",
"Le microcontroleur pilote les capteurs",
"La carte mere a ete changee pour plus de performance",
"L imprimante 3D fabrique des prototypes en plastique",
"Le robot evite les obstacles avec un lidar",
"L objet connecte transmet les donnees via Bluetooth",
"Le drone est stabilise par un gyroscope",
"Le SSD est bien plus rapide qu un disque dur classique",
"L ecran tactile supporte dix points de contact",
"Le cloud permet d acceder a ses fichiers partout",
"Le teletravail a accelere la transformation numerique",
"La blockchain garantit la tracabilite des echanges",
"Le metavers fascine autant qu il inquiete",
"Les startups innovent dans tous les domaines",
"Le streaming a remplace les DVD",
"Les notifications envahissent notre quotidien",
"L obsolescence programmee est un vrai debat",
"Les donnees personnelles sont devenues une monnaie",
"Le numerique transforme nos modes de vie"
]

class learnText(QWidget):
    def __init__(self, writeMorse):
        super().__init__()
        page = QVBoxLayout()
        forms = QHBoxLayout()

        leftSection = QVBoxLayout()
        self.srcForm = Form(30)
        leftSection.addLayout(Title("Écrire ici"))
        leftSection.addWidget(self.srcForm)

        rightSection = QVBoxLayout()
        self.destForm = Form(30)
        rightSection.addLayout(Title("Objectif"))
        rightSection.addWidget(self.destForm)

        forms.addLayout(leftSection)
        forms.addLayout(rightSection)

        buttonSection = QHBoxLayout()
        button = QPushButton("Valider")
        buttonSection.addWidget(button)

        page.addLayout(forms)
        page.addLayout(buttonSection)

        self.setLayout(page)

        button.clicked.connect(self.testValidity)

        self.writeMorse = writeMorse

        self.text = random.choice(textSentence)

        self.__nextSentence()


    def testValidity(self):
        print (toLetter(self.srcForm.getValue()).upper())
        if self.writeMorse:
            if toLetter(self.srcForm.getValue()).upper() == self.text.upper():
                self.__nextSentence()
            else:
                self.srcForm.setStyleSheet("background-color: RED;")
        else:
            if self.srcForm.getValue().upper() == self.text.upper():
                self.__nextSentence()
            else:
                self.srcForm.setStyleSheet("background-color: RED;")

    def __nextSentence(self):

        self.text = random.choice(textSentence)

        if self.srcForm.getValue:
            self.srcForm.setValue("")
        
        self.srcForm.setStyleSheet("")


        if self.writeMorse:
            self.destForm.setValue(self.text)
        else:
            self.destForm.setValue(toMorse(self.text).replace("  ", " |"))


