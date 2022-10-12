dictionnairePlateaux = {}

hauteur = int(input())
largeur = int(input())
plateauBase = []
for i in range(hauteur):
    plateauBase.append(list(input()))


def copier_plateau(plateau):
    """
    Copie un plateau dans un nouveau plateau (pour éviter les problèmes de références)
    :param plateau: plateau à copier (liste de listes)
    :return: nouveau plateau (liste de listes)
    """
    nouveauPlateau = []
    for i in range(hauteur):
        nouveauPlateau += [plateau[i][::]]
    return nouveauPlateau

def pion_peut_avancer(plateau, x, y, joueurActuel):
    """
    Vérifie si un pion peut avancer (sans manger)
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return: True si le pion peut avancer, False sinon
    """
    if joueurActuel == 'p' and x < hauteur - 1 and plateau[x+1][y] == ' ' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and plateau[x-1][y] == ' ' and plateau[x][y] == 'P':
        return True
    return False

def avancer_pion(plateau, x, y, joueurActuel):
    """
    Avance un pion d'une case
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return: plateau modifié (liste de listes)
    """
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y] = joueurActuel
    return plateau

def pion_peut_manger_gauche(plateau, x, y, joueurActuel):
    """
    Vérifie si un pion peut manger à gauche
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return: True si le pion peut manger à gauche, False sinon
    """
    if joueurActuel == 'p' and x < hauteur - 1 and y > 0 and plateau[x+1][y-1] == 'P' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and y > 0 and plateau[x-1][y-1] == 'p' and plateau[x][y] == 'P':
        return True
    return False

def manger_pion_gauche(plateau, x, y, joueurActuel):
    """
    Mange un pion à gauche
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return: plateau modifié (liste de listes)
    """
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y-1] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y-1] = joueurActuel
    return plateau

def pion_peut_manger_droite(plateau, x, y, joueurActuel):
    """
    Vérifie si un pion peut manger à droite
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return:  True si le pion peut manger à droite, False sinon
    """
    if joueurActuel == 'p' and x < hauteur - 1 and y < largeur - 1 and plateau[x+1][y+1] == 'P' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and y < largeur - 1 and plateau[x-1][y+1] == 'p' and plateau[x][y] == 'P':
        return True
    return False

def manger_pion_droite(plateau, x, y, joueurActuel):
    """
    Mange un pion à droite
    :param plateau: plateau de jeu
    :param x: position x du pion
    :param y: position y du pion
    :param joueurActuel: joueur actuel (p ou P)
    :return: plateau modifié (liste de listes)
    """
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y+1] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y+1] = joueurActuel
    return plateau

def calcul_successeurs(plateau, joueurActuel):
    """
    Calcul les successeurs d'un plateau pour un joueur donné (p ou P)
    :param plateau: plateau de jeu
    :param joueurActuel: joueur actuel (p ou P)
    :return: liste de successeurs (liste de listes)
    """
    successeurs = []
    for j in range(largeur):
        if plateau[0][j] == 'P':
            return []
        if plateau[hauteur-1][j] == 'p':
            return []
        for i in range(hauteur):
            if pion_peut_manger_gauche(plateau, i, j, joueurActuel):
                nouveauPlateau = copier_plateau(plateau)
                successeurs.append(manger_pion_gauche(nouveauPlateau, i, j, joueurActuel))
            if pion_peut_manger_droite(plateau, i, j, joueurActuel):
                nouveauPlateau = copier_plateau(plateau)
                successeurs.append(manger_pion_droite(nouveauPlateau, i, j, joueurActuel))
            if pion_peut_avancer(plateau, i, j, joueurActuel):
                nouveauPlateau = copier_plateau(plateau)
                successeurs.append(avancer_pion(nouveauPlateau, i, j, joueurActuel))
    return successeurs

def hexapawn_naif(plateau, joueurActuel):
    """
    Renvoie le meilleur coup pour le joueur actuel
    :param plateau: plateau de jeu
    :param joueurActuel: joueur actuel (p ou P)
    :return: meilleur coup
    """
    successeurs = calcul_successeurs(plateau, joueurActuel)
    valeursPositives = []
    valeursNegatives = []
    if len(successeurs) == 0:
        return 0
    for successeur in successeurs:
        valeur = hexapawn_naif(successeur, 'p' if joueurActuel == 'P' else 'P')
        # print(valeur)
        if valeur <= 0:
            valeursNegatives.append(valeur)
        else:
            valeursPositives.append(valeur)
    if len(valeursNegatives) > 0:
        return -1*max(valeursNegatives)+1
    else:
        return -1*max(valeursPositives)-1

def hexapawn_dynamique(plateau, joueurActuel):
    """
    Renvoie le meilleur coup pour le joueur actuel
    :param plateau: plateau de jeu
    :param joueurActuel: joueur actuel (p ou P)
    :return: meilleur coup
    """
    global dictionnairePlateaux
    if (str(plateau), joueurActuel) in dictionnairePlateaux:
        return dictionnairePlateaux[(str(plateau), joueurActuel)]
    successeurs = calcul_successeurs(plateau, joueurActuel)
    valeursPositives = []
    valeursNegatives = []
    if len(successeurs) == 0:
        return 0
    for successeur in successeurs:
        valeur = hexapawn_dynamique(successeur, 'p' if joueurActuel == 'P' else 'P')
        if valeur <= 0:
            valeursNegatives.append(valeur)
        else:
            valeursPositives.append(valeur)
    if valeursNegatives:
        dictionnairePlateaux[(str(plateau), joueurActuel)] = -1*max(valeursNegatives)+1
        return -1*max(valeursNegatives)+1
    else:
        dictionnairePlateaux[(str(plateau), joueurActuel)] = -1*max(valeursPositives)-1
        return -1*max(valeursPositives)-1

if __name__ == '__main__':
    # print(hexapawn_naif(plateauBase, 'P'))
    print(hexapawn_dynamique(plateauBase, 'P'))

