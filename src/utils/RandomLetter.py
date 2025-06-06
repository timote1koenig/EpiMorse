#!/usr/bin/env python3
"""
Filename: EpiMorse.py
Author: Timoté Koenig
Date: 22/05/2025
Version: 1.0
Description: This is the random function used to learn morse
"""

import random
import string

weights = {l: 1.0 for l in string.ascii_uppercase}

compteur = {l: 0 for l in string.ascii_uppercase}

conditions = {
    'Z': {'Q': 2, 'Y': 2},
    'Q': {'C': 2, 'J': 2},
    'Y': {'C': 2, 'J': 2},
    'C': {'X': 2, 'P': 2},
    'J': {'X': 2, 'P': 2},
    'X': {'F': 2, 'L': 2},
    'P': {'F': 2, 'L': 2},
    'F': {'B': 2, 'V': 2},
    'L': {'B': 2, 'V': 2},
    'B': {'H': 2},
    'V': {'H': 2},
    'H': {'W': 2, 'G': 2},
    'W': {'K': 2, 'D': 2},
    'G': {'K': 2, 'D': 2},
    'R': {'U': 2, 'D': 2},
    'K': {'U': 2, 'D': 2},
    'D': {'O': 2, 'S': 2},
    'U': {'O': 2, 'S': 2},
    'O': {'A': 2, 'N': 2},
    'S': {'A': 2, 'N': 2},
    'A': {'I': 2, 'M': 2},
    'N': {'I': 2, 'M': 2},
    'I': {'E': 2, 'T': 2},
    'M': {'E': 2, 'T': 2},
}

def est_debloquee(lettre, compteur, conditions):
    if lettre not in conditions:
        return True  # Pas de condition : toujours débloquée
    for lettre_requise, nb_min in conditions[lettre].items():
        if compteur[lettre_requise] < nb_min:
            return False
    return True

def tirage_pondéré(weights, compteur, conditions):
    total = 0
    lettres_disponibles = []
    poids_effectifs = []

    for l in weights:
        if est_debloquee(l, compteur, conditions):
            lettres_disponibles.append(l)
            poids_effectifs.append(weights[l])
            total += weights[l]

    if not lettres_disponibles:
        raise ValueError("Aucune lettre disponible selon les conditions.")

    return random.choices(lettres_disponibles, weights=poids_effectifs, k=1)[0]

def mise_a_jour_weights(weights, lettre_tirée, taux_diminution=0.1):
    poids_perdu = weights[lettre_tirée] * taux_diminution
    weights[lettre_tirée] -= poids_perdu
    gain_par_autre = poids_perdu / (len(weights) - 1)
    for l in weights:
        if l != lettre_tirée:
            weights[l] += gain_par_autre

def getRandomLetter():

    l = tirage_pondéré(weights, compteur, conditions)
    compteur[l] += 1
    mise_a_jour_weights(weights, l)

    return l

