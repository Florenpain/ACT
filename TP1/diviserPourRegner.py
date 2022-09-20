import askTheUser


def main():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()  # points est une liste de tuples (x, y)

    area_max = diviserPourRegner(points, 0, largeur, hauteur)  # Aire maximale
    print(area_max)


def diviserPourRegner(liste_triee_par_abscisse, plan_x1, plan_x2, hauteur):
    liste_triee_par_ordonnee = sorted(liste_triee_par_abscisse, key=lambda point: point[1])  # On trie par ordonnée
    largeur_plan = plan_x2 - plan_x1  # Largeur du plan
    (x1, y1) = liste_triee_par_ordonnee[0]  # point le plus bas

    aire = largeur_plan * y1  # Aire du rectangle

    index_pivot = liste_triee_par_abscisse.index((x1, y1))  # On récupère l'index du point le plus bas

    aire_max_plan_gauche = 0
    aire_max_plan_droit = 0

    if len(liste_triee_par_abscisse[:index_pivot]) > 0:  # Si le plan de gauche n'est pas vide
        aire_max_plan_gauche = diviserPourRegner(liste_triee_par_abscisse[:index_pivot], plan_x1, x1, hauteur)  # On appelle la fonction récursivement sur le plan de gauche
    if len(liste_triee_par_abscisse[index_pivot+1:]) > 0:  # Si le plan de droite n'est pas vide
        aire_max_plan_droit = diviserPourRegner(liste_triee_par_abscisse[index_pivot+1:], x1, plan_x2, hauteur)  # On appelle la fonction récursivement sur le plan de droite

    return max(aire, aire_max_plan_gauche, aire_max_plan_droit)  # On retourne l'aire maximale


if __name__ == '__main__':
    main()
