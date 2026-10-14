#Fonctions

#Définition : ensemble d'instructions pour effectuer une tâche précise

def somme(nombre1=10, nombre2=15):
    return nombre1 + nombre2

print(somme())

#Exemple : Codez la fonction factorielle

def factorielle(n):
    if n<0 : 
        raise ValueError
    elif n==0 : 
        return 1
    else :
        result = 1
        for i in range(1,n+1):
            result *= i
        return result



