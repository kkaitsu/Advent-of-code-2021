# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:57:55 2021

@author: Kaisa Ylikoski
"""

import numpy as np


def factorial(x): 
    result = x
    count = x-1
    while count > 0:
        result += count
        count -= 1
    return result

with open("7.1.txt") as f:

    positions = f.read()
    positions = positions.split(',')
    positions = [int(x) for x in positions]

#mean menetelmällä positio heittää yhdellä, hngh
mean = np.round(np.mean(positions))

fuel = 0
fuel_index = []

for j in range(max(positions)):
    fuel =0
    for i,position in enumerate(positions):
        #fuel += factorial(abs(position-mean))
        fuel += factorial(abs(position-j))
    fuel_index.append(fuel)
where = np.where(np.array(fuel_index)==min(fuel_index))

print(fuel_index[where[0][0]])
#wrong answer 90041060 too high

#np.mean menetalmän minimipositio: 465