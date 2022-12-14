# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:39:58 2021

@author: Kaisa Ylikoski
"""
from enum import Enum
import numpy as np
import math
import sys




def find_hits(ruudukko, luku):
    #indeksit joissa oikea luku sijaitsee
    for ruutu in ruudukko:
        if ruudukko[ruutu]['bingo'] == False:
            erikoinen = 0
            index = np.where(np.array(ruudukko[ruutu]['x'])==str(luku))[0]
            indey = np.where(np.array(ruudukko[ruutu]['y'])==str(luku))[0]
            #oikeisiin indekseihin luku 1000
            #käydään riviä läpi, osuman tilalle luku 1000
            for i in index:
                for j, elem in enumerate(ruudukko[ruutu]['x'][i]):
                    if str(elem) == str(luku):
                        ruudukko[ruutu]['x'][i][j] = '1000'
                        #tarkista tuliko bingo
                        osumat = np.where(np.array(ruudukko[ruutu]['x'])=='1000')[0]
                        for k in osumat:
                            #jos samalla rivillä on 5 osumaa -> bingo
                            if np.count_nonzero(k == osumat) == 5:
                                #bingo = true
                                ruudukko[ruutu]['bingo'] = True
                                erikoinen = ruutu
            for i in indey:
                for j, elem in enumerate(ruudukko[ruutu]['y'][i]):
                    if str(elem) == str(luku):
                        ruudukko[ruutu]['y'][i][j] = '1000'
                        #tarkista tuliko bingo
                        osumat = np.where(np.array(ruudukko[ruutu]['y'])=='1000')[0]
                        for k in osumat:
                            #jos samalla rivillä on 5 osumaa -> bingo
                            if np.count_nonzero(k == osumat) == 5:
                                #bingo = true
                                ruudukko[ruutu]['bingo'] = True
                                erikoinen = ruutu

                            

    return(ruudukko, erikoinen)

ruudukkox = []
ruudukkoy = []
ruudukkoyapu = []
ruudukko = {
    1:dict}

with open("4.1.txt") as f2:
    ruudukkox = [str(line[:-1]) for line in f2]
    #poista tyhjät rivit
    ruudukkox = [x for x in ruudukkox if x]
    for i, line in enumerate(ruudukkox):
        ruudukkox[i] = ruudukkox[i].split(' ')
        #poista tyhjät
        ruudukkox[i] = [x for x in ruudukkox[i] if x]
        
    #lisää ruudukkox dictiin
    i = 0
    for j in range(0,len(ruudukkox),5):
        ruudukko[i] = {'bingo':False, 'x': ruudukkox[j:j+5], 'y': []}
        i+=1

    
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
        
    #lisää ruudukkoy dictiin
    i = 0
    for j in range(0,len(ruudukkoy),5):
        ruudukko[i]['y'] = ruudukkoy[j:j+5]
        i+=1
    
        
    with open("4.2.txt") as f:
        #järkkä jossa lukuja arvotaan
        order = [str(line) for line in f][0].split(',')
        order = [int(x) for x in order]
        
        for luku in order:
            ruudukko, ruutu2 = find_hits(ruudukko, luku)
            i = 0
            for ruutu in ruudukko:
                if ruudukko[ruutu]['bingo'] == True:
                    i += 1
                    if i == 100: #51
                        print('bingo!')
                        littana = [item for sublist in ruudukko[ruutu2]['x'] for item in sublist]
                        summa = 0
                        for l in littana:
                            if str(l) != str(1000):
                                summa += int(l)
                        print(summa*luku)
                        sys.exit()
                                    