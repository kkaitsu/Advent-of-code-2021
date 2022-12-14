# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:40:57 2021

@author: Kaisa Ylikoski
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:28:53 2021

@author: Kaisa Ylikoski
"""

import numpy as np


def isoin_lista(lista):
    for i in range(0,12):
        column = [x[i] for x in lista]
        
        if column.count('0') > column.count('1'):
            index = np.where(np.array(column) == '0')[0]
            lista = [lista[i] for i in index]
            
        if column.count('1') >= column.count('0'):
            index = np.where(np.array(column) == '1')[0]
            lista = [lista[i] for i in index]
            
        if len(lista) == 1:
            break
    return(lista)
    
def pienin_lista(lista):
    for i in range(0,12):
        column = [x[i] for x in lista]
        
        if column.count('0') <= column.count('1'):
            index = np.where(np.array(column) == '0')[0]
            lista = [lista[i] for i in index]
            
        if column.count('1') < column.count('0'):
            index = np.where(np.array(column) == '1')[0]
            lista = [lista[i] for i in index]
            
        if len(lista) == 1:
            break
    return(lista)    
    
with open("3.1.txt") as f:
    l = [str(line) for line in f]
    oxygen = isoin_lista(l)
    co2 = pienin_lista(l)
    
    print(int(oxygen[0][:-1], 2)*int(co2[0][:-1], 2))
    

