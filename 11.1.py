# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:30:21 2021

@author: Kaisa Ylikoski

11.1 ja 11.2
"""
from copy import deepcopy


def ympäröivät(valot, i, j,flashes):
    flashes[0] += 1
    valot[i][j] = 0
    
    #print('i', i,j)
    if i >-1 and j > -1:

        apu((i-1),(j-1),valot, flashes)
        apu(i-1,j,valot, flashes)
        apu(i-1,j+1,valot, flashes)
        apu(i,j-1,valot, flashes)
        apu(i,j+1,valot, flashes)
        apu(i+1,j-1,valot, flashes)
        apu(i+1,j,valot, flashes)
        apu(i+1,j+1,valot, flashes)
        
            
def apu(i2, j2, valot, flashes):
    #print('i2' , i2,j2)
    try:
        if i2 > -1 and j2 > -1:
            if valot[i2][j2] != 0:
                valot[i2][j2] += 1
                if valot[i2][j2] > 9:
                    ympäröivät(valot, i2, j2, flashes) 
    except:
            pass

with open("11.1.txt") as f:

    valot = []
    valot_all = []
    for i, rivi in enumerate(f):
        valot_rivi = [int(x) for x in rivi[:-1]]
        valot.append(valot_rivi)

flashes = [0]
valot_all.append(deepcopy(valot))

#kierrokset
for s in range(10000):
    apu3 = 0
    for i, rivi in enumerate(valot):
        for j, item in enumerate(rivi):
            valot[i][j] += 1
    for i, rivi in enumerate(valot):
        for j, item in enumerate(rivi):
            if valot[i][j] > 9:
                ympäröivät(valot,i,j,flashes)
    valot_all.append(deepcopy(valot))
    for rivi in valot:
        for item in rivi:
            if item == 0:
                apu3 += 1
    if apu3 == 100:
        print(s+1)
        break
            

#print(flashes[0])
            
    
        
#1444 too low