# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

joululalenteri 1.2
"""

m = 0
l = []
with open("D:\joulukalenteri2021\kaikuluotain.txt") as f:
        
    l = [int(line) for line in f]
    
    for i in range(len(l)):
        if i > 2:
            if l[i]-l[i-3] > 0:
                print("i-2" , l[i-3])
                print("i", l[i])
                print ("erotus" , l[i]-l[i-3])
                m += 1
        
        
    print(m)