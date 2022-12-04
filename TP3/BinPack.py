class BinPack:
    def __init__(self, nb_objets, poids, capacite, nb_sacs):
        self.nombre_objets = nb_objets
        self.poids = poids
        self.capacite = capacite
        self.nombre_sacs = nb_sacs

    def __str__(self):
        return "Nombre d'objets: " + str(self.nombre_objets) + " Poids: " + str(self.poids) + " Capacite: " + str(self.capacite) + " Nombre de sacs: " + str(self.nombre_sacs) + " "

    def aUneSolution(self):
        # TODO: essaie tous les certificats un à un jusqu’à en trouver un correct -si il existe
        return True

    def aUneSolutionNonDeterministe(self):
        # TODO génère alétaoirement un certificat et vérifie si il est correct
        return True