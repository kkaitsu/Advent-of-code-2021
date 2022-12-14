# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:41:14 2021

@author: Kaisa Ylikoski
"""
values = {}


with open("5.1.txt") as f:
    biggestx = 0
    biggesty = 0
    koordinaatit = [str(line[:-1]) for line in f]
    for i, line in enumerate(koordinaatit):
        value = line.split(' -> ')
        x1 = int(value[0].split(',')[0])
        x2 = int(value[1].split(',')[0])
        y1 = int(value[0].split(',')[1])
        y2 = int(value[1].split(',')[1])

        values[i] = {
            'x1': x1,
            'x2':x2,
            'y1':y1,
            'y2':y2
        }
        if x1 > biggestx:
            biggestx = x1
        if x2 > biggestx:
            biggestx = x2
        if y1 > biggesty:
            biggesty = y1
        if y2 > biggesty:
            biggesty = y2
                
    kenttä = [[0 for i in range(biggestx+1)] for j in range(biggesty+1)]

    for i in values:
        if values[i]['y1'] == values[i]['y2']:
            mini = min(values[i]['x1'],values[i]['x2'])
            maxi = max(values[i]['x1'],values[i]['x2'])
            for j in range(mini, maxi+1):
                if kenttä[values[i]['y1']][j] == 0:
                    kenttä[values[i]['y1']][j] = 1
                else:
                    kenttä[values[i]['y1']][j] += 1
        elif values[i]['x1'] == values[i]['x2']:
            mini = min(values[i]['y1'],values[i]['y2'])
            maxi = max(values[i]['y1'],values[i]['y2'])
            for j in range(mini, maxi+1):
                if kenttä[j][values[i]['x1']] == 0:
                    kenttä[j][values[i]['x1']] = 1
                else:
                    kenttä[j][values[i]['x1']] += 1
        elif (values[i]['x1'] < values[i]['x2'] and values[i]['y1'] < values[i]['y2']) \
              or (values[i]['x1'] > values[i]['x2'] and values[i]['y1'] > values[i]['y2']):
            miniy = min(values[i]['y1'],values[i]['y2'])
            maxiy = max(values[i]['y1'],values[i]['y2'])
            minix = min(values[i]['x1'],values[i]['x2'])
            maxix = max(values[i]['x1'],values[i]['x2'])
            k = miniy
            for j in range(minix, maxix+1):
                if kenttä[k][j] == 0:
                    kenttä[k][j] = 1
                else:
                    kenttä[k][j] += 1
                k += 1
        else:
            if values[i]['x1'] < values[i]['x2']:
                k = values[i]['y1']
                for j in range(values[i]['x1'],values[i]['x2']+1):
                    if kenttä[k][j] == 0:
                        kenttä[k][j] = 1
                    else:
                        kenttä[k][j] += 1
                    #print(k)
                    k -= 1
            else:
                k = values[i]['x1']
                for j in range(values[i]['y1'],values[i]['y2']+1):
                    if kenttä[j][k] == 0:
                        kenttä[j][k] = 1
                    else:
                        kenttä[j][k] += 1
                    k -= 1
                    
            
    littana = [item for sublist in kenttä for item in sublist]
    summa = 0
    for i in littana:
        if i > 1:
            summa += 1
            
    print(summa)
            
            
    