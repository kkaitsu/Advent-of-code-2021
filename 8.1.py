# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:05:20 2021

@author: Kaisa Ylikoski
"""

output = []

with open("8.1.txt") as f:

    for i, digitals in enumerate(f):
        digitals = digitals.split('|')
        output.append(digitals[1][:-1].split(' '))
    summa = 0
    for rivi in output:

        for digit in rivi:
            p = len(digit)
            if p== 2 or p == 3 or p== 4 or p==7:
                summa += 1
            
    print(summa)