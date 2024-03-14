from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from PyQt5.QtCore import QSize, Qt
from tuiles import SacDeLettres  # Assurez-vous que tuiles.py est accessible
from button import ValiderButton  # Importez la nouvelle classe
from tuiles import Tuile, SacDeLettres
from mouse import MouseHandler
from regles import ReglesScrabble

class GrilleScrabbleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grille de Scrabble")
        self.setFixedSize(QSize(600, 640))  # Dimension pour grille + chevalet
        self.sac = SacDeLettres()  # Initialisation du sac de lettres
        lettres_tirees = self.sac.tirer_lettres(7)
        self.chevalet = [Tuile(lettre['letter'], lettre['value'], position=(j * 40, 600)) for j, lettre in enumerate(lettres_tirees)]
        
        # Instancie la classe ValiderButton
        self.valider_button = ValiderButton(self)
        self.valider_button.show()  # Affiche le bouton
        
        self.mouse_handler = MouseHandler(self, self.chevalet)

        # Initialiser les règles avec le sac de lettres
        self.regles = ReglesScrabble(self.sac)
        self.valider_button.button.clicked.connect(self.on_valider)


    def paintEvent(self, event):
        painter = QPainter(self)
        font = QFont('Arial', 20)
        painter.setFont(font)

        # Dessiner la grille 15x16
        cell_size = 40
        for i in range(16):
            for j in range(15):
                painter.setPen(Qt.black)
                painter.drawRect(j * cell_size, i * cell_size, cell_size, cell_size)
                if i == 15 and j< len(self.chevalet):  # Dessine les lettres dans le chevalet
                  
                    tuile = self.chevalet[j]
                    painter.setBrush(QColor(tuile.couleur_fond))
                    painter.fillRect(tuile.position[0], tuile.position[1], tuile.size[0], tuile.size[1], QColor(tuile.couleur_fond))
                    painter.setPen(QColor(tuile.couleur_texte))
                    painter.drawText(tuile.position[0] + 10, tuile.position[1] + 27, tuile.lettre)

    def mousePressEvent(self, event):
        self.mouse_handler.mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        self.mouse_handler.mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.mouse_handler.mouseReleaseEvent(event)
# Créer l'application et l'instance de GrilleScrabbleGUI
        

    def on_valider(self):
        print("Validation et tirage en cours...")
        ZONE_CHEVALET_Y = 600

        # Gel des tuiles qui ont été posées sur la grille
        for tuile in self.chevalet:
            # Supposons que la zone y < 600 correspond à la grille
            if tuile.position[1] < ZONE_CHEVALET_Y :

                tuile.geler()
        
        # Identifier les tuiles à conserver et celles à remplacer
        tuiles_a_conserver = [tuile for tuile in self.chevalet if tuile.gelée]
        nombre_tuiles_a_tirer = 7 - len(tuiles_a_conserver)
        
        # Tirer de nouvelles tuiles du sac
        nouvelles_tuiles = self.sac.tirer_lettres(nombre_tuiles_a_tirer)
        
        # Mise à jour de la position des nouvelles tuiles pour qu'elles s'affichent correctement dans le chevalet.
        for i, tuile in enumerate(nouvelles_tuiles, start=len(tuiles_a_conserver)):
            position = (i * 40, ZONE_CHEVALET_Y)
            self.chevalet.append(Tuile(tuile['letter'], tuile['value'], position=position))
        
        # Mise à jour de l'affichage.
        self.update()






app = QApplication([])
fenetre = GrilleScrabbleGUI()
fenetre.show()
app.exec_()
