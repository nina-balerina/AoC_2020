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
valid2 = 0
eye_color = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
for line in in1:
    k = 0; k2 = 0
    a = {}
    bs = line.replace('\n',' ').strip().split(' ')
    for b in bs:
        cs = b.split(':')
        a[cs[0]] = cs[1]
    for f in ok_fields:
        if f in a: 
            # counter for part 1:
            k +=1 
            # counter for part 2:
            if f=='byr':
                if int(a['byr']) in range (1920, 2003): k2 +=1
            elif f=='iyr':
                if int(a['iyr']) in range (2010, 2021): k2 +=1
            elif f=='eyr':
                if int(a['eyr']) in range (2020, 2031): k2 +=1
            elif f=='hgt':
                if 'cm' == a['hgt'][3:]:
                    if a['hgt'][0:3].isdigit()==1 and (int(a['hgt'][0:3]) in range (150, 194)):
                        k2 +=1
                elif 'in' == a['hgt'][2:]:
                    if a['hgt'][0:2].isdigit()==1 and (int(a['hgt'][0:2]) in range(59, 77)):
                        k2 +=1
            elif f=='hcl':
                if a['hcl'][0] == '#':
                    if len(a['hcl'])==7 and (all(c.isdigit() or c.islower() for c in a['hcl'][1:])):
                            k2 +=1
            elif f=='ecl':
                if a['ecl'] in eye_color: k2 +=1
            elif f=='pid':    
                if len(a['pid'])==9 and a['pid'].isdigit()==1: k2 +=1
    if k==7: valid +=1
    if k2==7: valid2 +=1

print("part1 : %s" % valid) #219
print("part2 : %s" % valid2) #127
print("--- %s seconds ---" % (time.time() - start_time))  