# TP1 : Le plus grand Rectangle

## Question 1 : Une première approche 

Un rectangle de surface maximale respectant les contraintes a nécessairement deux sommets de la forme (xi
, 0),(xj , 0) avec 0 ≤ i < j ≤ n − 1 car un veut que l'un des côtés soit sur l'axe des abscisses.

On a donc :

### l'algortihme en n3 :

- on parcourt tous les points de la liste
- on parcourt tous les points de la liste après le point courant
- on parcourt tous les points entre ces deux points et on prend le plus bas
- on calcule la surface du rectangle formé par les deux points courants et le point le plus bas entre les deux
- on retourne la surface maximale

### l'algortihme en n2 :

- on parcourt tous les points de la liste
- on parcourt tous les points de la liste après le point courant
- on calcule la surface du rectangle formé par les deux points courants et le point le plus bas entre les deux
- on met à jour le point le plus bas entre les deux points courants lors du deuxième parcours
- on retourne la surface maximale

## Question 2 : Diviser pour régner

On va diviser le problème en deux sous-problèmes de taille n/2. On va donc calculer la surface maximale pour les deux sous-problèmes et on va calculer la surface maximale pour le problème initial en utilisant les deux sous-problèmes.

### l'algortihme en nlog(n) :

- on détermine le point pivot (x, y) qui est le point le plus bas
- on calcule l'aire formée par le point pivot et les extrémités du plan
- on coupe verticalement le plan en deux au niveau du point piveau
- on appelle récursivement la fonction sur les deux sous-plans
- on retourne la surface maximale trouvée dans les sous-plans et la surface maximale trouvée en utilisant le point pivot

## Question 3 : Linéaire

On utilise une pile pour stocker les points de la liste. 
On parcourt la liste et on empile les points. 
On dépile les points de la pile tant que le point courant est plus bas que le point au sommet de la pile. 
On calcule alors la surface maximale formée par le point courant et le point au sommet de la pile. 
On met à jour la surface maximale si nécessaire. On retourne la surface maximale.
On va parcourir la liste de points et on va calculer la surface maximale en utilisant le point courant et le point précédent.
On va mettre à jour le point le plus bas entre les deux points courants lors du parcours.

