# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:11:57 2021

@author: Kaisa Ylikoski
"""

class Kala:
    def __init__(self, alkuarvo = None):
        self.kunnes = 9
        if alkuarvo:
            self.kunnes = alkuarvo
        
    def __repr__(self):
        return f'Kala {self.kunnes}'
        
    def pienene_yksi(self):
        self.kunnes -= 1
        if self.kunnes == -1:
            self.kunnes = 6
            return Kala()
    
    
with open("6.1.txt") as f:

    iät = f.read()
    iät = iät.split(',')
    iät = [int(ikä) for ikä in iät]
    kalat = []
    for i in iät:
        kalat.append(Kala(i))
        
    #päivien lisäyksiä
    for i in range(80):
        apu = []
        for kala in kalat:
            pienikala = kala.pienene_yksi()
            if pienikala:
                kalat.append(pienikala)
            apu.append(kala.kunnes)
        #print(apu)
    
    print(len(kalat))