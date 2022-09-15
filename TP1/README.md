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


Divisé pour reigner

Prendre le point le plus bas 
  calculer l'air du rectangle en dessous de ce point
  couper la liste des points en deux parties
  répéter sur les deux sous graph
  
  
 def clac(tab_de_points,largeur,hauteur)
  #cas de base
  if count(tab_de_points) = 1
      air=largeur*min.y
      return air
   else
      min=plus petit y de tab_de_points 
      liste1=tab_de_point[0:x](avec le 0 compris et le x non compris dans la liste)
      liste2=tab_de_point[x:n](avec le n compris et le x non compris dans la liste)
      air1= clac(liste1,largeur/2,hauteur)
      air2= clac(liste2,largeur/2,hauteur)
      return max(air1,air2)
  
