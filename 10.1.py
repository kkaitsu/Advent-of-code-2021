# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:36:24 2021

@author: Kaisa Ylikoski
"""

with open("10.1.txt") as f:

    sulut = []
    for i, rivi in enumerate(f):
        sulut.append(rivi[:-1])
        
parit = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'}
    
auki = '([{<'    
virheet = ''
for rivi in sulut:
    l = ''
    for item in rivi:
        if auki.find(item) != -1:
            l = l+item
        else:
            if parit[item] != l[-1]:
                virheet = virheet + item
                print(item, rivi)
                break
            else:
                l = l[:-1]
                
summa = virheet.count(')')*3 + virheet.count(']')*57 + \
    virheet.count('}')*1197 + virheet.count('>')*25137

print(summa)
    # ): 3 points.
    # ]: 57 points.
    # }: 1197 points.
    # >: 25137 points.

        

