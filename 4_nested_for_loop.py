"""
Essential problems in Python; no.: 4
Objective: Print multiplication table of 1 to 5 (from 1 to 10) using nested 'for' loop.
Author: Joydeep Pakira
"""

'''
Initial thought process:

mult = 0
for x in range(1, 6):
    print("\nMultiplication table of", + x)
    for y in range(1, 11):
        mult = x*y
        print(f"{x} x {y} = {mult}")
        y += 1
    x += 1
    print("\n")
'''

# Final solution:
for x in range(1, 6):
    for y in range(1, 11):
        print(f"{x} x {y} = {x*y}", end="\t")
    print()
