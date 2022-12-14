# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

joululalenteri 1
"""

inc = 0
m = 0
with open("D:\joulukalenteri2021\kaikuluotain.txt") as f:
        
    for i, line in enumerate(f):
        if i != 0:
            t = int(line) - m
            if t > 0:
                inc += 1
        m = int(line)
        
    print(inc)