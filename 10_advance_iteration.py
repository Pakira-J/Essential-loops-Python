"""
Essential problems in Python; no.: 10
Objective: Use a loop with enumerate() to print each list element along with its index.
Author: Joydeep Pakira
"""

car_manufacturers = [
    "Toyota",
    "Honda",
    "Ford",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Hyundai",
    "Kia",
    "Chevrolet",
    "Volkswagen"
]

for index, item in enumerate(car_manufacturers):
    print(f"Index = {index} : Manufacturer = {item}")
