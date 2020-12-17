# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:13:59 2020

@author: nina
"""

import time
import itertools
start_time = time.time()

f = open("day11.txt",'r')
txt = f.readlines()

a = {}
i = 0
for line in txt:
    j = 0
    line_clear = line.strip()
    for char in line_clear:
        if char=='L':
            a[str([i,j])] = 1
        j += 1
    i += 1
b = a

perms = []
for r in itertools.product([-1, 0, 1], repeat=2):
    perms.append(r)
del perms[perms.index((0,0))]

### part 1

chaos = 0
a_new = {}
t = 1
while chaos==0:
    t += 1
    for i in range(len(txt)):
        for j in range(len(line_clear)):
            no_occupied_neigh = 0
            for k in range(len(perms)):
                x_neigh = i + perms[k][0]
                y_neigh = j + perms[k][1]
                if str([x_neigh,y_neigh]) in a:
                    if a[str([x_neigh,y_neigh])]==1:
                        no_occupied_neigh = no_occupied_neigh + 1
            if str([i,j]) in a:
                if a[str([i,j])]==0:
                    if no_occupied_neigh==0:
                        a_new[str([i,j])] = 1
                    else:
                        a_new[str([i,j])] = 0
                elif a[str([i,j])]==1:
                    if no_occupied_neigh>=4:
                        a_new[str([i,j])] = 0
                    else:
                        a_new[str([i,j])] = 1
    if a==a_new:
        chaos = 1
    del a
    a = a_new 
    a_new = {}  

print("part 1: %s" % (sum(a.values()))) #2316
print("--- %s seconds ---" % (time.time() - start_time)) 

### part 2

a = b
chaos2 = 0
a_new = {}
t = 1
while chaos2==0:
    t += 1
    for i in range(len(txt)):
        for j in range(len(line_clear)):
            no_occupied_neigh = 0
            for k in range(len(perms)):
                seat_c = 0
                steps = 1
                l = 0
                while (seat_c==0) and (steps<=(len(line_clear)+1)):
                    x_neigh = i + steps*perms[k][0]
                    y_neigh = j + steps*perms[k][1]
                    if str([x_neigh,y_neigh]) in a:
                        seat_c = 1
                        if a[str([x_neigh,y_neigh])]==1:
                            no_occupied_neigh = no_occupied_neigh + 1
                    steps += 1
            if str([i,j]) in a:
                if a[str([i,j])]==0:
                    if no_occupied_neigh==0:
                        a_new[str([i,j])] = 1
                    else:
                        a_new[str([i,j])] = 0
                elif a[str([i,j])]==1:
                    if no_occupied_neigh>=5:
                        a_new[str([i,j])] = 0
                    else:
                        a_new[str([i,j])] = 1
    if a==a_new:
        chaos2 = 1
    del a
    a = a_new 
    a_new = {}  

print("part 2: %s" % (sum(a.values()))) #2128
print("--- %s seconds ---" % (time.time() - start_time)) 
