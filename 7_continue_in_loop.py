"""
Essential problems in Python; no.: 7
Objective: Print only odd numbers from 1 to 20 using 'for' loop and 'continue'.
Author: Joydeep Pakira
"""

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=' ')
