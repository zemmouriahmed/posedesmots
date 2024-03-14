# button.py
from PyQt5.QtWidgets import QPushButton

class ValiderButton:
    def __init__(self, parent):
        self.button = QPushButton('Valider', parent)
        self.button.setGeometry(280, 600, 320, 40)  # Positionne le bouton
        self.button.clicked.connect(self.valider_action)

        # Définir la couleur de fond du bouton à rouge
        self.button.setStyleSheet("background-color: red;")

    def valider_action(self):
        # Définir les actions à effectuer lors du clic sur le bouton
        print("Validation en cours...")  # Placeholder pour l'action





    def show(self):
        self.button.show()
