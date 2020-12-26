# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:34:09 2020

@author: nina
"""

import time
start_time = time.time()

no_1 = 14788856
no_2 = 19316454
divider = 20201227

a = 1
cond = 0
loop_size = 0
while cond == 0:
    loop_size += 1
    a = a*7
    a = a%divider
    
    if a == no_1:
        cond = 1
        
b = 1
for i in range(loop_size):
    b1 = b*no_2
    b = b1%divider


print("---%s seconds---" % (time.time()-start_time))