# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:55:54 2020

@author: nina.ceh
"""

import time
import itertools
start_time = time.time()

f = open("day17.txt",'r')
txt = f.readlines()

### part 1

i = 0
a = {}
for line in txt:
    j = 0
    line_clear = line.strip()
    for char in line_clear:
        if char=='#':
            a[str([i,j,0])] = 1
        elif char=='.':
            a[str([i,j,0])] = 0
        j +=1
    i +=1
minx = 0; maxx = i
miny = 0; maxy = j
minz = 0; maxz = 0
    
perms = []
for r in itertools.product([-1,0,1], repeat=3):
    perms.append(r)
del perms[perms.index((0,0,0))]

l = 0
a_new = {}
for l in range(6):
    for i in range(minx - 1, maxx + 2):
        for j in range(miny - 1, maxy + 2):
            for k in range(minz - 1, maxz + 2):
                cond = 0
                for m in range(len(perms)):
                    x_neigh = i + perms[m][0]
                    y_neigh = j + perms[m][1]
                    z_neigh = k + perms[m][2]
                    if str([x_neigh, y_neigh, z_neigh]) in a:
                        cond = cond + a[str([x_neigh, y_neigh, z_neigh])]
                if str([i,j,k]) in a:
                    if a[str([i,j,k])] ==1:
                        if cond==2 or cond==3:
                            a_new[str([i,j,k])] = 1
                    else:
                        if cond==3:
                            a_new[str([i,j,k])] = 1
                else:
                    if cond==3:
                        a_new[str([i,j,k])] = 1
    del a
    a = a_new
    a_new = {}
    minx = minx - 1; maxx = maxx + 1
    miny = miny - 1; maxy = maxy + 1
    minz = minz - 1; maxz = maxz + 1

print("part 1: %s" % (sum(a.values()))) #388
print("--- %s seconds ---" % (time.time() - start_time))  

### part 2 (the same as part 1 with one more dimension)

i = 0
a = {}
for line in txt:
    j = 0
    line_clear = line.strip()
    for char in line_clear:
        if char=='#':
            a[str([i,j,0,0])] = 1
        elif char=='.':
            a[str([i,j,0,0])] = 0
        j +=1
    i +=1

minx = 0; maxx = i
miny = 0; maxy = j
minz = 0; maxz = 0
minw = 0; maxw = 0

perms = []
for r in itertools.product([-1,0,1], repeat=4):
    perms.append(r)  
del perms[perms.index((0,0,0,0))]

l = 0
a_new = {}
for l in range(6):
    for i in range(minx - 1, maxx + 2):
        for j in range(miny - 1, maxy + 2):
            for k in range(minz - 1, maxz + 2):
                for n in range(minw - 1, maxw + 2):
                    cond = 0
                    for m in range(len(perms)):
                        x_neigh = i + perms[m][0]
                        y_neigh = j + perms[m][1]
                        z_neigh = k + perms[m][2]
                        w_neigh = n + perms[m][3]
                        if str([x_neigh, y_neigh, z_neigh, w_neigh]) in a:
                            cond = cond + a[str([x_neigh, y_neigh, z_neigh, w_neigh])]
                    if str([i,j,k, n]) in a:
                        if a[str([i,j,k, n])] ==1:
                            if cond==2 or cond==3:
                                a_new[str([i,j,k,n])] = 1
                        else:
                            if cond==3:
                                a_new[str([i,j,k,n])] = 1
                    else:
                        if cond==3:
                            a_new[str([i,j,k,n])] = 1
    del a
    a = a_new
    a_new = {}
    minx = minx - 1; maxx = maxx + 1
    miny = miny - 1; maxy = maxy + 1
    minz = minz - 1; maxz = maxz + 1
    minw = minw - 1; maxw = maxw + 1

print("part 2: %s" % (sum(a.values()))) #2280
print("--- %s seconds ---" % (time.time() - start_time))  
