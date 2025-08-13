"""
Essential problems in Python; no.: 9
Objective: Given: list of temp in *C; Task: convert them to *F inside a loop & store them in a new list.
Author: Joydeep Pakira
"""
temperatures_celsius = [22, 25, 18, 30, 27, 15, 20, 24, 28, 19]
temperatures_fahrenheit = []

for temparature in temperatures_celsius:
    convert_fahrenheit = (temparature * 1.8) + 32
    temperatures_fahrenheit.append(convert_fahrenheit)

print(temperatures_fahrenheit)
