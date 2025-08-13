"""
Essential problems in Python; no.: 2
Objective: To print numbers from 1 to 10 on the same line using 'for' loop
Author: Joydeep Pakira
"""

'''
Initial thought process: 

n = 0
for n in range(10):
    n += 1
    print(n, end=" ")       # end parameter is used as to give space in b/w two 
                              consecutive numbers. 
'''

# Final code:
for num in range(1, 11):
    print(num, end=' ')
