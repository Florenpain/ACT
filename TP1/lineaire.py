import askTheUser


def main():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()

    pile = [points[0]] # On initialise la pile avec le premier point
    aire = 0 # Aire maximale

    for i in range(1, len(points)): # On parcourt les points
        aire = max(aire, (points[i][0] - pile[-1][0]) * hauteur) # On calcule l'aire maximale
        if points[i][1] >= pile[-1][1]: # Si le point est plus haut que le dernier point de la pile
            pile.append(points[i]) # On ajoute le point à la pile
        else:
            while len(pile) > 1 and points[i][1] < pile[-1][1]: # Tant que la pile contient plus d'un élément et que le point est plus bas que le dernier point de la pile
                aire = max(aire, (points[i][0] - pile[-2][0]) * pile[-1][1] ) # On calcule l'aire maximale
                pile.pop() # On retire le dernier point de la pile
            pile.append(points[i]) # On ajoute le point à la pile
    while len(pile) > 1: # Tant que la pile contient plus d'un élément
        aire = max(aire, (largeur - pile[-2][0]) * pile[-1][1]) # On calcule l'aire maximale
        pile.pop() # On retire le dernier point de la pile
    print(aire) # On affiche l'aire maximale


if __name__ == '__main__':
    main()
