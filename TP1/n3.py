import askTheUser
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def n3():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()

    area_max = 0  # Aire maximale
    points_best_rectangle = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]  # On ajoute les points pour le cas où le rectangle est le plus grand possible
    n = len(points)  # Nombre de points
    for i in range(0, n):  # On parcourt tous les points
        for j in range(i, n):  # On parcourt tous les points
            hauteur_max = hauteur  # On initialise la hauteur maximale à la hauteur du plan
            (x1, y1) = points[i]  # On récupère le point i
            (x2, y2) = points[j]  # On récupère le point j
            largeur_max = x2 - x1  # On calcule la largeur maximale
            for k in range(i+1, j):  # On parcourt tous les points entre i et j
                (x3, y3) = points[k]  # On récupère le point k
                if hauteur_max > y3:  # Si la hauteur maximale est plus grande que le point k
                    hauteur_max = y3    # On met à jour la hauteur maximale
            if largeur_max * hauteur_max > area_max:    # Si l'aire maximale est plus grande que l'aire maximale actuelle
                area_max = largeur_max * hauteur_max  # On met à jour l'aire maximale
                points_best_rectangle = [(x1, 0), (x1, hauteur_max), (x2, hauteur_max), (x2, 0), (x1, 0)]  # On met à jour les points du rectangle

    fig = plt.figure()  # On crée la figure
    ax = fig.add_subplot()  # On crée l'axe

    rect = Rectangle((points_best_rectangle[0][0],
                      points_best_rectangle[0][1]),
                     points_best_rectangle[2][0] - points_best_rectangle[0][0],
                     points_best_rectangle[2][1] - points_best_rectangle[0][1],
                     linewidth=1,
                     edgecolor='black',
                     facecolor='black')     # On crée le rectangle

    ax.set_title('Aire maximum : ' + str(area_max))   # On met le titre
    ax.add_patch(rect)  # On ajoute le rectangle
    ax.set_xlim(0, largeur)  # On met les limites de l'axe x
    ax.set_ylim(0, hauteur)  # On met les limites de l'axe y
    plt.ylabel('y')  # On met le label de l'axe y
    plt.xlabel('x')  # On met le label de l'axe x
    plt.plot([p[0] for p in points], [p[1] for p in points], 'ro')  # On ajoute les points
    plt.show()  # On affiche la figure

    print(area_max)  # On affiche l'aire maximale
    # print(points_best_rectangle)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n3()
