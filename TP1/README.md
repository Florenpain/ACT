# TP1 : Le plus grand Rectangle

## Question 1 : Une première approche 

Un rectangle de surface maximale respectant les contraintes a nécessairement deux sommets de la forme (xi
, 0),(xj , 0) avec 0 ≤ i < j ≤ n − 1 car on veut que l'un des côtés soit sur l'axe des abscisses.

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

- Si la liste est vide :
    - on retourne l'aire formé par les extrémités du plan et la hauteur
- On parcourt la liste pour déterminer le point le plus bas 
- On récupère l'index du point le plus bas
- On coupe verticalement le plan en deux parties au niveau du point le plus bas
- On calcule la surface maximale pour la partie gauche
- On calcule la surface maximale pour la partie droite
- On calcule la surface maximale pour le plan en utilisant les deux sous-problèmes
- On retourne la surface maximale

## Question 3 : Linéaire

- On utilise une pile et on stocke le premier point de la liste. 
- On parcourt la liste :
  - on calcule l'aire du rectangle formé par le point courant, le sommet de la pile, et la hauteur du plan.
  - Si le point courant est plus haut que le sommet de la pile, on le met dans la pile
  - Sinon, on dépile la pile tant que le point courant est plus bas que le sommet de la pile. 
  - Pour chaque point dépiler, on calcule l'aire du rectangle formé par le point courant, le sommet de la pile, et le point dépilé. 
  - On met à jour la surface maximale si nécessaire. On met ensuite le point courant dans la pile.
- Tant qu'il y a des points dans la pile :
  - on les dépiles et on calcule l'aire du rectangle formé par le point courant, le sommet de la pile, et le point dépilé. 
  - On met à jour la surface maximale si nécessaire.
- On retourne la surface maximale.


