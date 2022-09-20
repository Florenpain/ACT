import askTheUser
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def n2():
    # On récupère les données de l'utilisateur (voir TP1\askTheUser.py)
    points, largeur, hauteur = askTheUser.main()

    area_max = 0  # Aire maximale
    points_best_rectangle = [(0, 0), (0, 0), (0, 0), (0, 0)]  # On ajoute les points pour le cas où le rectangle est le plus grand possible
    n = len(points)  # Nombre de points
    for i in range(0, n):   # On parcourt tous les points
        hauteur_max = hauteur  # On initialise la hauteur maximale à la hauteur du plan
        for j in range(i+1, n):  # On parcourt tous les points
            (x1, y1) = points[i]  # On récupère le point i
            (x2, y2) = points[j]
            largeur_max = x2 - x1   # On calcule la largeur maximale
            if area_max < largeur_max * hauteur_max:    # Si l'aire maximale est plus grande que l'aire maximale actuelle
                area_max = largeur_max * hauteur_max    # On met à jour l'aire maximale
                points_best_rectangle = [(x1, 0), (x1, hauteur_max), (x2, hauteur_max), (x2, 0)]    # On met à jour les points du rectangle
            if hauteur_max > y2:    # Si la hauteur maximale est plus grande que le point k
                hauteur_max = y2  # On met à jour la hauteur maximale

    fig = plt.figure()
    ax = fig.add_subplot()

    rect = Rectangle((points_best_rectangle[0][0], points_best_rectangle[0][1]),
                     points_best_rectangle[2][0] - points_best_rectangle[0][0],
                     points_best_rectangle[2][1] - points_best_rectangle[0][1], linewidth=1, edgecolor='black',
                     facecolor='black')

    ax.set_title('Aire maximum : ' + str(area_max))
    ax.add_patch(rect)
    ax.set_xlim(0, largeur)
    ax.set_ylim(0, hauteur)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.plot([p[0] for p in points], [p[1] for p in points], 'ro')
    plt.show()

    print(area_max)
    # print(points_best_rectangle)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n2()
