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
    liste_triee_par_ordonnee = sorted(liste_triee_par_abscisse, key=lambda point: point[1])
    largeur_plan = plan_x2 - plan_x1
    (x1, y1) = liste_triee_par_ordonnee[0]  # point le plus bas
    aire = largeur_plan * y1
    index_pivot = liste_triee_par_abscisse.index((x1, y1))
    aire_max_plan_gauche = 0
    aire_max_plan_droit = 0
    if len(liste_triee_par_abscisse[:index_pivot]) > 0:
        aire_max_plan_gauche = diviserPourRegner(liste_triee_par_abscisse[:index_pivot], plan_x1, x1, hauteur)
    if len(liste_triee_par_abscisse[index_pivot+1:]) > 0:
        aire_max_plan_droit = diviserPourRegner(liste_triee_par_abscisse[index_pivot+1:], x1, plan_x2, hauteur)
    return max(aire, aire_max_plan_gauche, aire_max_plan_droit)


def lineaire(points, hauteur):
    pile = [points[0]]
    aire = 0
    for i in range(1, len(points)):
        while len(pile) > 0 and pile[len(pile) - 1][1] > points[i][1]:
            hauteur_min = pile.pop()[1]
            if len(pile) > 0:
                aire = max(aire, (points[i][0] - pile[len(pile) - 1][0]) * hauteur_min)
        pile.append(points[i])
    return aire


if __name__ == '__main__':
    main()
