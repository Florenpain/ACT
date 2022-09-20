def main():
    largeur_plan, hauteur_plan = input().split()
    largeur = int(largeur_plan)
    hauteur = int(hauteur_plan)
    n = int(input())    # nombre de points dans le plan
    points = [(0, 0)]
    for i in range(0, int(n)): # on lit les points
        x, y = input().split()
        x = int(x)
        y = int(y)
        points.append((x, y))
    points.append((largeur, 0))

    return points, largeur, hauteur
