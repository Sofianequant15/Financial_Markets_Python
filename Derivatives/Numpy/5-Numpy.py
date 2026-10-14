import numpy as np

# Créer deux tableaux NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

"""
Opérations sur les tableaux NumPy :
    * Opérations arithmétiques élémentaires (+, -, *, /)
    * Comparaison avec des listes
"""

# Opérations arithmétiques élémentaires
c = a + b #Addition
print(c)

d = b - a #Soustraction
print(d)
e = a * b #Multiplication
print(e)
f = b / a #Division
print(f)

#Comparaison liste
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(liste1+liste2)

try:
    print(liste1-liste2)
    print(liste1*liste2)
    print(liste1/liste2)
except:
    print("impossible")
    