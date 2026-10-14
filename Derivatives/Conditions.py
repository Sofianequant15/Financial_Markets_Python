#CONDITIONS

"""

Les opérateurs de comparaison :
    == --> Egal à
    != --> Différent de
    < --> plus petit que
    > --> plus grand que
    <= --> plus petit ou égal à
    >= --> plus grand ou égal à
    """
"""
Exemple d'illustration :
   À t=0, mon action vaut 100€
   À t=1, mon action vaut 101€
   À t=2, mon action vaut 103€
   
   """
action_price0 = 100
action_price1 = 99
action_price2 = 103

#Calcul du return
return_t1 = ((action_price1 - action_price0) / action_price0) * 100
return_t2 = ((action_price2 - action_price1) / action_price1) * 100

print(return_t1, return_t2)

#Si mon return est supérieur à 1%, j'achète l'action, sinon je ne fais rien 
#if return_t1 >= 1 :
#    print("J'achète l'action")
#elif return_t1 >= 2 :
#    print("J'achète deux actions")    
#else : 
#    print("je n'achète pas l'action")

"""

Conditions multiples : 
    and --> et
    or --> ou
    in/not in --> dans/pas dans
    """
#Si mes deux returns consécutifs sont supérieurs à 1% alors j'achète l'action
#if return_t1 >= 1 and return_t2 >= 1 : 
#    print("J'achète l'action")

#Si un de mes deux returns est supérieur à 1% alors j'achète l'action
#if return_t1 >= 1 or return_t2 >= 1 :
#    print("J'achète l'action")

#Illustration in & not in : 
letter = "b"
voyelles = "aeiouy"

if letter not in voyelles :
    print("je suis une consonne")
    
    
