import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))

"""
Début :
    plt.figure()
Contenu : 
    plt.plot() ou plt.subplot(lignes, colonnes, position)
    plt.xlabel()
    plt.ylabel()
    plt.title()
    plt.legend() (en indiquant le label dans plt.plot())
Affichage :
    plt.show()
Sauvegarder :
    plt.save('exemple.png')
"""

x = np.linspace(0, 2, 10)
y = x**2
z = x**3
#Début
plt.figure(figsize=(12,8))

#Contenu
plt.plot(x, y,label='fonction quadratique')
plt.plot(x, z,label='fonction cubique')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()
plt.title('Courbe quadratique & cubique')

#Affichage
plt.show()

#Sauvegarder le graphique
plt.savefig('test.png')


