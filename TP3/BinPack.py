import random
import sys


def readBinPackFromFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        capacite = int(file.readline())
        nombre_objets = int(file.readline())
        poids = []
        for i in range(nombre_objets):
            poids.append(int(file.readline()))
        return capacite, nombre_objets, poids


def verificationCertificat(nombre_objets, nombre_sacs, capacite, poids, certificat):

    poids_sacs = {}

    for i in range(nombre_objets):
        if certificat[i] in poids_sacs:
            poids_sacs[certificat[i]] += poids[i]
        else:
            poids_sacs[certificat[i]] = poids[i]

    if len(poids_sacs) > nombre_sacs:
        return False

    for sac in poids_sacs:
        if poids_sacs[sac] > capacite:
            return False
    return True


def generationCertificatAleatoire(nombre_objets, nombre_sacs):
    certificat = []
    for i in range(nombre_objets):
        certificat.append(random.randint(0, nombre_sacs - 1))
    return certificat


def aUneSolutionNonDeterministe(nombre_objets, nombre_sacs, capacite, poids):
    certificat = generationCertificatAleatoire(nombre_objets, nombre_sacs)
    return verificationCertificat(nombre_objets, nombre_sacs, capacite, poids, certificat), certificat


def generationCertificatSuccessif(nombre_objets, nombre_sacs, certificat):
    if certificat == None:
        certificat = [0] * nombre_objets
    else:
        certificat = certificat.copy()
        i = 0
        while i < nombre_objets and certificat[i] == nombre_sacs - 1:
            certificat[i] = 0
            i += 1
        if i == nombre_objets:
            return None
        certificat[i] += 1
    return certificat


def aUneSolution(nombre_objets, nombre_sacs, capacite, poids):
    certificat = None
    while True:
        certificat = generationCertificatSuccessif(nombre_objets, nombre_sacs, certificat)
        if certificat == None:
            return False
        if verificationCertificat(nombre_objets, nombre_sacs, capacite, poids, certificat):
            return True


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 BinPack.py <filename> <type> <nombre_sacs>")
        exit(1)

    filepath = sys.argv[1]
    mode = sys.argv[2]
    nombre_sacs = int(sys.argv[3])
    capacite, nombre_objets, poids = readBinPackFromFile(filepath)

    if mode == 'ver':
        certificat = input("Entrez le certificat sous la forme d'une liste de nombres: ")
        if verificationCertificat(nombre_objets, nombre_sacs, capacite, poids, certificat):
            print("Le certificat est valide")
        else:
            print("Le certificat est faux")

    elif mode == 'nd':
        boolTest, certificat = aUneSolutionNonDeterministe(nombre_objets, nombre_sacs, capacite, poids)
        if boolTest:
            print("Le certificat généré aléatoirement " + certificat.__str__() + " est valide")
        else:
            print("Le certificat généré aléatoirement " + certificat.__str__() + " est faux")

    elif mode == 'exh':
        if aUneSolution(nombre_objets, nombre_sacs, capacite, poids):
            print('Une solution à été trouvé')
        else:
            print('pas de solution possible')
    else:
        print("Erreur lors de la saisie du mode")
