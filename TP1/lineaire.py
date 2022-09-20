import askTheUser


def main():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()

    pile = [points[0]] # On initialise la pile avec le premier point
    aire = 0 # Aire maximale
    for i in range(1, len(points)): # On parcourt les points
        while len(pile) > 0 and pile[len(pile) - 1][1] > points[i][1]:  # Tant que la pile n'est pas vide et que le point en haut de la pile est plus haut que le point courant
            hauteur_min = pile.pop()[1]  # On récupère la hauteur minimale
            if len(pile) > 0:  # Si la pile n'est pas vide
                aire = max(aire, (points[i][0] - pile[len(pile) - 1][0]) * hauteur_min)  # On calcule l'aire maximale
        pile.append(points[i])  # On ajoute le point courant à la pile
    print(aire)  # On affiche l'aire maximale


if __name__ == '__main__':
    main()
