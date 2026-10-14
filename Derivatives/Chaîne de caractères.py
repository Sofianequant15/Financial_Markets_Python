#LES CHAINES DE CARACTÈRES

#Définition : Une suite ordonnée de caractère que l'on définit avec""

"""

Transformer des chaînes de caractères
    str.upper()         --> Majuscules
    str.lower()         --> Minuscules
    str.capitalize()    --> Première lettre en Maj
    str.title()         --> Première lettre de chaque mot en Maj
    str.index()         --> Retourne l'indice d'un caractère dans une chaîne de caractère
    str.replace()       --> Remplace un caractère par un autre
    str.islower()       --> Vérifie si la chaîne est en minuscules
    str.isupper()       --> Vérifie si la chaîne est en majuscules
    
"""

ma_chaine = "Hello derivatives"

#print(ma_chaine.upper())
#print(ma_chaine.lower())
#print(ma_chaine.capitalize())
#print(ma_chaine.title())

"""

Ces méthodes ne travaillent pas sur la chaîne elle-même mais sur une copie de la chaîne
"""

#ch2 = ma_chaine
#print(ma_chaine)
#print(ch2)

#ma_chaine = ma_chaine.upper()

#print(ma_chaine)
#print(ch2)

#print(ma_chaine.replace("e", "a", 1))

#print(ma_chaine.index(("Hello")))

ma_chaine = ma_chaine.lower()
if ma_chaine.islower() :
    print("C'est en minuscules")


