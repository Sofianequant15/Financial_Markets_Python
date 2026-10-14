# VARIABLES 

#Definition : Une variable est une zone de la mémoire de l'ordinateur dans laquelle une valeur est stockée

age_chien = 10

"""
pour nommer une variable : 
    -La variable doit commencer par une lettre ou un underscore
    -La variable ne doit pas contenir d'effet spéciaux
    -La variable ne doit pas contenir d'espace mais (_) valide
    -La variable doit être explicite (capable de commenter votre code)
    -Une valeur est affectée à une variable par le biais d'un =
    """

#Exemples de notation pour des variables
ageChien1 = 1
age_chien2 = 2.5 #recommandé
agechien3 = "3"
AgeChien4 = False

#Il est recommandé de garder la même syntaxe dans tout votre projet

"""
Les différents types de données standards :
    - entier numérique (int pour integer)   = 14
    - nombre flottant (float)               = 3.5
    - chaîne de caractère (str pour string) = 'Hello world'
    - booléen (bool pour boolean)           = False
    - autres (listes, dictionnaires, tuples etc...)
"""
#Afficher les variables avec la fonction print
print(ageChien1)
print("le chien est agé de", age_chien2, "ans")
print("le chien est agé de", agechien3, "ans")
print(AgeChien4)

#Afficher le type d'une donnée avec la fonction type
print(type(ageChien1))
print(type(age_chien2))
print(type(agechien3))
print(type(AgeChien4))

#Changer le type d'une donnée : 
print(type(str(ageChien1)))
print(type(int(age_chien2)))
print(type(bool(agechien3)))
print(type(float(AgeChien4)))

"""
Les fonctions : 
- print() : affiche à l'écran
- type() : afficher le type d'une donnée
- int(), float(), str(), bool() : convertir une donnée
"""