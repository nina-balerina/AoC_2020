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
        nums.append(int(bus))
        differences.append(diff)
    except:
        1
    diff += 1

e = []
for number in nums:
    b = int(a/number)
    e.append(((b + 1)*number)-a)
ind = e.index(min(e)) 
res = e[ind]*nums[ind]
print("part 1: %s"  % res) # 115
print("--- %s seconds ---" % (time.time() - start_time))

# part2

additional_nums = [nums[0]]
difs = [differences[0]]
for i in range(1,9):
    j = 0
    cond = 0
    while cond==0:
        j +=1
        tp = j*additional_nums[i-1] + difs[i-1]    
        if (tp+differences[i])%nums[i]==0:
            additional_nums.append(additional_nums[i-1]*nums[i])
            difs.append(tp)
            cond=1

print("part 2: %s" % tp) # 756261495958122
print("--- %s seconds ---" % (time.time() - start_time))