class MouseHandler:
    def __init__(self, interface, chevalet):
        self.interface = interface
        self.chevalet = chevalet
        self.selected_tuile = None
        self.initial_mouse_pos = None
        self.tuile_initial_pos = None

    def mousePressEvent(self, event):
        print("Clic détecté à la position :", event.pos())



        for index, tuile in enumerate(self.chevalet):
            if tuile.rect().contains(event.pos()) and not tuile.gelée:
                print(f"Tuile {index} sélectionnée.")
                self.selected_tuile = tuile
                self.initial_mouse_pos = event.pos()
                self.tuile_initial_pos = tuile.position
                break



    def mouseMoveEvent(self, event):
        if self.selected_tuile:
            dx = event.pos().x() - self.initial_mouse_pos.x()
            dy = event.pos().y() - self.initial_mouse_pos.y()
            new_position = (self.tuile_initial_pos[0] + dx, self.tuile_initial_pos[1] + dy)
            self.selected_tuile.setPosition(new_position)
            self.interface.update()



    def mouseReleaseEvent(self, event):
        if self.selected_tuile:
            # Calculer la position ajustée sur la grille
            snapped_position = self.getClosestGridPosition(self.selected_tuile.position)
            self.selected_tuile.setPosition(snapped_position)
            self.selected_tuile = None
            self.interface.update()

    def getClosestGridPosition(self, position):
        # Calculer la position de grille la plus proche
        cell_size = 40  # Assurez-vous que cela correspond à la taille de votre cellule
        grid_x = round(position[0] / cell_size) * cell_size
        grid_y = round(position[1] / cell_size) * cell_size

        # Limiter les positions pour qu'elles restent dans les limites de la grille
        grid_x = max(0, min(grid_x, cell_size * (15 - 1)))  # 15 colonnes pour la grille, -1 pour l'index
        grid_y = max(0, min(grid_y, cell_size * (15 - 1)))  # 15 lignes pour la grille, -1 pour l'index

        return (grid_x, grid_y)