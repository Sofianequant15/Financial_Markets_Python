#DICTIONNAIRES

#Définition : C'est une collection qui associe une clé à une valeur

mon_dico = {"action":"tesla","prix":100} #clés et valeurs peuvent être des listes, tuples etc.

#Accéder une valeur de mon dico

mon_dico["action"]
print(mon_dico["action"])

try:
    print(mon_dico[1])
except:
    print("impossible")

#Modifier une valeur de mon dico
mon_dico["prix"] = 500
print(mon_dico)

#Ajouter une valeur à mon dico
mon_dico["volume"] = "1mio"
print(mon_dico)

#Supprimer une valeur
mon_dico.pop("prix")
del mon_dico["volume"]

print(mon_dico)

#chercher une clé dans un dico
if "action" in mon_dico :
    print("oui")
else : 
    print("non")

#boucler sur les clés ou les valeurs
for key in mon_dico.keys():
    print(key)

for value in mon_dico.values():
    print(value)

#Afficher les clés et les valeurs
for key, value in mon_dico.items():
    print(key, value)

#Peut-on trier un dictionnaire ? Non

#Même problème qu'avec les listes pour la copie des dictionnaires
dico1 = mon_dico
dico2 = mon_dico.copy()
dico2["action"]="facebook"
print(dico2)
print(mon_dico)

dico1["action"]="facebook"
print(dico1)
print(mon_dico)

