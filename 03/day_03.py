# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:29:22 2022

@author: jacob.smith
"""
import string
p_score_dict = dict(zip(string.ascii_letters, range(1,53)))

#read in txt file as list
with open('input.txt') as f:
    lines = f.readlines()

#testing datase:
#read in txt file as list
# with open('test.txt') as f:
#     lines = f.readlines()

#cleaning strings by getting rid of breaks
lines = [line.replace('\n', '').replace('\r', '') for line in lines]

total = 0
lines_matches = 0

#seperate strings
for line in lines:
    end = len(line) #careful here of zero indexing
    end_first = int(len(line)/2)
    start_second = int(end_first)
    
    first_string = line[0:end_first]
    second_string = line[start_second:end+1]
    
    flag = False #a flag to break the loop as I couldn't figure out how to d
    
    #Find same letter/item in both strings/rucksacks
    for letter in first_string:
        if flag == True:
            break
        for comp_letter in second_string:
            if flag == True:
                break
            elif letter == comp_letter:
                item = letter
    #Add to the total by priority score
                p_score = p_score_dict[item]
                total += p_score
                lines_matches += 1
                print("score this round: ", p_score)
                print("Running total: ", total)
                flag = True
            else:
                continue
        
print("Lines with match: ", lines_matches)
print(total)


#Part 2
##################

