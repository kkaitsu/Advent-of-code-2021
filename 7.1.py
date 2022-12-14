# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:49:48 2021

@author: Kaisa Ylikoski
"""
import numpy as np

with open("7.1.txt") as f:

    positions = f.read()
    positions = positions.split(',')
    positions = [int(x[:,-1]) for x in positions]


median = np.median(positions)

fuel = 0
for i,position in enumerate(positions):
    fuel += abs(position-median)
    
print(fuel)