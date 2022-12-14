# TP 3 - BinPack

## 1 - Qu’est-ce qu’une propriété NP ?

### Question 1 : La propriété est NP

#### Définir une notion de certificat.
Le certificat correspond à un ensemble d'objet pour chaque sac

#### Comment pensez-vous l’implémenter ?
On peut représenter le certificat par une liste, chaque élément de la liste correspond à un numéro de sac, pour l'objet du même index dans la liste d'objets.

#### Quelle sera la taille d’un certificat ?
La taille d'un certificat sera égale au nombre d'objets présents (n) dans le problème.

#### La taille des certificats est-elle bien bornée polynomialement par rapport à la taille de l’entrée ?
Oui, la taille des certificats est bien bornée polynomialement par rapport à la taille de l'entrée.

#### Proposez un algorithme de vérification associé. Est-il bien polynomial ?

```python
def verificationCertificat(nombre_objets, nombre_sacs, capacite, poids, certificat):
    poids_sacs = {}
    for i in range(nombre_objets):
        if certificat[i] in poids_sacs:
            poids_sacs[certificat[i]] += poids[i]
        else:
            poids_sacs[certificat[i]] = poids[i]
    if len(poids_sacs) > nombre_sacs:
        return False
    for sac in poids_sacs:
        if poids_sacs[sac] > capacite:
            return False
    return True
```

L'algorithme de vérification est polynomial, car il parcourt les éléments du certificat et les poids des objets, et effectue des opérations élémentaires.

### Question 2 : NP = Non déterministe polynomial

#### Q 2.1. Génération aléatoire d’un certificat.

```python
def generationCertificatAleatoire(nombre_objets, nombre_sacs):
    certificat = []
    for i in range(nombre_objets):
        certificat.append(random.randint(0, nombre_sacs - 1))
    return certificat
```

#### Votre algorithme génère-t-il de façon uniforme les certificats, i.e. tous les certificats ont-ils la même probabilité d’apparaître ?
Notre algorithme génère un certificat de manière uniforme les certificats, c'est-à-dire que chaque certificat a la même probabilité d'être généré.

Effectivement, le sac attribué à un objet est choisi de façon aléatoire et chaque sac a la même probabilité d'être choisi.

$$ \frac {1}{k ^ n} $$

#### Q 2.2. Quel serait le schéma d’un algorithme non déterministe polynomial pour le problème ?
On peut utiliser un algorithme non déterministe polynomial pour le problème en générant un certificat aléatoire, et en vérifiant si ce certificat est valide.

### Question 3 : NP ⊂ EXPTIME

#### Q 3.1. Pour n et k fixés, combien de valeurs peut prendre un certificat ?
Un certificat peut prendre k^n valeurs. En effet, pour chaque objet, il y a k sacs possibles.

#### Q 3.2. Enumération de tous les certificats. Quel ordre proposez-vous pour parcourir tous les certificats ?
Le premier certificat sera celui où tous les objets sont dans le premier sac, le dernier certificat sera celui où tous les objets sont dans le dernier sac.

Entre temps on peut parcourir tous les certificats en incrémentant le certificat précédent.

Par exemple, si on a 3 objets et 2 sacs, on aura les certificats suivants :
- [0, 0, 0]
- [1, 0, 0]
- [0, 1, 0]
- [1, 1, 0]
- [0, 0, 1]
- [1, 0, 1]
- [0, 1, 1]
- [1, 1, 1]

#### Q 3.3. L'algorithme du British Museum : Comment déduire de ce qui précède un algorithme pour tester si le problème a une solution ? Quelle complexité a cet algorithme ?
On peut déduire de ce qui précède un algorithme pour tester si le problème a une solution en parcourant tous les certificats et en vérifiant si un certificat est valide.

Cet algorithme a une complexité de O(k^n).

### Question 4 : Implémentation 
cf BinPack.py

## 2 - Réductions polynomiales

### Question 1 : Montrer que Partition se réduit polynomialement en BinPack.

On cherche une fonction de réduction permettant de résoudre le problème Partition en un problème BinPack.

Pour cela, il faut adapter les données du problème Partition pour qu'elles soient compatibles et utilisables avec le problème BinPack.
    
| Partition                                                                          | BinPack                                  |
|------------------------------------------------------------------------------------|------------------------------------------|
| n -> un nombre d'entiers                                                           | n -> nombre d'objets                     |
| 2 -> nombre de sacs                                                                | k -> nombre de sacs                      |
| (sum(x1, x2, ..., xn)/2 + sum(x1, x2, ..., xn)%2]) -> la moitié de la somme des xi | c -> capactité d'un sac                  |
| [x1, x2, ..., xn] -> les entiers                                                   | [x1, x2, ..., xn] -> le poids des objets |

Résoudre le problème Partition revient à résoudre le problème BinPack suivant :
- On cherche à savoir s'il existe un sac de capacité égale à la moitié de la somme des objets.
- Si oui, alors il existe une partition des objets en deux groupes de poids égaux.
- Sinon, alors il n'existe pas de partition des objets en deux groupes de poids égaux.

#### Q 1.1. Implémenter la réduction polynomiale de Partition dans BinPack
    
    ```python
    def reductionPartition(nombre_objets, nombre_sacs, capacite, poids):
        capacite = sum(poids) // 2 + sum(poids) % 2
        return nombre_objets, nombre_sacs, capacite, poids
    ```

#### Q 1.2. La propriété Partition est connue NP−complète. Qu’en déduire pour BinPack ?
La propriété Partition est connue NP−complète, donc BinPack est NP−complète puisque Partition se réduit polynomialement en BinPack.

#### Q 1.3. Pensez-vous que BinPack se réduise polynomialement dans Partition ? Pourquoi ?
On ne pense pas que BinPack se réduise polynomialement dans Partition, car on ne peut pas adapter les données du problème BinPack pour qu'elles soient compatibles et utilisables avec le problème Partition.

### Question 2 : Entre Sum et Partition, lequel des deux problèmes peut être presque vu comme un cas particulier de l’autre ? Qu’en déduire en termes de réduction ?
Partition peut être vu comme un cas particulier de Sum, car on cherche à savoir s'il existe un sous-ensemble de poids égal à la cible donnée en paramètre.

Il suffit de modifier un peu les données pour que la cible recherchée dans Sum correspondent à la moitié de la somme des objets dans Partition.

### Question 3 : Montrer que Sum se réduit polynomialement en Partition.

On cherche une fonction de réduction permettant de résoudre le problème Sum en un problème Partition.

Pour cela, il faut adapter les données du problème Sum pour qu'elles soient compatibles et utilisables avec le problème Partition.

| Sum                                                                   | Partition                        |
|-----------------------------------------------------------------------|----------------------------------|
| n -> nombre d'entiers                                                 | n -> nombre d'entiers            |
| [x1, x2, ..., xn] + [2*cible - somme(x1, x2, ..., xn)] -> les entiers | [x1, x2, ..., xn] -> les entiers |
| cible -> un entier cible                                              | (sum(x1, x2, ..., xn)/2 + sum(x1, x2, ..., xn)%2])                |

Résoudre le problème Sum revient à résoudre le problème Partition suivant :
- On cherche à savoir s'il existe un sous-ensemble de poids égal à la moitié de la somme des objets.
- Si oui, alors il existe une partition des objets en deux groupes de poids égaux.
- Sinon, alors il n'existe pas de partition des objets en deux groupes de poids égaux.

:warning: On a ajouté une valeur à la liste des entiers pour que la somme des entiers soit égale à 2*cible.

valeur ajoutée:

$$ 2\times c - \sum_{i=1}^{n}(xi) $$

### Question 4 : En utilisant la réduction précédente, comment implémenter une réduction polynomiale de Sum dans BinPack ?

On cherche une fonction de réduction permettant de résoudre le problème Sum en un problème BinPack.

Pour cela, il faut adapter les données du problème Sum pour qu'elles soient compatibles et utilisables avec le problème BinPack.

| Sum                                                                   | BinPack                                  |
|-----------------------------------------------------------------------|------------------------------------------|
| n -> nombre d'entiers                                                 | n -> nombre d'objets                     |
| [x1, x2, ..., xn] + [2*cible - somme(x1, x2, ..., xn)] -> les entiers | [x1, x2, ..., xn] -> le poids des objets |
| 2                                                                     | k -> nombre de sacs                      |
| cible -> un entier cible                                              | c -> capactité d'un sac                  |

Résoudre le problème Sum revient à résoudre le problème BinPack suivant :
- On cherche à savoir s'il existe un sac de capacité égale à la moitié de la somme des objets.
- Si oui, alors il existe une partition des objets en deux groupes de poids égaux.
- Sinon, alors il n'existe pas de partition des objets en deux groupes de poids égaux.

### Question 5 : Proposer une réduction polynomiale de BinPackDiff dans BinPack (inutile de l’implémenter)

On cherche une fonction de réduction permettant de résoudre le problème BinPackDiff en un problème BinPack.

Pour cela, il faut adapter les données du problème BinPackDiff pour qu'elles soient compatibles et utilisables avec le problème BinPack.

| BinPackDiff                                                   | BinPack                                  |
|---------------------------------------------------------------|------------------------------------------|
| n -> nombre d'objets                                          | n -> nombre d'objets                     |
| [x1, x2, ..., xn] -> le poids des objets                      | [x1, x2, ..., xn] -> le poids des objets |
| k -> nombre de sacs                                           | k -> nombre de sacs                      |                        
| min([c1, c2, ..., ck]) -> le sac avec la plus petite capacité | c -> capactité d'un sac                  |

Résoudre le problème BinPackDiff revient à résoudre le problème BinPack suivant :
- On cherche à savoir s'il existe une solution en modifiant la donnée de telle sorte à ce que la capacité d'un sac soit égale à la plus petite capacité des sacs.
- Si oui, alors il existe une solution.
- Sinon, alors il n'existe probablement pas de solution.

## 3. Optimisation versus Décision

### Question 1 : Montrer que si BinPackOpt1 (resp. BinPackOpt2) était P, la propriété BinPack le serait aussi ; qu’en déduire pour BinPackOpt1 (resp. BinPackOpt2) ?

Si BinPackOpt1 (resp. BinPackOpt2) était P, cela impliquerait qu'il existe un algorithme polynomial qui résout le problème BinPackOpt1 (resp. BinPackOpt2).

On remarque ici que, lors du calcul de BinPackOpt1 (resp. BinPackOpt2), on calcule BinPack également.

La complexité de BinPack est donc inférieure ou égale à celle de BinPackOpt1 (resp. BinPackOpt2).

Or, on sait que BinPackOpt1 se résout en un temps polynomial.

Ainsi : Si BinPackOpt1 (resp. BinPackOpt2) était P, la propriété BinPack le serait aussi.

De plus, 
Si BinpackOpt2 est P, 
Binpack est P également, car BinPackOpt2 nous fourni directement une mise en sacs correcte optimale,
c'est donc le certificat valide pour BinPack.

### Question 2 : Montrer que si la propriété BinPack était P, BinPackOpt1 le serait aussi

Si Binpack est P, 
BinPackOpt1 l'est également, 
car nous pouvons faire une boucle qui prend une variable (nombre de sacs) 
et l'incrémente à chaque itération pour le donner en paramètre à Binpack jusqu'à ce qu'on obtienne une mise en sachets valide. 
La valeur de la variable pour laquelle nous aurions notre première mise en sachets valide, 
est notre nombre de sachets minimum.

### Question 3 : Montrer que si la propriété BinPack était P, BinPackOpt2 le serait aussi

Nous avons vu ci-dessus que si Binpack est P, nous avons le nombre minimum de sachets.  
Or, si nous avons notre nombre minimum de sachets, 
il n'y a plus qu'un trouver un certificat valide avec le nombre de sachets minimal pour avoir la mise en sachets correcte qui minimise le nombre de sachets.

