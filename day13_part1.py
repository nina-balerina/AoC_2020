# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 07:57:04 2020

@author: nina
"""
import time
start_time = time.time()
f = open("day13.txt",'r')
txt = f.readlines()

a = int(txt[0])
buses = txt[1].split(',')

buses2 = []
nums = []
differences = []
diff = 0

for bus in buses:
    try:
        bus = int(bus)
        nums.append(bus)
        differences.append(diff)
        diff +=1
    except:
        bus
        diff += 1
    buses2.append(bus)

from_largest = [0]*len(nums)
for i in range(0, len(differences)):
    from_largest[i] = differences[i]-differences[n]

times =[]*len(nums)
d = []
e = []
for number in nums:
    b = int(a/number)
    d = (b + 1)*number
    e = d-a
    print(number, e)
print("--- %s seconds ---" % (time.time() - start_time))



    

    
    

    
    
    
   
