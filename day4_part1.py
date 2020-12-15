# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:24:44 2020

@author: nina.ceh
"""
import time
start_time = time.time()

f = open("day4.txt",'r')
txt = f.readlines()

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
ok_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

i = 0
a = {}
valid = 0
k = 0
for line in txt:
    if line in ['\n', '\r\n']:
        for f in ok_fields:
            if f in a:
                k +=1
        if k==7:
            valid +=1
            print(a, valid)
        i = 0
        del a
        a = {}
        del bs
        k = 0
    else:
        i +=1
        print(i)
        ds = line.split('\n')
        bs = ds[0].split(' ')
        cs = []
        j = 0
        for b in bs:
            cs.append(b.split(':'))
            a[cs[j][0]] = cs[j][1]
            j +=1
        

                
        