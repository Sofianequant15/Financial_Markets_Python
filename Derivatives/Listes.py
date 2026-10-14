#Listes

#Définition : C'est une collection ordonnée d'éléments pouvant être de différents types

liste_vide = []
liste = [1, "Hello", 2.5, True]

"""

Les différents moyens d'accéder à des éléments pour une liste
    liste[X]   --> Afficher l'élément d'indice X
    liste[-X]  --> Afficher Xème élément en partant de la fin
    liste[:]   --> Afficher tous les éléments
    liste[:X]  --> Afficher tous les X premiers éléments
    liste[X:]  --> Afficher les X derniers éléments
    liste[X:Y] --> Afficher de l'élément d'indice X à l'indice d'élément Y (exclus)
"""
#print(liste[1])
#print(liste[-1])
#print(liste[:])
#print(liste[:1])
#print(liste[1:])
#print(liste[1:3])

#Savoir si un élément est dans une liste ?
if "Hello" in liste:
    print("l'élément est dans la liste")

#Ajouter ou supprimer des éléments
liste.append(5)
print(liste)

liste.insert(2, "DERIVATIVES")
print(liste)

#Supprimer des éléments
liste.remove("DERIVATIVES")
print(liste)

del liste[4]
print(liste)

print(liste.index("Hello"))

#Trouver l'indice d'un élément dans une liste
print(liste.index("Hello"))

liste2 = liste[:]
liste2.append(10)

print(liste)
print(liste2)

liste_nb = [1, 5, 6, 2, 3, 15]

#concatenation

liste3 = liste + liste_nb
print(liste3)

#tri
liste_nb.sort()
print(liste_nb)

#inverser mes éléments
liste.reverse()
print(liste)

#bloucles et listes
for nb in liste_nb:
    if nb%2==0:
        print(nb, "est divisible par 2")

#compter les éléments d'une liste
liste4 = [1,0,0,0,1,0]
print(liste4.count(0))






