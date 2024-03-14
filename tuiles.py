import random
from PyQt5.QtCore import QRect

class SacDeLettres:
    def __init__(self):
        self.lettres = self.initialiser_lettres()

    def initialiser_lettres(self):
        # Crée une liste de lettres basée sur la quantité de chaque lettre
        sac = []
        letters = [
           
        {'letter':'A', 'quantity': 9, 'value': 1},
        {'letter':'B', 'quantity': 2, 'value': 3},
        {'letter':'C', 'quantity': 2, 'value': 3},
        {'letter':'D', 'quantity': 4, 'value': 2},
        {'letter':'E', 'quantity': 12, 'value': 1},
        {'letter':'F', 'quantity': 2, 'value': 4},
        {'letter':'G', 'quantity': 3, 'value': 2},
        {'letter':'H', 'quantity': 2,'value': 4},
        {'letter':'I', 'quantity': 9, 'value': 1},
        {'letter':'J','quantity': 1, 'value': 8},
        {'letter':'K', 'quantity': 1, 'value': 5},
        {'letter':'L', 'quantity': 4,'value': 1},
        {'letter':'M','quantity': 2, 'value': 3},
        {'letter':'N', 'quantity':6, 'value': 1},
        {'letter':'O','quantity': 8, 'value': 1},
        {'letter':'P','quantity':2, 'value': 3},
        {'letter':'Q','quantity': 1, 'value': 10},
        {'letter':'R','quantity': 6, 'value': 1},
        {'letter':'S','quantity': 4, 'value': 1},
        {'letter':'T', 'quantity': 6, 'value': 1},
        {'letter':'U','quantity': 4, 'value': 1},
        {'letter':'V','quantity': 2, 'value': 4},
        {'letter':'W','quantity': 2, 'value': 4},
        {'letter':'X','quantity': 1, 'value': 8},
        {'letter':'Y','quantity': 2, 'value': 4},
        {'letter':'Z','quantity': 1, 'value': 10},
        {'letter':'?', 'quantity':2, 'value': 0}  # Joker avec une valeur de 0
        
        ]
        for letter_info in letters:
            for _ in range(letter_info['quantity']):
                sac.append({'letter': letter_info['letter'], 'value': letter_info['value']})
        random.shuffle(sac)  # Mélange le sac de lettres pour le tirage aléatoire
        return sac

    def tirer_lettres(self, nombre):
        # Tire un nombre spécifié de lettres du sac
        tirage = self.lettres[:nombre]
        self.lettres = self.lettres[nombre:]
        return tirage

    def remettre_lettres(self, lettres):
        # Ajoute les lettres spécifiées dans le sac et mélange à nouveau
        self.lettres.extend(lettres)
        random.shuffle(self.lettres)


    def obtenir_valeur_lettre(lettre):
        # Imaginons que vous avez un dictionnaire global ou une structure similaire pour stocker ces valeurs
        valeurs = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
            'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
            'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
            'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
            'Z': 10, '?': 0
        }
        return valeurs.get(lettre, 0)  # Retourne la valeur de la lettre, 0 si non trouvée

# tuiles.py
class Tuile:
    def __init__(self, lettre, valeur, couleur_fond='blue', couleur_texte='yellow', position=(0, 0), size=(40, 40), gelee = False):
        self.lettre = lettre
        self.valeur = valeur
        self.couleur_fond = couleur_fond
        self.couleur_texte = couleur_texte
        self.position = position
        self.size = size
        self.gelée = gelee  # État de la tuile (True = gelée, False = non gelée)

    def rect(self):
        return QRect(self.position[0], self.position[1], self.size[0], self.size[1])


    def setPosition(self, position):
        self.position = position

    def geler(self):
        # Méthode pour geler la tuile
        self.gelée = True
        self.couleur_fond = 'grey'  # Change la couleur pour indiquer qu'elle est gelée