# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:48:29 2020

@author: nina
"""

import time
start_time = time.time()

txt = '871369452' #my input
#txt = '389125467' #test input
cups = txt

cond = 0
curr_index = 0
for i in range(100):
    position = curr_index%9
    curr_cup = int(cups[position])
    
    pcc_string = ''
    for j in range(3):
        pcc_string = pcc_string + cups[(curr_index + j + 1)%9]
    
    for j in range(3):
        cups = cups.replace(pcc_string[j],'')
        
    dest_cup = curr_cup - 1
    if dest_cup < 1:
        dest_cup = 9 - dest_cup
    while str(dest_cup) in pcc_string:
        dest_cup -= 1
        if dest_cup < 1:
            dest_cup = 9 - dest_cup
            
    c2 = cups.replace(str(dest_cup), str(dest_cup)+pcc_string)
    keep_position = c2.index(str(curr_cup))
    if keep_position != position:
        cups = c2[keep_position-position:] + c2[0:keep_position-position]
    else:
        cups = c2
    
    curr_index += 1

print("party 1: %s" % (cups[3:]+cups[0:2])) #28793654
print("---%s seconds---" % (time.time()-start_time))       
    
