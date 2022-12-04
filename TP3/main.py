import BinPack
import Certificat

def readCertificatFromFile(file):
    nb_objets = int(file.readline())
    poids = []
    for i in range(nb_objets):
        poids.append(int(file.readline()))
    capacite = int(file.readline())
    nb_sacs = int(file.readline())
    binPackProblem = BinPack.BinPack(nb_objets, poids, capacite, nb_sacs)
    return Certificat.Certificat(binPackProblem)

def readBinPackFromFile(file):
    capacite = int(file.readline())
    nombre_objets = int(file.readline())
    poids_objets = []
    for i in range(nombre_objets):
        poids_objets.append(int(file.readline()))
    return BinPack.BinPack(nombre_objets, poids_objets, capacite, 0)

def main():
    file = open("TP3\BinPack.txt", "r")
    binPackProblem = readBinPackFromFile(file)
    print(binPackProblem)
    file.close()

    file = open("TP3\Certificat.txt", "r")
    certificat = readCertificatFromFile(file)
    print(certificat)
    file.close()

    print(binPackProblem.aUneSolution())
    print(binPackProblem.aUneSolutionNonDeterministe())

if __name__ == "__main__":
    main()