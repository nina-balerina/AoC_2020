# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:44:42 2020

@author: nina
"""
import time
start_time = time.time()

import re
import math
f = open("day12.txt",'r')
txt = f.readlines()

a = []
val = []
b = []
for line in txt:
    match = re.match(r"([a-z]+)([0-9]+)", line, re.I)
    items = match.groups()
    a.append(items[0])
    b.append(items[0])
    val.append(int(items[1]))
   
action = ['N','S','E','W','L','R','F']
ang_direction = ['E','N','W','S']
direction = 'E'
pos = [0]*2; # Eeast (negative is west), North (negative is south)c

for i in range(0, len(a)):
    if a[i]==action[6]:
        a[i] = direction 
    elif a[i]==action[4]:
        ind = ang_direction.index(direction)
        direction = ang_direction[(ind+int(val[i]/90))%4]
    elif a[i]==action[5]:
        ind = ang_direction.index(direction)
        direction = ang_direction[(ind-int(val[i]/90))%4]
    if a[i]==action[0]:
        pos[1] += val[i]
    elif a[i]==action[1]:
        pos[1] -= val[i]
    elif a[i]==action[2]:
        pos[0] += val[i]
    elif a[i]==action[3]:
        pos[0] -= val[i]

print('part 1')        
print(abs(pos[0])+abs(pos[1]))

print("--- %s seconds ---" % (time.time() - start_time))
time2 = time.time()

WP_pos = [10,1]
direction2 = ['E','N','W','S']
pos2 = [0]*2

for i in range(0, len(b)):
    if b[i]==action[6]:
        #b[i] = direction 
        pos2[0] += WP_pos[0]*val[i]
        pos2[1] += WP_pos[1]*val[i]
    elif b[i]==action[4]: # left rotation
        theta = -val[i]*math.pi/180
        temporary = WP_pos[0]
        WP_pos[0] = round(WP_pos[0]*math.cos(theta) + WP_pos[1]*math.sin(theta))
        WP_pos[1] = round(-temporary*math.sin(theta) + WP_pos[1]*math.cos(theta))
    elif b[i]==action[5]: # right rotation
        theta = val[i]*math.pi/180
        temporary = WP_pos[0]
        WP_pos[0] = round(WP_pos[0]*math.cos(theta) + WP_pos[1]*math.sin(theta))
        WP_pos[1] = round(-temporary*math.sin(theta) + WP_pos[1]*math.cos(theta))
    if b[i]==action[0]:
        WP_pos[1] += val[i]
    elif b[i]==action[1]:
        WP_pos[1] -= val[i]
    elif b[i]==action[2]:
        WP_pos[0] += val[i]
    elif b[i]==action[3]:
        WP_pos[0] -= val[i]
    if pos2[0]<0:
        direction2[0] = 'W'
    if pos2[1]<0:
        direction2[1] = 'S'
 
print('part 2')
print(abs(pos2[0])+abs(pos2[1]))    
    
print("--- %s seconds ---" % (time.time() - time2))


    
