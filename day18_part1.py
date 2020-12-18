# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:40:05 2020

@author: nina.ceh
"""

import re
import time
start_time = time.time()

f = open('day18.txt','r')
txt = f.readlines()

data = []
levels_data = []
operations_data = []

line_sum = []
for line in txt: 
    line_clean = line.strip().replace(' ', '')
    new_line_clean = line_clean
    data.append(line_clean)
    line_parts = line_clean.split('(') 
    
    l = 0
    new_line_parts = ''
    for line_part in line_parts:
        l = l+1
        cond = 0
        new_line_part = line_part
        if ')' in line_part:
            cond = 1
            bracket = line_part.split(')') 
            numbers = re.findall(r'\d+', bracket[0])
            signs = ''.join(c for c in bracket[0] if c.isdigit()==0)
            res = int(numbers[0])
            
            for i in range(1,len(signs)+1):
                if signs[i-1]=='+':
                    res = res+int(numbers[i])
                elif signs[i-1]=='*':
                    res = res*int(numbers[i])     
            new_bracket = str(res)
        if cond==1:
            new_line_clean = new_line_clean.replace('('+bracket[0]+')', new_bracket)
    
    if '(' in new_line_clean: 
        line_parts = new_line_clean.split('(') 
        
        l = 0
        new_line_parts = ''
        for line_part in line_parts:
            l = l+1
            cond = 0
            
            new_line_part = line_part
            if ')' in line_part:
                cond = 1
                bracket = line_part.split(')') 
                numbers = re.findall(r'\d+', bracket[0])
                signs = ''.join(c for c in bracket[0] if c.isdigit()==0)
                res = int(numbers[0])
                
                for i in range(1,len(signs)+1): 
                    if signs[i-1]=='+':
                        res = res+int(numbers[i])
                    elif signs[i-1]=='*':
                        res = res*int(numbers[i])   
                new_bracket = str(res)
                for k in range(1,len(bracket)):
                    new_bracket = new_bracket 
            if cond==1:
                new_line_clean = new_line_clean.replace('('+bracket[0]+')', new_bracket)
    numbers2 = re.findall(r'\d+', new_line_clean)
    signs2 = ''.join(c for c in new_line_clean if c.isdigit()==0)
    res1 = int(numbers2[0])
    
    for i in range(1,len(signs2)+1): 
        if signs2[i-1]=='+':
            res1 = res1+int(numbers2[i])
        elif signs2[i-1]=='*':
            res1 = res1*int(numbers2[i])

    line_sum.append(res1)   
 
print("part 1: %s" % (sum(line_sum)))
print("--- %s seconds ---" % (time.time() - start_time))  
