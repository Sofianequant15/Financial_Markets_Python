#MODULES

"""
Définition : Ce sont des fichiers qui contiennent du code python et 
qui peuvent être utilisés dans d'autres programmes Python
"""

"""
Comment utiliser un module ? Il faut d'abord l'importer dans notre programme.
    - import nom_du_module
    - from nom_du_module import fonction
    - from nom_du_module import*
"""

import Autres.numerical as nl

print(nl.factorielle(4))

