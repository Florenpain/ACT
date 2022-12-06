# TP 4 - Heuristiques

## Question 1 :
cf fonction evaluation

## Question 2 :
cf fonction ordonnancement_aleatoire

## Question 3 :

### 3.1 : Heuristique limite naïve
cf fonction heuristiqueLimite

Description : on trie les tâches par ordre croissant de durée limite.

### 3.2 : Heuristique ratio limite sur poids
cf fonction heuristiqueLimiteSurPoids

Description : on trie les tâches par ordre croissant de ratio limite sur poids.

## Question 4 : Hill climbing
cf fonction hillClimbing

On part d'une solution initiale (donnée par une heuristique)
Pour générer le voisin, on applique la démarche suivante :
- on parcourt les tâches de la solution initiale
- pour chaque tâche, on cherche la prochaine tâche qui est en retard 
- on effectue une permutation entre les deux
- on recalcule les temps de complétion et les retards

## Question 5 : ILS
cf fonction ils

On part d'une solution initiale (donnée par une heuristique)
On applique HillClimbing sur cette solution
Pour une certaine condition : (à déterminer)(boucle)(critère d'arrêt)
- Perturbation : on échange l'ordre de 2 tâches de manière aléatoire. (possbilité d'ajouter un paramètre pour définir le nombre de tâches à permuter)
- on applique HillClimbing sur cette nouvelle solution
- Si cette nouvelle solution est meilleure que la solution choisie précédemment, on la garde comme solution finale (critère d'acceptation)

## Question 6 : 
TODO