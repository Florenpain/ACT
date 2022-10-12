from copy import deepcopy

hauteur = int(input())
largeur = int(input())
plateauBase = []
for i in range(hauteur):
    plateauBase.append(list(input()))
# print(plateauBase)

def pion_peut_avancer(plateau, x, y, joueurActuel):
    if joueurActuel == 'p' and x < hauteur - 1 and plateau[x+1][y] == ' ' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and plateau[x-1][y] == ' ' and plateau[x][y] == 'P':
        return True
    return False

def avancer_pion(plateau, x, y, joueurActuel):
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y] = joueurActuel
    return plateau

def pion_peut_manger_gauche(plateau, x, y, joueurActuel):
    if joueurActuel == 'p' and x < hauteur - 1 and y > 0 and plateau[x+1][y-1] == 'P' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and y > 0 and plateau[x-1][y-1] == 'p' and plateau[x][y] == 'P':
        return True
    return False

def manger_pion_gauche(plateau, x, y, joueurActuel):
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y-1] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y-1] = joueurActuel
    return plateau

def pion_peut_manger_droite(plateau, x, y, joueurActuel):
    if joueurActuel == 'p' and x < hauteur - 1 and y < largeur - 1 and plateau[x+1][y+1] == 'P' and plateau[x][y] == 'p':
        return True
    elif joueurActuel == 'P' and x > 0 and y < largeur - 1 and plateau[x-1][y+1] == 'p' and plateau[x][y] == 'P':
        return True
    return False

def manger_pion_droite(plateau, x, y, joueurActuel):
    if joueurActuel == 'p':
        plateau[x][y] = ' '
        plateau[x+1][y+1] = joueurActuel
    elif joueurActuel == 'P':
        plateau[x][y] = ' '
        plateau[x-1][y+1] = joueurActuel
    return plateau

def calcul_successeurs(plateau, joueurActuel):
    successeurs = []
    for j in range(largeur):
        if plateau[0][j] == 'P':
            return []
        if plateau[hauteur-1][j] == 'p':
            return []
        for i in range(hauteur):
            if pion_peut_manger_gauche(plateau, i, j, joueurActuel):
                nouveauPlateau = deepcopy(plateau)
                successeurs.append(manger_pion_gauche(nouveauPlateau, i, j, joueurActuel))
            if pion_peut_manger_droite(plateau, i, j, joueurActuel):
                nouveauPlateau = deepcopy(plateau)
                successeurs.append(manger_pion_droite(nouveauPlateau, i, j, joueurActuel))
            if pion_peut_avancer(plateau, i, j, joueurActuel):
                nouveauPlateau = deepcopy(plateau)
                successeurs.append(avancer_pion(nouveauPlateau, i, j, joueurActuel))
    return successeurs

def hexapawn_naif(plateau, joueurActuel):
    successeurs = calcul_successeurs(plateau, joueurActuel)
    maxPositif = 0
    minNegatif = None
    if len(successeurs) == 0:
        return 0
    for successeur in successeurs:
        valeur = hexapawn_naif(successeur, 'p' if joueurActuel == 'P' else 'P')
        # print(valeur)
        if valeur > maxPositif:
            maxPositif = valeur
        elif minNegatif == None and valeur != 0:
            minNegatif = valeur
        elif minNegatif != None and valeur < 0 and valeur > minNegatif:
            minNegatif = valeur
    if minNegatif != None:
        return -(minNegatif-1)
    else:
        if maxPositif == 0 and joueurActuel == 'p':
            return -1
        elif maxPositif == 0 and joueurActuel == 'P':
            return 1
        return -(maxPositif+1)

def hexapawn_dynamique(plateau, joueurActuel, dictPlateaux):
    if (str(plateau), joueurActuel) in dictPlateaux:
        return dictPlateaux[(str(plateau), joueurActuel)]

    successeurs = calcul_successeurs(plateau, joueurActuel)
    maxPositif = 0
    minNegatif = None

    if len(successeurs) == 0:
        return 0

    for successeur in successeurs:
        valeur = hexapawn_dynamique(successeur, 'p' if joueurActuel == 'P' else 'P', dictPlateaux)

        if valeur > maxPositif:
            maxPositif = valeur
        elif minNegatif == None and valeur != 0:
            minNegatif = valeur
        elif minNegatif != None and valeur < 0 and valeur > minNegatif:
            minNegatif = valeur

    if minNegatif != None:
        dictPlateaux[(str(plateau), joueurActuel)] = -(minNegatif-1)
        return -(minNegatif - 1)
    else:
        if maxPositif == 0 and joueurActuel == 'p':
            dictPlateaux[(str(plateau), joueurActuel)] = -1
            return -1
        elif maxPositif == 0 and joueurActuel == 'P':
            dictPlateaux[(str(plateau), joueurActuel)] = 1
            return 1
        else:
            dictPlateaux[(str(plateau), joueurActuel)] = -(maxPositif+1)
            return -(maxPositif + 1)

if __name__ == '__main__':
    print(hexapawn_naif(plateauBase, 'P'))
    # print(hexapawn_dynamique(plateauBase, 'P', dict()))

