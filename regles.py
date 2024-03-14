class ReglesScrabble:
    def __init__(self, sac_de_lettres):
        self.sac_de_lettres = sac_de_lettres
    
    def tirer_tuiles(self, chevalet):
        # Complète le chevalet jusqu'à 7 tuiles si nécessaire
        nombre_a_tirer = 7 - len(chevalet)
        if nombre_a_tirer > 0:
            nouvelles_tuiles = self.sac_de_lettres.tirer_lettres(nombre_a_tirer)
            chevalet.extend(nouvelles_tuiles)
