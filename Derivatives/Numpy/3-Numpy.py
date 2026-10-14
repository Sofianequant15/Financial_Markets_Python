#NUMPY

import numpy as np

"""
3- Indexation et extraction de sous-tableaux
    * array[ligne:colonne] --> indexing
    * array[début:fin, début:fin] --> slicing (on peut également ajouter un pas)
    * Utilisez les indices et les tranches (slices) pour accéder aux éléments d'un tableau.
    * Utilisez les indices et les tranches (slices) pour extraire des sous-tableaux.
    * Boolean Indexing --> Permet de sélectionner uniquement les éléments qui répondent à certaines conditions spécifiques
"""

# Créer un tableau NumPy de 2x3 avec des nombres entiers aléatoires
a = np.random.randint(10, size=(2, 3))
print("Le tableau a est :\n", a)
np.random.seed(10)

# Accéder à un élément spécifique du tableau
print("L'élément à la position (0, 1) est :", a[0, 1])

# Accéder à une ligne spécifique ou colonne du tableau
print("La deuxième ligne du tableau est :", a[1, :])
print("La troisième colonne du tableau est :", a[:, 2])

# Extraire un sous-tableau à partir d'une tranche (slice) du tableau
print("Le sous-tableau a[0:2, 1:3] est :\n", a[0:2, 1:3])

# Boolean Indexing
print(a>5)
a = a[a>5]
print(a)
a = a[(a>5) & (a<7)]
print(a)



