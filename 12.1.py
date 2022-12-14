# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:09:16 2021

@author: Kaisa Ylikoski
"""

from copy import deepcopy

with open("12.2.txt") as f:
    tunneli = []
    for i, rivi in enumerate(f):
        pari = rivi.strip().split('-')
        tunneli.append((pari[0],pari[1]))

#jos luola ei ole start
#jos lopussa ei ole end
#jos pikkutunneli ei ole jo listassa  
#jos tunnelijonon vika alkio on sama kuin luola
#--> True      
def kelpaako(tunnelit, luola, luola2, key):
    apu = True
    if tunnelit[key][-1] != luola:
        apu = False
        return apu
    if luola == 'start' or luola2 == 'start':
        apu = False
        return apu
    if tunnelit[key][-1] == 'end':
        apu = False
        return apu
    #älä käy pienissä luolissa kahdesti
    if tunnelit[key].count(luola2) > 0 and luola2.islower():
        apu = False
        return apu
        
    else:
        return apu
        
def rekursio(tunnelit, tunneli):
  
    for key in tunnelit:
        for rivi in tunneli:
            luola = rivi[0]
            luola2 = rivi[1]
            if kelpaako(tunnelit, luola, luola2, key):
                tunnelit[key].append(luola2)
                rekursio(tunnelit, tunneli)
            if tunnelit[key][-1] == 'end':
                return
        

def yhdistä_verkosto(tunneli):
    tunnelit = {}
    a = True
    i = 0
    while a == True:
        for rivi in tunneli:
            i += 1
            if rivi[0] == 'start':
                tunnelit[i] = ['start']
                tunnelit[i].append(rivi[1])
                rekursio(tunnelit, tunneli)
            # elif rivi[1] == 'start':
            #     tunnelit[i] = ['start']
            #     tunnelit[i].append(rivi[0])
                
            # for key in tunnelit:
            #     if kelpaako(tunnelit, rivi[0], rivi[1], key):
            #         tunnelit[key].append(rivi[1])
            #     if kelpaako(tunnelit, rivi[1], rivi[0], key):
            #         tunnelit[key].append(rivi[0])

        if i > 100:    
            a = False
    return tunnelit         
        
    
    
    
    
    
tunnelit = yhdistä_verkosto(tunneli)
print(tunnelit)