# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:50:31 2021

@author: Kaisa Ylikoski
"""

from enum import Enum

class Direction(Enum):
    UP = 'up'
    FORWARD = 'forward'
    DOWN = 'down'

fw = 0
depth = 0
aim = 0
with open("2.1.txt") as f:
        
    for i, line in enumerate(f):
        l = line.split(" ")
        direction = Direction(l[0])
        amount = int(l[1])

        if direction == Direction.FORWARD:
            fw += amount
            depth += amount * aim
        if direction == Direction.DOWN:
            #d += amount
            aim += amount
        if direction == Direction.UP:
            #d -= amount
            aim -= amount
        
    print(fw*depth)
    