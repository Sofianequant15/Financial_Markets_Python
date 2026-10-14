import numpy as np

# Créer deux tableaux NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Calculer le produit vectoriel entre a et b 
c = np.cross(a,b)
print(c)

# Calculer le produit scalaire entre a et b
c = np.dot(a, b)
print(c)

# Créer deux matrices NumPy
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7,8]])

# Calculer le produit matriciel entre A et B
C = np.dot(A, B)
print(C)

#Tri et recherche
arr = np.array([5, 2, 8, 1, 4])

#Tri des valeurs
sorted_arr = np.sort(arr)
print(sorted_arr)

#Tri selon les indices qui trieraient le tableau
sorted_indices = np.argsort(arr)
print(sorted_indices)

#Obtenir les indices des valeurs minimales et maximales du tableau
min_index = np.argmin(arr)
max_index = np.argmax(arr)
print(min_index)
print(max_index)

arr2 = np.array([[5, 2, 8, 0, 4],
                 [12, 2, 8, 1, 14]])

#Tri des valeurs
sorted_arr2 = np.sort(arr2)
print(sorted_arr2)

#Tri selon les indices qui trieraient le tableau
sorted_indices = np.argsort(arr2)
print(sorted_indices)

#Obtenir les indices des valeurs minimales et maximales du tableau
min_index2 = np.argmin(arr2)
max_index2 = np.argmax(arr2)
print(min_index2)
print(max_index2)


