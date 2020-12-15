# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 07:26:07 2020

@author: nina
"""
import time
start_time = time.time()
inp = [0,13,16,17,1,10,6] # my input
#inp = [0,3,6] # test input
l = len(inp)
number = inp

a = {0:0,13:1,16:2,17:3,1:4,10:5,6:6}
b = {0:0,13:0,16:0,17:0,1:0,10:0,6:0}
c = {0:0,13:0,16:0,17:0,1:0,10:0,6:0}

new_number = number[l-1]
prev = []
for i in range(l,30000000): 
    prev = new_number
    if prev in a:
        if c[prev]==0:
            new_number = 0
            b[new_number] = a[new_number]
            a[new_number] = i
            c[new_number] = 1
        elif c[prev]!=0:
            new_number = a[prev]-b[prev] 
            if new_number in a:
                b[new_number] = a[new_number]
                a[new_number] = i
                c[new_number] = 1
            else:
                a[new_number] = i
                b[new_number] = 0 
                c[new_number] = 0 
    else:
        a[new_number] = i
        b[new_number] = 0 
        c[new_number] = 0
    if i == 2019:
        print("part 1: %s" % new_number)
    elif i ==30000000-1:
        print("part 3: %s" % new_number)

print("--- %s seconds ---" % (time.time() - start_time))  
    
            
    