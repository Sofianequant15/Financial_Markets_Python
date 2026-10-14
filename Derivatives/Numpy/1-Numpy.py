#NUMPY

"""

Qu'est-ce que NumPy?

    * NumPy est une bibliothèque Python open source, un des packages les plus importants de Python.
    * NumPy est une puissante bibliothèqe Python pour le calcul numérique.
    * Le nom "NumPy" est dérivé de "Numerical Pythoon".
Quels sont les avantages de NumPy par rapport aux listes Python ? 
    * Les tableaux NumPy sont plus rapides et plus efficaces que les listes Python en termes de mémoire et de performance.
    * NumPy offre une syntaxe plus simple pour effectuer des opérations mathématiques complexes sur des tableaux.
    * Elle fournit un objet tableau à N dimensions appelé ndarray.
    * NumPy est très utilisé en finance de marché pour manipuler et analyser des données financières.
Installation de Numpy ?
    * Exécutez la commande suivante dans votre terminal : pip install numpy
"""

#Importez numpy
import numpy as np

"""
1- Création de tableaux
np.array() crée un tableau NumPy à partir d'une liste ou d'un tuple.
    dtype: spécifie le type de données du tableau, tel que int, flaot, complex, bool, str, etc. typle léger/ rapide et lourd
    copy: spécifie si le tableau doit être copié ou pas. La valeur par défaut est True.
    order: spécifie la façon dont les éléments du tableau sont stockés en mémoire.
"""

# Créer un tableau NumPy à partir d'une liste
a = np.array([0, 1, 2, 3])
print(a)
print(type(a))

# Créer un tableau NumPy à partir d'un tuple
b = np.array((5, 6, 7, 8))
print(b)

# Créer un tableau avec 2 lignes et 4 colonnes

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

# Créer un tableau de 3x3 rempli de zéros
a = np.zeros((3,3))
print(a)
a = np.ones((4,3))
print(a)

# Créer une matrice identité de dimension n avec n le nombre d'éléments que l'on souhaite avoir sur la diagonale
a = np.eye(3)
print(a)

"""
np.arange() crée un tableau avec une séquence d'entiers.
    start: spécifie le premier nombre dans séquence. La valeur par défaut est 0.
    stop: spécifie le dernier nombre dans la séquence (non inclus).
    step: spécifie l'incrément entre les nombres dans la séquence. La valeur par défaut est 1.
    dtype: spécifie le type de données du tableau, tel que int, float, complex, bool, str, etc.
"""
# Créer un tableau avec une séquence d'entiers de 0 à 4
a = np.arange(5)
print(a)

# Créer un tableau avec une séquence d'entiers de 3 à 9 avec un pas de 2
a = np.arange(3, 10, 2)
print(a)

"""
np.linspace() crée un tableau avec un nombre spécifique d'éléments espacés uniformément entre deux valeurs.
    * start: spécifie la première valeur de la séquence.
    * stop: spécifie la dernière valeur de la séquence.
    * num: spécifie le nombre d'éléments dans la séquence.
    * endpoint: spécifie si stop est inclus dans la séquence ou pas. La valeur par défaut est True. 
    * retstep: spécifie si la taille de l'étape doit être retournée. La valeur par défaut est False.
    * dtype: spécifie le type de données du tableau, tel que int, float, complex, bool, str, etc. 
"""

# Créer un tableau avec 5 éléments espacés uniformément entre 0 et 1
a = np.linspace(0, 1, 5)
print(a)

# Créer un tableau avec 10 éléments espacés uniformément entre -1 et 1
b = np.linspace(-1, 1, 10)
print(b)

np.random.seed(10)
a = np.random.randn(4,4)
print(a)

print(np.random.randint(10, 20, (3,3)))



