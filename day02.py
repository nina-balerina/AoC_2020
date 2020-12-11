# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:52:36 2020

@author: nina.ceh
"""

f = open("day2.txt",'r')
txt = f.readlines()


no_valid = 0;
no_valid_2 = 0;

for line in txt:
    a = line.split() 
    b = a[0].split('-')
    low = int(b[0])
    high = int(b[1])
    letter = a[1][0]
    password = a[2]
    if low <= password.count(letter) <= high:
        no_valid += 1
    if (password[low-1]==letter and password[high-1]!=letter) or (password[low-1]!=letter and password[high-1]==letter):
        no_valid_2 += 1
        
print('part 1')
print(no_valid)

print('part 2')
print(no_valid_2)

    



