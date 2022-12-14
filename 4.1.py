# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:16:33 2021

@author: Kaisa Ylikoski
"""

from enum import Enum
import numpy as np
import math


def find_hits(ruudukko, luku):
    #indeksit joissa oikea luku sijaitsee
    index = np.where(np.array(ruudukko)==str(luku))[0]
    #oikeisiin indekseihin luku 1000
    for i in index:
        #käydään riviä läpiin
        for j, elem in enumerate(ruudukko[i]):
            if str(elem) == str(luku):
                ruudukko[i][j] = 1000
                #tarkista tuliko bingo
                osumat = np.where(np.array(ruudukko)=='1000')[0]
                for k in osumat:
                    #jos samalla rivillä on 5 osumaa -> bingo
                    if np.count_nonzero(k == osumat) == 5:
                        print("bingo!")
                        return(ruudukko, True, i)
    return(ruudukko, False, i)

#for i, line in enumerate(f):

    
ruudukkox = []
ruudukkoy = []
ruudukkoyapu = []
i2 = 0

with open("4.1.txt") as f2:
    ruudukkox = [str(line[:-1]) for line in f2]
    #poista tyhjät rivit
    ruudukkox = [x for x in ruudukkox if x]
    for i, line in enumerate(ruudukkox):
        ruudukkox[i] = ruudukkox[i].split(' ')
        #poista tyhjät
        ruudukkox[i] = [x for x in ruudukkox[i] if x]
        
    #tee pystyrivit sisältävä taulukko
    for i in range(0,5):
        ruudukkoyapu.append([x[i] for x in ruudukkox])
    #muotoile taulukko yhteneväksi ruudukkox kanssa
    for j in range(0,len(ruudukkox),5):
        ruudukkoy.append(ruudukkoyapu[0][j:j+5])
        ruudukkoy.append(ruudukkoyapu[1][j:j+5])
        ruudukkoy.append(ruudukkoyapu[2][j:j+5])
        ruudukkoy.append(ruudukkoyapu[3][j:j+5])
        ruudukkoy.append(ruudukkoyapu[4][j:j+5])
    
        
    with open("4.2.txt") as f:
        #järkkä jossa lukuja arvotaan
        order = [str(line[:-1]) for line in f][0].split(',')
        order = [int(x) for x in order]
        
        for luku in order:
            ruudukkox, bingo, sijainti = find_hits(ruudukkox, luku)
            if bingo == True:
                rivi = math.floor(sijainti/5)*5
                summa = 0
                littana = [item for sublist in ruudukkox[rivi:rivi+5] for item in sublist]
                for l in littana:
                    if str(l) != str(1000):
                        summa += int(l)
                break
            ruudukkoy, bingo, sijainti = find_hits(ruudukkoy, luku)
            if bingo == True:
                rivi = math.floor(sijainti/5)*5
                summa = 0
                littana = [item for sublist in ruudukkox[rivi:rivi+5] for item in sublist]
                for l in littana:
                    if str(l) != str(1000):
                        summa += int(l)
                        
                print(summa*luku)
                break
                                      
        
        
    
        
            