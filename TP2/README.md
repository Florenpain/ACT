# TP2

*[Lien du sujet](https://moodle.univ-lille.fr/pluginfile.php/2689929/mod_resource/content/1/hexapawn.pdf)*

## Question 1 : Formule mathématique 

Pour calculer la valeur d'une configuration à partir des valeurs de ses successeurs, on va utiliser la formule suivante :

- S'il existe des valeurs négatives parmis les successeurs :
  - on retourne l'opposé de la valeur négative la plus grande parmi les successeurs, +1
- Sinon :
  - on retourne l'opposé de la valeur positive la plus grande parmi les successeurs, -1

## Question 2 : Algorithme naïf

- On calcule tous les successeurs possibles du plateau de jeu pour le joueur actuel
- Si le plateau n'a pas de successeur, cela signifie qu'aucun coup n'est jouable, on retourne 0.
- On parcourt tous les successeurs
  - On calcule récusrivement la valeur renvoyé par le successeur
  - On met à jour la liste de valeurs des successeurs 
- On retourne la valeur de la configuration comme décrit dans la question 1

## Question 3 : Algorithme dynamique

Même principe que l'algorithme naïf, mais on stocke les valeurs des configurations déjà calculées dans un dictionnaire.
