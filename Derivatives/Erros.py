#ERRORS

def diviser(a,b):
    try : 
        result = a/b
    except ZeroDivisionError:
        print("La division par zéro n'est pas possible en maths")
    except TypeError:
        print("Veuillez saisr un nombre")
    else: 
        print("le résultat est", result)
    finally:
        print("fin du programme")
"""
Les différentes erreurs (ou exceptions):
    ValueError
    NameError
    TypeError
    ZeroDivisionError
    OSError
    AssertionError
    
    """


#variable = "3"
#print(diviser(10,variable))

#def diviser(a,b):
    #if b == 0:
    #    raise ZeroDivisionError("La division par zéro n'est pas possible en maths")
    #else:
    #    resultat = a/b
    #    return resultat

#def diviser(a,b):
    # assert b != 1, "Division par 1 trop facile !"
    # resultat = a/b
    # return resultat

print(diviser(10,1))


