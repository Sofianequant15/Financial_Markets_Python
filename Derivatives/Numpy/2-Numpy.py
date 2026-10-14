#NUMPY
import numpy as np
"""
2- Propriété des tableaux
    * size est un attribut qui renvoie la taille d'un tableau.
    * shape est un argument ou attribut qui spécifie la forme (dimensions) du tableau NumPy.
    Remarque : Le output de "shape" est un tuple.
    * dtype est un argument qui spécifie le type de données du tableau NumPy
"""

# Créer un tableau NumPy à partir d'une liste de nombres flottants
a = np.array([[1.2, 3.4, 5.6, 7.8],[3.1, 4.5, 8.4, 9.2]])

# Vérifier la taille (nombre total d'éléments) du tableau
print("La taille du tableau est:", a.size)

# Vérifier la forme (dimensions) du tableau
print("La forme du tableau est:", a.shape)

# Vérifier le type de données du tableau
print("Le type de données du tableau est:", a.dtype)


