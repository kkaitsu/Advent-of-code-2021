# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:05:20 2021

@author: Kaisa Ylikoski

RIKKI, toimii esimerkkidatalla, ei oikealla datalla
"""

#from numerot import numerot

#print(numerot[0]['yht'])
#print(numerot['kaikki'][0])

output = []
inputt = []
both = []
#koodaus[oikea kirjain] = dekoodattu kirjain
koodaus ={}

def similarity(string1, string2):
    count = 0

    for letter in set(string1):
      count += string2.count(letter)
    
    return count

def unsimilarity(string1, string2):
    le = ''
    s1 = len(string1)
    s2 = len(string2)
    if s1<s2:
        str_min = string1
        str_max = string2
    else:
        str_min = string2
        str_max = string1
    for letter in str_max:
       if str_min.find(letter) == -1:
           le = le + letter
    
    return le

def löytyykö(decoding, digit):
    tosi = True
    for i in decoding:
        if similarity(decoding[i], digit) == len(digit) and len(digit) == len(decoding[i]):
        #if decoding[i] == digit:
            tosi = False
    
    return tosi

def jotain(output, i, decoding2, summastring):
    for out in output[i]:
        for s, sana in enumerate(decoding2):
            if similarity(out, sana) == len(sana) and len(sana) == len(out):
                summastring = summastring + str(decoding3[s])
    
                if len(summastring) == 4:
                    #print(summastring)
                    return(summastring)
                
def fourdiff(decoding):
    fourdiff = unsimilarity(decoding['i1'], decoding['i4'])
    return(fourdiff)

with open("8.1.txt") as f:

    for i, digitals in enumerate(f):
        digitals = digitals.split('|')
        o = digitals[1][1:-1].split(' ')
        output.append(o)
        i = digitals[0][:-1].split(' ')
        inputt.append(i)
        both.append(i + o)
    
    summa = 0
    summat = []
    summastring = ''
    for i, rivi in enumerate(inputt):

        decoding = {
            'i0': '',
            'i1': '',
            'i2': '',
            'i3': '',
            'i4': '',
            'i5': '',
            'i6': '',
            'i7': '',
            'i8': '',
            'i9': ''}
        decoding2 = []
        decoding3 = []
        apu = 0
        while apu < 10:
            summa = 0
            summastring = ''
            for j, digit in enumerate(rivi):

                if len(digit)== 2 and apu == 0:
                    decoding['i1'] = digit
                    decoding2.append(digit)
                    decoding3.append(1)
                    apu +=1
                elif len(digit) == 3 and apu == 1:
                    decoding['i7'] = digit
                    decoding2.append(digit)
                    decoding3.append(7)
                    apu +=1
                elif len(digit) == 7 and apu == 2:
                    decoding['i8'] = digit
                    decoding2.append(digit)
                    decoding3.append(8)                     
                    apu +=1
                elif len(digit) == 4 and apu == 3:
                    decoding['i4'] = digit
                    decoding2.append(digit)
                    decoding3.append(4)
                    apu +=1
                    #cdfbe
                elif similarity(digit,decoding['i7']) == 3 and len(digit) == 5\
                    and apu == 4 and löytyykö(decoding,digit):
                    decoding['i3'] = digit
                    decoding2.append(digit)
                    decoding3.append(3)
                    apu +=1
                elif similarity(digit,decoding['i4']) == 4 and len(digit) == 6\
                    and apu == 5 and löytyykö(decoding,digit):
                    decoding['i9'] = digit
                    decoding2.append(digit)
                    decoding3.append(9)
                    apu +=1
                elif similarity(digit,fourdiff(decoding)) == 2 and len(digit) == 5\
                    and apu == 6 and löytyykö(decoding, digit):
                    decoding['i5'] = digit
                    decoding2.append(digit)
                    decoding3.append(5)
                    apu +=1
                elif similarity(digit,decoding['i5']) == 5 and len(digit) == 6\
                    and apu == 7 and löytyykö(decoding, digit):
                    decoding['i6'] = digit
                    decoding2.append(digit)
                    decoding3.append(6)
                    apu +=1
                elif len(digit) == 6 and apu == 8 and löytyykö(decoding, digit):
                    decoding['i0'] = digit
                    decoding2.append(digit)
                    decoding3.append(0)
                    apu +=1
                elif len(digit) == 5 and apu == 9 and löytyykö(decoding, digit):
                    decoding['i2'] = digit
                    decoding2.append(digit)
                    decoding3.append(2)
                    apu +=1
                elif apu > 9 :
                    summastring = ''
                    summat.append(int(jotain(output, i, decoding2, summastring)))
                    break
            #print(decoding3)


                        
                
print(sum(summat))

#1051087 oikea vastaus
#916541 too low