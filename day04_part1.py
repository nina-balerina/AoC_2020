# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:24:44 2020

@author: nina.ceh
"""
import time
start_time = time.time()

f = open("day4.txt",'r')
txt = f.read()
in1 = txt.split('\n\n')

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
ok_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid = 0
for line in in1:
    k = 0
    a = {}
    bs = line.replace('\n',' ').strip().split(' ')
    for b in bs:
        cs = b.split(':')
        a[cs[0]] = cs[1]
    for f in ok_fields:
        if f in a: k +=1
    if k==7: valid +=1

print("part1 : %s" % valid)
print("--- %s seconds ---" % (time.time() - start_time))  
