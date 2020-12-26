# -*- coding: utf-8 -*-
"""
@author: nina
"""
import time
import itertools
start_time = time.time()

f = open('day24.txt', 'r')
txt = f.readlines()

tiles = []
for line in txt:
    txt2 = line.replace('e','e.').replace('w','w.')
    l = txt2.split('.')
    tiles.append(l[:-1])

tile_dict = {} 
for tile in tiles:
    x = 0
    y = 0
    for i in range(len(tile)):
        if tile[i] == 'e':
            x += 1
        elif tile[i] == 'w':
            x -= 1
        elif tile[i] == 'ne':
            y += 1
        elif tile[i] == 'sw':
            y -= 1
        elif tile[i] == 'nw':
            x -= 1
            y += 1
        elif tile[i] == 'se':
            x += 1
            y -= 1
    if (x,y) in tile_dict:       
        tile_dict[(x,y)] = tile_dict[(x,y)] + 1     
    else:
        tile_dict[(x,y)] = 1
        
counter = 0
for tile in tile_dict:
    if int(tile_dict[tile])%2 == 1:
        counter += 1
        
print("party 1: %s" % counter)    
print("---%s seconds---" % (time.time()-start_time))

perms = []
for r in itertools.product([-1, 0, 1], repeat=2):
    perms.append(r)
del perms[perms.index((0,0))]
del perms[perms.index((1,1))]
del perms[perms.index((-1,-1))]

for k in range(100):
    tile_dict_keep = tile_dict.copy()
    
    for i in range(-80, 80):
        for j in range(-80, 80):
            
            adjacent_black_tiles = 0
            for l in range(len(perms)):
                if (i+perms[l][0],j+perms[l][1]) in tile_dict:
                    if tile_dict[(i+perms[l][0],j+perms[l][1])]%2 == 1:
                        adjacent_black_tiles += 1
             
            if (i,j) in tile_dict:
                if tile_dict[(i,j)]%2 == 1:
                    if adjacent_black_tiles == 0 or adjacent_black_tiles > 2:
                        tile_dict_keep[(i,j)] = tile_dict_keep[(i,j)] + 1
                else:
                    if adjacent_black_tiles == 2:
                        tile_dict_keep[(i,j)] = tile_dict_keep[(i,j)] + 1
            else:
                if adjacent_black_tiles == 2:
                    tile_dict_keep[(i,j)] = 1   
           
    del tile_dict
    tile_dict = tile_dict_keep
    del tile_dict_keep                    
    counter = 0
    for tile in tile_dict:
        if int(tile_dict[tile])%2 == 1:
            counter += 1
    
print("party 2: %s" % counter) #3777
print("---%s seconds---" % (time.time()-start_time))