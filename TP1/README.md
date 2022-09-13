# TP1 

## Question 1 :
Un rectangle de surface maximale a nécessairement deux sommets de la forme
(xi, 0), (xj, 0) avec 0 <= i < j <= n–1 uniquement parce qu'on souhaite que
la base du rectangle soit sur l’axe des x.

Il existe 2 types de rectangle:
- ceux limités en hauteur par un point donné
- ceux limités par la hauteur du plan donné 

Ainsi, certains rectangles dépendront de 2 points donnés et d'autres de 3. 
Il suffit alors de parcourir une seule fois la liste, en formant les rectangles 2 points par 2 points, et les rectangles 3 points par 3 points.
