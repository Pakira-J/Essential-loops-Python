"""
Essential problems in Python; no.: 1
Objective: Calculate the sum of integers from 1 to n (user input [int:type]) using 'while' loop
Author: Joydeep Pakira
"""
n = int(input("Enter a number: "))
sum = 0
x = 0
while x <= n:
    sum += x
    x += 1

print(f"Addition of integers from 1 to {n} is equals to {sum}.")
