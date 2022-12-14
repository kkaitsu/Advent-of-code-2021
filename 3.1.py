# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:28:53 2021

@author: Kaisa Ylikoski
"""

ones = 12*[0]
zeros = 12*[0]
most = 12*[0]
binary_most = ''
binary_least = ''

with open("3.1.txt") as f:
    for binary_value in f:
        for i in range(0,len(binary_value)):
            if binary_value[i] == "0":
                zeros[i] += 1
            if binary_value[i] == "1":
                ones[i] += 1
                
                

for i in range(0,len(ones)):
    if ones[i] > zeros[i]:   
        binary_most = binary_most + '0'
    if zeros[i] > ones[i]:
        binary_most = binary_most + '1'

binary_least =  ''.join(['1' if i == '0' else '0' for i in binary_most])

print(int(binary_most, 2)*int(binary_least, 2))

