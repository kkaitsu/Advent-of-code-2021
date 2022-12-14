# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:44:25 2021

@author: Kaisa Ylikoski
"""
import numpy as np

with open("10.1.txt") as f:

    sulut = []
    for i, rivi in enumerate(f):
        sulut.append(rivi[:-1])
        
parit = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'}

parit2 = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'}
    
pisteet = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
    }
auki = '([{<'    
virheet = ''
l2 = ''
l2_all = []
l3 = []

for rivi in sulut:
    l = ''
    l2 = ''
    summa = 0
    apu = True
    for item in rivi:
        if auki.find(item) != -1:
            l = l+item
        else:
            if parit[item] != l[-1]:
                virheet = virheet + item
                apu = False
                break
            else:
                l = l[:-1]
    if apu:
        for i, it in enumerate(l):
            i += 1
            l2 = l2 + parit2[l[-i]]
        for i, it in enumerate(l2):
            summa = 5*summa + pisteet[it]
        l2_all.append(summa)
        l3.append(l2)
        
print(np.median(l2_all))
        
        
        

    # ): 1 point.
    # ]: 2 points.
    # }: 3 points.
    # >: 4 points.

            
                


        

