# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:00:09 2021

@author: Kaisa Ylikoski
"""
from enum import Enum

class Direction(Enum):
    UP = 'up'
    FORWARD = 'forward'
    DOWN = 'down'

fw = 0
d = 0
with open("2.1.txt") as f:
        
    for i, line in enumerate(f):
        l = line.split(" ")
        direction = Direction(l[0])
        amount = int(l[1])
        print(amount)
        

        if direction == Direction.FORWARD:
            fw += amount
        if direction == Direction.DOWN:
            d += amount
        if direction == Direction.UP:
            d -= amount
        
    print(fw*d)
    