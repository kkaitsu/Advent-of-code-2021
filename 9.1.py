# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:38:01 2021

@author: Kaisa Ylikoski
"""

with open("9.1.txt") as f:
    hights = []
    hightsy = []
    for i, rivi in enumerate(f):
        hight_row = [int(x) for x in rivi[:-1]]
        hights.append(hight_row)
   
summa = 0         
for i, rivi in enumerate(hights):
    hightsy.append([x[i] for x in hights])
    #ekarivi
    for j,alkio in enumerate(rivi):
        if i == 0:
            
            #ylävasen kulma
            if j == 0:
                if alkio < hights[i+1][j] and alkio <hights[i][j+1]:
                    summa += 1 + alkio
                    #print(alkio, 'i ', i , 'j', j)
            #yläoikea kulma
            elif j == (len(hights[0])-1):
                if alkio < hights[i+1][j] and alkio <hights[i][j-1]:
                    summa += 1 + alkio
                    #print(alkio, 'i ', i , 'j', j)
            else:
                if alkio < hights[i+1][j] and alkio <hights[i][j+1] \
                    and alkio < hights[i][j-1]:
                    summa += 1 + alkio
                    #print(alkio, 'i ', i , 'j', j)
        #vikarivi
        elif i ==(len(hightsy[0])-1):
                #alavasen kulma
                if j == 0:
                    if alkio < hights[i-1][j] and alkio <hights[i][j+1]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
                #alaoikea kulma
                elif j == (len(hights[0])-1):
                    if alkio < hights[i-1][j] and alkio <hights[i][j-1]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
                else:
                    if  alkio <hights[i][j+1] and alkio < hights[i-1][j] \
                        and alkio < hights[i][j-1]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
        #keskirivit
        else:
                #vasen reuna
                if j == 0:
                    if alkio < hights[i-1][j] and alkio <hights[i][j+1]\
                        and alkio < hights[i+1][j]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
                #oikea reuna
                elif j == (len(hights[0])-1):
                    if alkio < hights[i-1][j] and alkio <hights[i][j-1]\
                        and alkio < hights[i+1][j]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
                #kaikki neljä sivua vapaina
                else:
                    if  alkio <hights[i][j+1] and alkio < hights[i][j-1] \
                        and alkio < hights[i+1][j] and alkio < hights[i-1][j]:
                        summa += 1 + alkio
                        #print(alkio, 'i ', i , 'j', j)
print(summa)