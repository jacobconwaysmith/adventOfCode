# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:00:38 2022

@author: jacob.smith
"""

#read in txt file as list
with open('input.txt') as f:
    lines = f.readlines()

#cleaning strings by getting rid of breaks
lines = [line.replace('\n', '').replace('\r', '') for line in lines]

#outcomes
lose = 0 #X
draw = 3 #Y
win  = 6 #Z

#shape YOU selected i.e. Y X Z
rock     = 1 # X
paper    = 2 # Y
scissors = 3 # Z

#oponnent's code
# A = rock #X
# B = paper #Y
# C = scissors #Z

total = 0
for line in lines:
    #score for selection
    if "X" in line:
        total += lose #add the strategy score of X, to lose
        if "A" in line:
            total += scissors
        elif "B" in line:
            total += rock
        else:
            total += paper
    elif "Y" in line:
        total += draw
        if "A" in line:
            total += rock
        elif "B" in line:
            total += paper
        else:
            total += scissors
    else:
        total += win
        if "A" in line:
            total += paper
        elif "B" in line:
            total += scissors
        else:
            total += rock
            
print(total)





