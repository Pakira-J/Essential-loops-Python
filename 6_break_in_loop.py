"""
Essential problems in Python; no.: 6
Objective: Given list of numbers, stop iteration when encountered a negative number and print the processed items so 
           far.
Author: Joydeep Pakira
"""

number_list = [1, 2, 8, 20, 100, 69, -2, -50, 3]
for n in number_list:
    if n < 0:
        break
    print(n, end=' ')

print('\nBreak in iteration')
