import random
import sys
import copy


def read_file(filepath):
    with open(filepath, 'r') as file:
        nombre_taches = int(file.readline())
        taches = []
        for i in range(nombre_taches):
            line = file.readline().split()
            taches.append({"temps execution": int(line[0]), "poids": int(line[1]), "date limite": int(line[2])})
        return taches


def evaluation(ordonnancement):
    somme_retards = 0
    for element in ordonnancement:
        somme_retards += element["retard"] * element["poids"]
    return somme_retards


def ordonnancement_aleatoire(taches):
    ordonnancement = copy.deepcopy(taches)
    random.shuffle(ordonnancement)

    temps = 0
    for element in ordonnancement:
        temps += element["temps execution"]
        element["temps completion"] = temps
        element["retard"] = max(0, (element["temps completion"] - element["date limite"]))

    return ordonnancement

def heuristiqueLimite(taches):
    ordonnancement = copy.deepcopy(taches)
    ordonnancement=sorted(ordonnancement, key=lambda tache: tache["date limite"])
    temps = 0
    for element in ordonnancement:
        temps += element["temps execution"]
        element["temps completion"] = temps
        element["retard"] = max(0, (element["temps completion"] - element["date limite"]))
    return ordonnancement

def heuristiqueLimiteSurPoids(taches):
    ordonnancement = [] # on utilise une pile
    for tache in taches:
        nouvelle_tache = copy.deepcopy(tache)
        buffer = []
        while len(ordonnancement) > 0:
            dernier_element = ordonnancement[len(ordonnancement)-1]
            if (tache["date limite"] / tache["poids"]) < (dernier_element["date limite"] / dernier_element["poids"]):
                buffer += ordonnancement.pop()
            else:
                break
        ordonnancement += nouvelle_tache
        for element in buffer:
            ordonnancement += element

    temps = 0
    for element in ordonnancement:
        temps += element["temps execution"]
        element["temps completion"] = temps
        element["retard"] = max(0, (element["temps completion"] - element["date limite"]))
    return ordonnancement

def HillClimbing(ordonnancement):
    # TODO: gérer problème d'adresse mémoire
    new_ordo = copy.deepcopy(ordonnancement)
    for index in range(0,len(new_ordo)):
        for jndex in range(index, len(new_ordo)):
            if new_ordo[jndex]["retard"] > 0: # variante avec new_ordo[jndex]["retard"] > new_ordo[index]["retard"]
                buffer = ordonnancement[jndex]
                new_ordo[jndex] = new_ordo[index]
                new_ordo[index] = buffer

    temps = 0
    for element in new_ordo:
        temps += element["temps execution"]
        element["temps completion"] = temps
        element["retard"] = max(0, (element["temps completion"] - element["date limite"]))
    return new_ordo

def ils(ordonnancement, limite_iteration):
    new_ordo = HillClimbing(ordonnancement)
    resultFind = False

    for i in range(0, limite_iteration):
        while not resultFind:
            if evaluation(ordonnancement) == evaluation(new_ordo):
                resultFind = True

    # Perturbation

    return 'idk'



if __name__ == "__main__":
    filepath = sys.argv[1]
    taches = read_file(filepath)

    ordonnancement_alea = ordonnancement_aleatoire(taches)
    somme_retards_alea = evaluation(ordonnancement_alea)
    print("retard pour ordonnancement aléatoire : " + str(somme_retards_alea))

    ordonnancement_heuristique_limite = heuristiqueLimite(taches)
    somme_retards_limite = evaluation(ordonnancement_heuristique_limite)
    print("retard pour ordonnancement heuristique limite : " + str(somme_retards_limite))

    heuristiqueLimiteSurPoids = heuristiqueLimiteSurPoids(taches)
    somme_retards_limiteSurPoids = evaluation(heuristiqueLimiteSurPoids)
    print("retard pour ordonnancement heuristique limite sur poids : " + str(somme_retards_limiteSurPoids))

    ordo_hillClimbing = HillClimbing(heuristiqueLimiteSurPoids)
    somme_retards_hillClimbing = evaluation(ordo_hillClimbing)
    print("retard pour Hill Climbing : " + str(somme_retards_hillClimbing))
