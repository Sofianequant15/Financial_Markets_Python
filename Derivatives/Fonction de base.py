#Fonction de base en python

#Les fondamentaux
x = -3.14
print(abs(x)) #valeur absolue
print(round(x,1)) #arrondi

liste = [-2, 3, -2, 1, 0, -4, True, False]
print(min(liste)) # minimum
print(max(liste)) # maximum
print(len(liste)) # longueur
print(sum(liste)) # somme des éléments
print(any(liste)) # y-a-t'il au moins un élément True ? 
print(all(liste)) # est-ce-que tous les éléments sont True ? 

#convertir un dictionnaire en liste : 
mon_dico = {"action":"tesla", "prix": 100}
print(list(mon_dico))
print(list(mon_dico.keys()))
print(list(mon_dico.values()))

#convertir une liste en dictionnaire : 
try:
    print(dict(liste))
except:
    print("impossible")

liste_keys = ["a", "b", "c", "d", "e"]
print(dict(zip(liste_keys, liste)))

#convertir une liste en un tuple: 
#print(tuple(liste))

#fonction input
age = input("quel âge avez-vous ?") #l'affichage du input est toujours en chaîne de caractères

#fonction format
action = "Tesla"
prix = 100
phrase1 = "Le prix de l'action {} est de {} euros".format(action,prix)
print(phrase1)
phrase2 = f"Le prix de l'action {action} est de {prix} euros"
print(phrase2)

"""
La fonction open : open(<nom du fichier>, <mode>)
    - le mode 'r' : lire un fichier de votre ordinateur
    - le mode 'w' : écrire un fichier sur votre ordinateur
    - le mode 'a' : (append) ajouter du contenu dans un fichier existant
"""

#Méthode 1 
#f = open('text.txt', 'w') # ouverture d'un objet fichier f
#f.write('hello')
#f.close() # il faut fermer notre fichier une fois le travail terminé

#Méthode 2 
with open('text.txt', 'r') as f:
    print(f.read())

#List Comprehension

import time

#exemple 1 
start = time.time()
liste_1 = []
for i in range(100000):
    liste.append(i**2)
end = time.time()
print(end - start)

#exemple 2
start = time.time()
liste_2 = [i**2 for i in range (100000)]
end = time.time()
print(end - start)

#exemple 2 avec une condition 
liste_2 = [i**2 for i in range (10) if i%2 ==0]
print(liste_2)

#Dict Comprehension
#Exercice : créer dictionaire avec clefs de 1 a 20 et comme valeur le carré de chaque clef

dictionnaire ={k : k**2 for k in range(1, 21)}






