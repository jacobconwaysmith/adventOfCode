# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:07:19 2022

@author: jacob.smith
"""

#read in txt file as list
# with open('test.txt') as f:
#     lines = f.readlines()
    
#read in txt file as list
with open('input.txt') as f:
    lines = f.readlines()

#cleaning strings by getting rid of breaks
lines = [line.replace('\n', '').replace('\r', '') for line in lines]

total = 0 #set up variable for loop
for line in lines:

    line = line.split(",")
    line_first = line[0].split("-")
    line_second = line[1].split("-")
    
    first_start = int(line_first[0])
    first_end = int(line_first[1])
    
    second_start = int(line_second[0])
    second_end   = int(line_second[1])
    
    # first_range = list(range(first_start,first_end))
    # second_range = list(range(second_start,second_end))
    
    #see if first is contained in second
    if first_start >= second_start and first_end <= second_end:
        total += 1
    #see if second is contained within first
    elif second_start >= first_start and second_end <= first_end:
        total += 1
        

print("Total pairs complete overlap: ", total)

#Part 2 - find all chores that overlap at all, not just entirely
total = 0 #set up variable for loop
for line in lines:

    line = line.split(",")
    line_first = line[0].split("-")
    line_second = line[1].split("-")
    
    first_start = int(line_first[0])
    first_end = int(line_first[1])
    
    second_start = int(line_second[0])
    second_end   = int(line_second[1])
    
    if first_end >= second_start and first_end <= second_end:
        total += 1
    elif second_end >= first_start and second_end <= first_end:
        total += 1
    
#answer for test = 4
print("Total pairs of any overlap at all:", total)






