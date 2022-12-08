# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:12:26 2022

@author: jacob.smith

Day  1 of advent coding cal
https://adventofcode.com/2022/day/1

Saved the input file as input.txt

"""

#read in txt file as list
with open('input.txt') as f:
    lines = f.readlines()

#Setup veriables including a dict
total = 0
elf = 0
elf_dict = {}

#loop over every item in list
for line in lines:
    if not line.isspace(): 
        total += int(line) #add together if not a space
    else:
        elf += 1 #label the next elf (be carefule of zero indexing)
        elf_dict[elf] = total #send the sum of an elf to a dict
        total = 0 #reset total for each elf to zero for counting

#get highest elf
elf_key_highest = max(elf_dict, key=elf_dict.get)

print("The elf with the highest calories is: " + str(elf_key_highest) + " with a total calories of:" + str(elf_dict[elf_key_highest]))     


top_three = sorted(elf_dict, key=elf_dict.get, reverse=True)[:3]

sum_top_3 = sum([elf_dict[x] for x in top_three])

print("The top three carrying elves have are: ", top_three, " with a sum of: ", sum_top_3, " calories")
