import random

class BinPack:
    def __init__(self, nb_objets, poids, capacite, nb_sacs):
        self.nombre_objets = nb_objets
        self.poids = poids
        self.capacite = capacite
        self.nombre_sacs = nb_sacs

    def __str__(self):
        return "Nombre d'objets: " + str(self.nombre_objets) + " Poids: " + str(self.poids) + " Capacite: " + str(self.capacite) + " Nombre de sacs: " + str(self.nombre_sacs) + " "

    def aUneSolution(self):
        certificats = self.generationTousLesCertificats()
        for i in range(len(certificats)):
            if self.verificationCertificat(certificats[i]):
                return True
        return False

    def aUneSolutionNonDeterministe(self):
        certificat = self.generationCertificatAleatoire()
        return self.verificationCertificat(certificat)

    def verificationCertificat(self, certificat):

        # On vérifie que le certificat est une liste de listes
        if not isinstance(certificat, list):
            return False
        for i in range(len(certificat)):
            if not isinstance(certificat[i], list):
                return False

        # On vérifie que le certificat contient le bon nombre de sacs
        if len(certificat) != self.nombre_sacs:
            return False

        # On vérifie que le certificat contient le bon nombre d'objets
        nb_objets = 0
        for i in range(len(certificat)):
            nb_objets += len(certificat[i])
        if nb_objets != self.nombre_objets:
            return False

        # On vérifie que le certificat contient bien tous les objets
        objets = []
        for i in range(len(certificat)):
            for j in range(len(certificat[i])):
                objets.append(certificat[i][j])
        objets.sort()
        for i in range(self.nombre_objets):
            if objets[i] != i:
                return False

        # On vérifie que le certificat respecte la capacité des sacs
        for i in range(len(certificat)):
            poids_utilise = 0
            for j in range(len(certificat[i])):
                poids_utilise += self.poids[certificat[i][j]]
            if poids_utilise > self.capacite:
                return False

        return True


    def generationCertificatAleatoire(self):
        certificat = []
        for i in range(self.nombre_sacs):
            certificat.append([])
        for i in range(self.nombre_objets):
            certificat[random.randint(0, self.nombre_sacs - 1)].append(i)
        return certificat

    def generationTousLesCertificats(self):
        certificats = []
        certificat = []
        for i in range(self.nombre_sacs):
            certificat.append([])
        for i in range(self.nombre_objets):
            certificat[0].append(i)
        certificats.append(certificat)
        while not self.certificatDernier(certificat):
            certificat = self.certificatSuivant(certificat)
            certificats.append(certificat)
        return certificats

    def certificatSuivant(self, certificat):
        for i in range(len(certificat)):
            if len(certificat[i]) > 0:
                certificat[i].pop()
                if i < len(certificat) - 1:
                    certificat[i + 1].append(certificat[i][0])
                    certificat[i].pop(0)
                else:
                    certificat[0].append(certificat[i][0])
                    certificat[i].pop(0)
                break
        return certificat

    def certificatDernier(self, certificat):
        return len(certificat[len(certificat) - 1]) == self.nombre_objets
