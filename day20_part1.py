# -*- coding: utf-8 -*-
"""
@author: nina
"""

import time
start_time = time.time()

f = open('day20.txt', 'r')
txt = f.read().split('\n\n')
del txt[len(txt)-1]

tileIDs = []
tiles = []
boundaries = []
for tile in txt:
    tileIDs.append(int(tile.split(':')[0].split(' ')[1]))
    tile_image = tile.split(':')[1].strip()
    tiles.append(tile_image)
    tile_parts = tile_image.split('\n')
    b1 = ''; b2 = ''
    for tile in tile_parts:
        b1 += tile[0]
        b2 += tile[-1]
    boundaries_single_tile = [tile_parts[0][:], b2, tile_parts[-1][:], b1]
    boundaries.append(boundaries_single_tile)
    
bound_match = []    
for i in range(len(tiles)):
    cond_tile = 0
    for j in range(4):
        cond = 0
        B1 = boundaries[i][j]
        for k in range(len(tiles)):
            for m in range(4):
                B2 = boundaries[k][m]
                B3 = boundaries[k][m][::-1]
                if i!=k and (B1==B2 or B1==B3):
                    cond += 1
        cond_tile += cond
    bound_match.append(cond_tile)

indices = [i for i, x in enumerate(bound_match) if x == 2]
res = 1
for index in indices: res = res*tileIDs[index]

print("part 1: %s" % res) #32287787075651
print("--- %s seconds ---" % (time.time() - start_time))  
