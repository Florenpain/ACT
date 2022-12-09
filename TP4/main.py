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


# Calcule la somme de tous les retards
def evaluation(ordonnancement):
    somme_retards = 0
    for element in ordonnancement:
        somme_retards += element["retard"] * element["poids"]
    return somme_retards


# Met à jour le retard de chaque tâche selon l'ordonnancement
def calcul_retard_tache(ordonnancement):
    temps = 0
    for element in ordonnancement:
        temps += element["temps execution"]
        element["temps completion"] = temps
        element["retard"] = max(0, (element["temps completion"] - element["date limite"]))
    return ordonnancement


def ordonnancement_aleatoire(taches):
    ordonnancement = copy.deepcopy(taches)
    random.shuffle(ordonnancement)
    ordonnancement = calcul_retard_tache(ordonnancement)
    return ordonnancement

def heuristiqueLimite(taches):
    ordonnancement = copy.deepcopy(taches)
    ordonnancement = sorted(ordonnancement, key=lambda tache: tache["date limite"])
    ordonnancement = calcul_retard_tache(ordonnancement)
    return ordonnancement

def heuristiqueLimiteSurPoids(taches):
    ordonnancement = [] # on utilise une pile
    # ordonnancement = sorted(ordonnancement, key=lambda tache: tache["date limite"]/ tache["poids"])
    for tache in taches:
        nouvelle_tache = copy.deepcopy(tache)
        buffer = []
        while len(ordonnancement) > 0:
            dernier_element = ordonnancement[len(ordonnancement)-1]
            if (tache["date limite"] / tache["poids"]) < (dernier_element["date limite"] / dernier_element["poids"]):
                buffer += [ordonnancement.pop()]
            else:
                break
        ordonnancement += [nouvelle_tache]
        for element in buffer:
            ordonnancement += [element]
    ordonnancement = calcul_retard_tache(ordonnancement)
    return ordonnancement

def HillClimbing(ordonnancement):
    # Attention au problème de stockage mémoire
    new_ordo = copy.deepcopy(ordonnancement)
    for index in range(0,len(new_ordo)):
        for jndex in range(index, len(new_ordo)):
            if new_ordo[jndex]["retard"] > 0: # variante avec new_ordo[jndex]["retard"] > new_ordo[index]["retard"]
                new_ordo[jndex], new_ordo[index] = new_ordo[index], new_ordo[jndex]
    new_ordo = calcul_retard_tache(new_ordo)
    return new_ordo

def ils(ordonnancement, limite_iteration):
    new_ordo = HillClimbing(ordonnancement)

    for i in range(0, limite_iteration):

        # Perturbation
        random_int = random.randint(0, len(ordonnancement))
        random_int2 = random.randint(0, len(ordonnancement))
        ordonnancement[random_int], ordonnancement[random_int2] = ordonnancement[random_int2], ordonnancement[random_int]
        ordonnancement = calcul_retard_tache(ordonnancement)

        #HillClimbing
        new_ordo_bis = HillClimbing(ordonnancement)

        #Evaluation et mise à jour si besoin
        if evaluation(new_ordo_bis) < evaluation(new_ordo):
            new_ordo = new_ordo_bis

    return new_ordo



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

    ordo_ils = ils(heuristiqueLimiteSurPoids, 5)
    somme_retards_ils = evaluation(ordo_ils)
    print("retard pour ILS : " + str(somme_retards_ils))

