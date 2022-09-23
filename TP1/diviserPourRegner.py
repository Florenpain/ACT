import askTheUser


def main():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()  # points est une liste de tuples (x, y)

    area_max = diviserPourRegner(points, 0, largeur, hauteur)  # Aire maximale
    print(area_max)


def diviserPourRegner(liste_triee_par_abscisse, plan_x1, plan_x2, hauteur):

    if len(liste_triee_par_abscisse) == 0: # Si la liste est vide
        return (plan_x2 - plan_x1) * hauteur  # On retourne l'aire maximale
    point_le_plus_bas = (0, hauteur)  # On initialise le point le plus bas à la hauteur du plan
    for point in liste_triee_par_abscisse:  # On parcourt tous les points
        if point[1] < point_le_plus_bas[1]: # Si le point est plus bas que le point le plus bas
            point_le_plus_bas = point # On met à jour le point le plus bas
    index_pivot = liste_triee_par_abscisse.index(point_le_plus_bas)  # On récupère l'index du point le plus bas
    aire_max_gauche = diviserPourRegner(liste_triee_par_abscisse[:index_pivot], plan_x1, point_le_plus_bas[0], hauteur)  # On calcule l'aire maximale dans le plan de gauche
    aire_max_droite = diviserPourRegner(liste_triee_par_abscisse[index_pivot + 1:], point_le_plus_bas[0], plan_x2, hauteur)  # On calcule l'aire maximale dans le plan de droite
    aire_max = max(aire_max_gauche, aire_max_droite, (plan_x2 - plan_x1) * point_le_plus_bas[1])  # On calcule l'aire maximale
    return aire_max


if __name__ == '__main__':
    main()
