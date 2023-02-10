# Psuedo code 
"""
keep track of:
    gas price, distance, miles per gallon

calculate cost

"""

print("Welcome to the trip cost calculator")

gas_price = float(input("What is the gas price? "))
distance = float(input("how far will you go in miles?"))
mpg = float(input("How many miles per gallon does your car get?"))
total = (distance/mpg) * mpg

print(f"the total cost for your trip will be ${total}")

retry = input("do you want to run the program again(y/n)")






