"""
Essential problems in Python; no.: 8
Objective: A loop to print key-value pair in a given dictionary.
Author: Joydeep Pakira
"""

student = {'name': "Sumit", 'age': 23, 'branch': "ECE", 'id_no': 202500250163}

for key, value in student.items():
    print(f"{key} : {value}")
