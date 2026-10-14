import numpy as np

# Créer deux tableaux NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Calculer l'exponentielle de chaque élément du tableau
b = np.exp(a)
print(b)
# Calculer le logarithme de chaque élément du tableau
b = np.log(a)
print(b)

#Calculer la somme, moyenne, min & max
total = a.sum(axis=0) #somme selon l'axe vertical
print(total)
col_means = np.mean(a, axis=0) #moyenne selon l'axe vertical
print(col_means)
min_val = np.min(a) #min
print(min_val)
var = a.var() #variance
print(var)
std = a.std() #ecart-type
print(std)

#Création d'une matrice 3x3
a = np.random.randint(10, 30, (3,3))
print(a)

# Produit cumulé
print(np.cumprod(a, axis=1))
print(np.cumprod(a, axis=0))
#Somme cumulée
print(np.cumsum(a, axis=1))
print(np.cumsum(a, axis=0))

# Matrice de corrélation
matrice_correlation = np.corrcoef(a) #correlation entre les elements de a
print(matrice_correlation)

# Afficher les elements uniques d'un tableau
a = np.random.randint(10, 15, (3,3))
print(a)

unique = np.unique(a)
print(unique)

# Nan
a = np.random.randn(3,3)
a[0:2, 1:3]= np.nan

# Calcul d'une moyenne
print(np.mean(a))
print(np.nanmean(a))

# Manipuler les nan
print(np.isnan(a))
print(np.isnan(a).sum())
a[np.isnan(a)] = 5
print(a)

