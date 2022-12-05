import BinPack
import Certificat
import sys

def readBinPackFromFile(file, nombre_sacs):
    nombre_sacs = int(nombre_sacs)
    capacite = int(file.readline())
    nombre_objets = int(file.readline())
    poids_objets = []
    for i in range(nombre_objets):
        poids_objets.append(int(file.readline()))
    return BinPack.BinPack(nombre_objets, poids_objets, capacite, nombre_sacs)

def askForCertificat():
    print("Entrez un certificat (sous la forme d'une liste de listes):")
    return input()

def main(filepath, nombre_sacs, methode):

    file = open(filepath, "r")
    binPackProblem = readBinPackFromFile(file, nombre_sacs)
    print(binPackProblem)
    file.close()

    if methode == "verification":
        print("Verification")
        certificat = askForCertificat()
        print(binPackProblem.verificationCertificat(certificat))
    elif methode == "non-deterministe":
        print("Non deterministe")
        print(binPackProblem.aUneSolutionNonDeterministe())
    elif methode == "exploration-exhaustive":
        print("exploration exhaustive")
        print(binPackProblem.aUneSolution())
    else:
        print("Methode non reconnue")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
