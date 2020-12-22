# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 08:02:17 2020

@author: nina
"""

import time
start_time = time.time()
f = open('day22.txt','r')
txt = f.read().split('\n\n')

player1 = txt[0].replace('Player 1:\n','').split('\n') 
player2 = txt[1].replace('Player 2:\n','').strip().split('\n') 

cond = 0; i = 0
while cond==0:
    card1 = int(player1[i])
    card2 = int(player2[i])
    if card1>card2:
        player1.append(card1)
        player1.append(card2)
    elif card2>card1:
        player2.append(card2)
        player2.append(card1)   
    i += 1
    if len(player1)<=i or len(player2)<=i:
        cond = 1

win_deck = player1[i:] + player2[i:]
res = 0; counter = 0
for i in range(len(win_deck)-1,-1,-1):
    counter += 1
    res = res + int(win_deck[i])*counter
    
print("party 1: %s" % res) #36257
print("---%s seconds---" % (time.time()-start_time))