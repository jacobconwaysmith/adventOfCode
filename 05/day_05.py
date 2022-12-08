# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:13:00 2022

@author: jacob.smith
"""
#read in txt file as list
# with open('input.txt') as f:
#     lines = f.readlines()

#testing datase:
# read in txt file as list
def read_data(input_file):
    

with open('test.txt') as f:
    lines = f.readlines()

#get the moves -- need to change for the big dataset
moves = lines[5:]
stack = lines[:4]

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


#move number from orig to dest
#answer is what packages are on the top