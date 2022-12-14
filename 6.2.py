# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:11:57 2021

@author: Kaisa Ylikoski
"""
from scipy.optimize import curve_fit
import numpy as np

# class Kala:
#     def __init__(self, alkuarvo = None):
#         self.kunnes = 9
#         if alkuarvo:
#             self.kunnes = alkuarvo
        
#     def __repr__(self):
#         return f'Kala {self.kunnes}'
        
#     def pienene_yksi(self):
#         self.kunnes -= 1
#         if self.kunnes == -1:
#             self.kunnes = 6
#             return Kala()


with open("6.1.txt") as f:

    iät = f.read()
    iät = iät.split(',')
    iät = [int(ikä) for ikä in iät]

    #ämpärit[0] on 0 ikäisien kalojen lkm
    ämpärit = [0,0,0,0,0,0,0,0,0]
    ämpärit_apu = ämpärit
    for i in iät:
        ämpärit[i] += 1
        
    #päivien lisäyksiä
    for i in range(256):
       ämpärit_apu = [0,0,0,0,0,0,0,0,0]
       ämpärit_apu[8] = ämpärit[0]
       ämpärit_apu[6] = ämpärit[0]
       ämpärit_apu[0] = ämpärit[1]
       ämpärit_apu[1] = ämpärit[2]
       ämpärit_apu[2] = ämpärit[3]
       ämpärit_apu[3] = ämpärit[4]
       ämpärit_apu[4] = ämpärit[5]
       ämpärit_apu[5] = ämpärit[6]
       ämpärit_apu[6] += ämpärit[7]
       ämpärit_apu[7] = ämpärit[8]

       ämpärit = ämpärit_apu

    print(sum(ämpärit))
        
    
    
    #"{:.8f}".format(float(m))
    #np.polyfit(np.exp(kalojen_määrä_x), kalojen_määrä, 1)