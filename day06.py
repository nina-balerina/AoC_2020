# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:05:28 2020

@author: nina
"""

import time
import re
start_time = time.time()

f = open("day6.txt",'r')
txt = f.read()
ins = txt.split('\n\n')

yeses = 0
for in1 in ins:
    a = in1.replace('\n','').strip()
    r = re.compile(r"(.)\1{0,}")
    bs = r.findall(a)
    letters = {}
    for b in bs:letters[b] = 1
    yeses += len(letters)

print("part 1: %s" % yeses) # 6714
print("--- %s seconds ---" % (time.time() - start_time))  

in2 = []
yeses_all = 0
for in1 in ins:
    ds = in1.strip().split('\n')
    a = in1.replace('\n','').strip()
    r = re.compile(r"(.)\1{0,}")
    bs = r.findall(in1)
    letters_2 = {}
    for b in bs: letters_2[b] = bs.count(b)
    for let in letters_2: 
        if letters_2[let] == len(ds): yeses_all += 1

print("part 2: %s" % yeses_all) # 3435
print("--- %s seconds ---" % (time.time() - start_time))  