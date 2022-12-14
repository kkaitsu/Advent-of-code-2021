# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:56:28 2021

@author: Kaisa Ylikoski
"""
import numpy as np
from functools import reduce  # Required in Python 3
import operator

def laajene(i, j, taulukko, sapluuna):
    if i < 0 or j < 0:
        return sapluuna
    if taulukko[i][j] == 9:
        return sapluuna
    #print('i', i, 'j ',j)
    sapluuna[i][j] = 1
    
    laajentuakko(i,(i+1),j,(j),taulukko, sapluuna)
    laajentuakko(i,(i-1),j,(j),taulukko, sapluuna)
    laajentuakko(i,(i),j,(j+1),taulukko, sapluuna)
    laajentuakko(i,(i),j,(j-1),taulukko, sapluuna)
        
    return sapluuna
    
def onko_tyhjä(sapluuna, i, j):
    if sapluuna[i][j] == 0:
        return True
    return False
    
def laajentuakko(i,i2,j,j2,taulukko,sapluuna):
    try:
        if taulukko[i2][j2] > taulukko[i][j] and onko_tyhjä(sapluuna,i2,j2):
            laajene(i2,j2, taulukko,sapluuna)
    except:
        #print(i)
        pass
    
def prod(iterable):
    return reduce(operator.mul, iterable, 1)


sapluuna = []
hightsy = []
sapluunat = []
koot = []

with open("9.1.txt") as f:
    hights = []
    hightsy = []
    for i, rivi in enumerate(f):
        hight_row = [int(x) for x in rivi[:-1]]
        hights.append(hight_row)
    hightsy.append([x[i] for x in hights])

for i, rivi in enumerate(hights):
    for j, item in enumerate(rivi):
        s = 0
        sapluuna = [[0 for j in range(len(hights[0]))] for i in range(len(hightsy[0]))]
        sapluunat.append(laajene(i,j,hights,sapluuna))
        #for r in sapluuna:
        #    s += sum(r)
        s = sum([sum(rivi) for rivi in sapluuna])

        koot.append(s)
        
koot = np.array(koot)
koot = -np.sort(-koot)
print(prod(koot[:3]))
    