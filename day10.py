# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

myfile = open("day10.txt")
txt = myfile.read()
myfile.close()

a = txt.split('\n');

b = [0]*len(a);
for i in range (0, len(a)-1):
    b[i] = int(a[i])

b.sort();
b.append(b[len(b)-1] + 3);

c = [0]*(len(b)-1);
for i in range (0, len(b)-1):
    c[i] = b[i+1] - b[i]
    
no_1 = c.count(1);   

no_3 = c.count(3);

print('part 1:')
print(no_1*no_3)