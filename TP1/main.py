import askTheUser


def main():
    # The user gives us all the data we need to solve the problem
    points, largeur, hauteur = askTheUser.main()

    aire_max_n3 = n3(points, hauteur)
    aire_max_n2 = n2(points, hauteur)
    aire_max_diviser_pour_regner = diviserPourRegner(points, 0, largeur, hauteur)
    aire_max_lineaire = lineaire(points, hauteur)

    print("aire n3", aire_max_n3)
    print("aire n2", aire_max_n2)
    print("aire diviser pour mieux reigner", aire_max_diviser_pour_regner)
    print("aire linéaire", aire_max_lineaire)


def n3(points, hauteur):
    area_max = 0
    # points_best_rectangle = [(0, 0), (0, 0), (0, 0), (0, 0)]
    n = len(points)
    for i in range(0, n):
        for j in range(i, n):
            hauteur_max = hauteur
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            largeur_max = x2 - x1
            for k in range(i + 1, j):
                (x3, y3) = points[k]
                if hauteur_max > y3:
                    hauteur_max = y3
            if largeur_max * hauteur_max > area_max:
                area_max = largeur_max * hauteur_max
                # points_best_rectangle = [(x1, 0), (x1, hauteur_max), (x2, hauteur_max), (x2, 0)]
    return area_max


def n2(points, hauteur):
    area_max = 0
    # points_best_rectangle = [(0, 0), (0, 0), (0, 0), (0, 0)]
    n = len(points)
    for i in range(0, n):
        hauteur_max = hauteur
        for j in range(i + 1, n):
            (x1, y1) = points[i]
            (x2, y2) = points[j]
            largeur_max = x2 - x1
            if area_max < largeur_max * hauteur_max:
                area_max = largeur_max * hauteur_max
            if hauteur_max > y2:
                hauteur_max = y2
    return area_max


def diviserPourRegner(liste_triee_par_abscisse, plan_x1, plan_x2, hauteur):
    if len(liste_triee_par_abscisse) == 0:  # Si la liste est vide
        return (plan_x2 - plan_x1) * hauteur  # On retourne l'aire maximale
    point_le_plus_bas = (0, hauteur)  # On initialise le point le plus bas à la hauteur du plan
    for point in liste_triee_par_abscisse:  # On parcourt tous les points
        if point[1] < point_le_plus_bas[1]:  # Si le point est plus bas que le point le plus bas
            point_le_plus_bas = point  # On met à jour le point le plus bas
    index_pivot = liste_triee_par_abscisse.index(point_le_plus_bas)  # On récupère l'index du point le plus bas
    aire_max_gauche = diviserPourRegner(liste_triee_par_abscisse[:index_pivot], plan_x1, point_le_plus_bas[0],
                                        hauteur)  # On calcule l'aire maximale dans le plan de gauche
    aire_max_droite = diviserPourRegner(liste_triee_par_abscisse[index_pivot + 1:], point_le_plus_bas[0], plan_x2,
                                        hauteur)  # On calcule l'aire maximale dans le plan de droite
    aire_max = max(aire_max_gauche, aire_max_droite,
                   (plan_x2 - plan_x1) * point_le_plus_bas[1])  # On calcule l'aire maximale
    return aire_max


def lineaire(points, hauteur):
    pile = [points[0]]  # On initialise la pile avec le premier point
    aire = 0  # Aire maximale

    for i in range(1, len(points)):  # On parcourt les points
        aire = max(aire, (points[i][0] - pile[-1][0]) * hauteur)  # On calcule l'aire maximale
        if points[i][1] >= pile[-1][1]:  # Si le point est plus haut que le dernier point de la pile
            pile.append(points[i])  # On ajoute le point à la pile
        else:
            while len(pile) > 1 and points[i][1] < pile[-1][
                1]:  # Tant que la pile contient plus d'un élément et que le point est plus bas que le dernier point de la pile
                aire = max(aire, (points[i][0] - pile[-2][0]) * pile[-1][1])  # On calcule l'aire maximale
                pile.pop()  # On retire le dernier point de la pile
            pile.append(points[i])  # On ajoute le point à la pile
    while len(pile) > 1:  # Tant que la pile contient plus d'un élément
        aire = max(aire, (largeur - pile[-2][0]) * pile[-1][1])  # On calcule l'aire maximale
        pile.pop()  # On retire le dernier point de la pile
    return aire  # On affiche l'aire maximale


if __name__ == '__main__':
    main()
