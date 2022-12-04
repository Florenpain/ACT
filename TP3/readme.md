# TP 3 - Les propriétés NP, les réductions polynomiales

## Commandes utiles 

python main.py data/exBPeq1_min3 5 verification

##  Qu’est-ce qu’une propriété NP ?

Données:
n : un nombre d’objets
x1, · · · , xn : n entiers, les poids des objets
c : la capacité d’un sac (entière)
k : le nombre de sacs

Sortie:
Chaque objet est attribué à un sac si possible sinon false

### Q 1.La propriété est NP.

#### Définir une notion de certificat.
Le certificat correspond à un ensemble d'objet pour chaque sac

#### Comment pensez-vous l’implémenter ?
on peut représenter le certificat par un tableau associatif , pour chaque objet on a un sac. (peut être faire une liste de liste , premier indice le sac et la liste les objetsà l'interieur)

#### Quelle sera la taille d’un certificat ?
La taille d'un certificat sera la taille sera le nombre d'objets présent dans le problème.

#### La taille des certificats est-elle bien bornée polynomialement par rapport à la taille de l’entrée ?
La taille est égal a n 

#### Proposez un algorithme de vérification associé. Est-il bien polynomial ?

   On récupére un tab associatif L qui a n objets, et chaque objet est associé à un sac k.

    
    // Il faudrait idéalement vérifier si les objets sont bien présents dans la liste d'objet de départ

    //on calcule la somme des poids par sac et
    //on vérifie que chaque objet appartient bien à un sac
    o= liste de de sac associé à 0 
    Pour i allant de 0 à n-1
        if L[i] != null // on vérifie queun sac est bien associé à chaque objet
            o[L[i]]+=x[L[i]]  on ajoute à la table associatif le poid de l'objet
     
    //on vérifie que chaque sac n'a pas dépasser sa capacité
    Pour u allant de 0 à k-1
        si o[u] > c
            return false
    return true

### Q 2. NP = Non déterministe polynomial

#### Q 2.1. Génération aléatoire d’un certificat.

entrée

n : un nombre d’objets
k : le nombre de sacs


//on attribut un sac aléatoirement à chaque objet
L: liste taille n qui corrspond à un numéro de sac

for i allant de 0 à n-1
    L[i]=random([0:k[) // on attribut un sac aléatoire on considére que c est //un tableau commencant par 0 donc 0 est inclu et k exclu

#### Votre algorithme génère-t-il de façon uniforme les certificats, i.e. tous les certificats ont-ils la même probabilité d’apparaître ?

La génération de l'aléatoire vient de la fonction random, par exemple 



Q 2.2. Quel serait le schéma d’un algorithme non-déterministe polynomial pour le problème ?
Q 3. NP ⊂ EXP T IME
Q 3.1. Pour n et k fixés, combien de valeurs peut-prendre un certificat 
    
