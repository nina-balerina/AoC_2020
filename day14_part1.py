# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:20:11 2020

@author: nina.ceh
"""
import time
start_time = time.time()
import re
f = open("day14.txt",'r')
txt = f.readlines()

coms = []
values = []
values2 = []
bit_values = []
instructions = []
for line in txt:
    coms.append(line.split('=')[0])
    values.append(line.split('=')[1])
    a = line.split('=')[1]
    b = a.split(' ')[1]
    c = b.split('\n')[0]
    bit_values.append(c)
    if '[' in line:
        instructions.append(line.split('[')[0])
    else:
        instructions.append(line.split('=')[0])
    
### part 1 ###

positions = []  
for (com , value) in zip(coms, values):
    number = [float(s) for s in re.findall(r'-?\d+\.?\d*', com)]
    number2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', value)]
    if len(number)==1:
        positions.append(int(number[0])) 
        values2.append(int(number2[0])) 
    elif len(number)==0:
        positions.append(0)
        values2.append(0)

# formats int x to binary of len n ()
def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

number_list = [0]*(max(positions)+1)
j = 0
for (instruction, position, value2, bit_value) in zip (instructions, positions, values2, bit_values):
    j += 1
    if instruction=='mask ':
        M = bit_value
    elif instruction=='mem':
        current_no_bin = format(value2, 'b').zfill(36)
        new_no_bin = []
        for i in range(0,36):
            if M[i]=='1':
                new_no_bin.append('1')
            elif M[i]=='0':
                new_no_bin.append('0')
            elif M[i]=='X':
                new_no_bin.append(current_no_bin[i])
        s = ''.join(new_no_bin)
        number_list[position] = int(s, 2)
    
print("part 1: %s" % (sum(number_list))) # 10452688630537
print("--- %s seconds ---" % (time.time() - start_time))
