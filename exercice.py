#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, "C:\Poly\A20\INF1007\c04-ch6-exercices-Elleiluj")
from exercice2 import frequence


# TODO: Définissez vos fonction ici
def masse_volume(a=5,b=10,c=4,masse_volumique=120):
    Volume = 4 * a * b * c * math.pi / 3
    Masse = Volume * masse_volumique
    return Volume, Masse



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(masse_volume())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("Bonjour, comment vas-tu"))
    pass
