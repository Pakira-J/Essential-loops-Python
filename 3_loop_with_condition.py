"""
Essential problems in Python; no.: 3
Objective: Print all the numbers from 1 to 50 except those who are divisible by 3 & 5.
Author: Joydeep Pakira
"""

'''
Initial thought process:

for n in range(1, 51):
    if n % 3 == 0 or n % 5 == 0:
        print(end='')
    else:
        print(n, end=' ')
'''

# Final solution:
for num in range(1, 51):
    if num % 3 == 0 or num % 5 == 0:
        continue
    print(num, end=' ')
