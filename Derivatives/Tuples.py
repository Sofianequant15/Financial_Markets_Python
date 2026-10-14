#TUPLES

#Définition : collection ordonnée d'éléments ne pouvant être modifiable

mon_tuple = (10, "Hello", False, 2.5)

try : 
    mon_tuple[1]= 0
except : 
    print("l'affectation n'est pas possible")

#Affectation multiple

(action1, variations) = (100, 1)
print(type((action1, variations)))

def simulation(price):
    new_price = price + 10
    variations = (new_price - price)/price
    return (new_price, variations)

(action1, variations)  = simulation(100)

print(action1, variations)

