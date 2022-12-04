import BinPack

class Certificat:
    def __init__(self, binPackProblem):
        self.binPackProblem = binPackProblem
        self.solution = []

    def setSolution(self, solution):
        self.solution = solution

    def estCorrect(self):
        # TODO : vérifie si le certificat est correct
        return True

    def suivant(self):
        # TODO : génère le certificat suivant
        return True

    def estDernier(self):
        # TODO : vérifie si le certificat est le dernier
        return True

    def aleatoire(self):
        # TODO : génère un certificat aléatoire
        return True

    def afficher(self):
        # TODO : affiche le certificat
        return True

