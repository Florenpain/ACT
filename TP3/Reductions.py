from BinPack import aUneSolution
import sys


def readPartitionFile(filename):
    with open(filename, 'r') as file:
        nombre_objets = int(file.readline())
        poids = []
        for i in range(nombre_objets):
            poids.append(int(file.readline()))
        return nombre_objets, poids


def readSumFile(filepath):
    with open(filepath, 'r') as f:
        nombre_objets = int(f.readline())
        poids = []
        for i in range(nombre_objets):
            poids.append(int(f.readline()))
        cible = int(f.readline())
        return nombre_objets, poids, cible


def partition(nombre_objets, poids):
    somme = sum(poids)/2 + sum(poids)%2
    return aUneSolution(nombre_objets, 2, somme, poids)


def sum(nombre_objets, poids, cible):
    poids += [2*cible - sum(poids)]
    return partition(nombre_objets+1, poids)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 Reductions.py <filename> <type>")
        exit(1)
    filename = sys.argv[1]
    type = sys.argv[2]
    if type == "par":
        nombre_objets, poids = readPartitionFile(filename)
        if partition(nombre_objets, poids):
            print("Une solution a été trouvée")
        else:
            print("Aucune solution n'a été trouvée")
    elif type == "sum":
        nombre_objets, poids, cible = readSumFile(filename)
        if sum(nombre_objets, poids, cible):
            print("Une solution a été trouvée")
        else:
            print("Aucune solution n'a été trouvée")
    else:
        print("Type must be 'par' or 'sum'")