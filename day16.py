# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 07:51:44 2020

@author: nina
"""

import time
start_time = time.time()

f = open("day16.txt",'r')
txt = f.read()
ins = txt.split('\n\n')

instructions = ins[0].split('\n')
min1 = []
max1 = []
min2  =[]
max2 = []
f_name = []
for instruction in instructions:
    f_name.append(instruction.split(':')[0])
    min1.append(int(instruction.split(':')[1].split('or')[0].split('-')[0].strip()))
    max1.append(int(instruction.split(':')[1].split('or')[0].split('-')[1].strip()))
    min2.append(int(instruction.split(':')[1].split('or')[1].split('-')[0].strip()))
    max2.append(int(instruction.split(':')[1].split('or')[1].split('-')[1].strip()))

my_ticket = ins[1].strip('your ticket:\n')
my_ticket_values = my_ticket.split(',')
nearby_tickets = ins[2].strip('nearby tickets:\n').split('\n')

value_sum = 0
valid_tickets = []
for nearby_ticket in nearby_tickets:
    nearby_ticket_values = nearby_ticket.split(',')
    c_ticket = 1
    for nearby_ticket_value in nearby_ticket_values:
        c = 0; i = 0
        while (c==0 and i<len(min1)):
            if (min1[i] <= int(nearby_ticket_value) <= max1[i]) or (min2[i] <= int(nearby_ticket_value) <= max2[i]):
                c = 1
            i +=1
        if c==0:  
            value_sum = value_sum + int(nearby_ticket_value)
            c_ticket = 0
    if (c_ticket==1): valid_tickets.append(nearby_ticket.split(',')) 

print("part 1: %s" % value_sum)

all_possibilities = []
for m in range(len(min1)):
    poss = []
    for k in range(len(min1)):
        c_field = 0
        for l in range(len(valid_tickets)):
            val = int(valid_tickets[l][m])
            if (min1[k] <= val <= max1[k]) or (min2[k] <= val <= max2[k]):
                c_field +=1
        if c_field==len(valid_tickets): 
            poss.append(k); 
    all_possibilities.append(poss)

ss = []
for p in all_possibilities:
    ss.append(len(p))

ss1 = sorted(ss); len_indices = []
for (s, s1) in zip(ss, ss1):
    len_indices.append(ss.index(s1))

field_indices = []
found = []
for i in range(len(min1)):
    possibles = all_possibilities[len_indices[i]]
    for possible in possibles:
        if (possible in found) == 0:
            field_indices.append(possible)
            found.append(possible)
            
res = 1
for i in range(len(min1)):
      if 'departure' in f_name[i]:
          res = int(res)*int(my_ticket_values[len_indices[field_indices.index(i)]])

print("part 2: %s" % res) #1382443095281
print("--- %s seconds ---" % (time.time() - start_time))  