# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:37:27 2020

@author: nina
"""

import time
start_time = time.time()

f = open('day1.txt', 'r')
txt = f.readlines()

numbers = []
for line in txt:
    numbers.append(int(line.strip()))

### part 1    

for number1 in numbers:
    for number2 in numbers:
        sumed = number1 + number2
        if sumed == 2020:
            n1 = number1
            n2 = number2
            break  # why break doesn't break all nested loops?
    
print("part 1: %s" % (n1*n2)) #776064
print("---%s seconds..." % (time.time()-start_time))

### part 2

for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            sumed = number1 + number2 + number3
            if sumed == 2020:
                n1 = number1; n2 = number2; n3 = number3
                break 

print("part 2: %s" % (n1*n2*n3)) #6964490
print("---%s seconds..." % (time.time()-start_time))