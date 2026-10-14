#NUMPY

import numpy as np

"""
4- Modification de la forme d'un tableau
    * Utilisez reshape() pour changer la forme d'un tableau sans modifier ses données.
    * Obtenir un tableau à plusieurs dimensions sur une seule dimension
    * Astuce : Avoir un 1 à la place d'une virgule pour les tuples de dimension 1.
    * Astuce : Faire disparaître le 1
"""

#Créer un tableau NumPy 4x3
a = np.array([[0, 2, 8], [4, 8, 2], [0, 7, 5], [1, 4, 2]])

#Redimensionner mon tableau 
b = a.reshape(2,6)
print(b)

#Obtenir un tableau de dimension 1 à partir d'un tableau à plusieurs dimensions
c = b.ravel()
print(c)
print(c.shape)

#Astuce 1
c = c.reshape(c.shape[0],1)
print(c.shape)

#Astuce 2
c = c.squeeze()
print(c.shape)

