__author__ = 'Conor'

"""
    Q2.
    (a) Briefly outline the operator hierarchy for python. (5)
    http://www.tutorialspoint.com/python/operators_precedence_example.htm

    (b) Write a python programme that reads in 3 numbers A, B and C and evaluates the following expressions:
        1. A x B^C
        2. (A + B)^B+C
        3. A^B / (B + C)
    (10)

    (c) The NoFrills airline has a 40 euro cost for all flights regardless of destination. It has however a detailed
    policy on extras.

        Luggage is charged according to weight as follows..

        First 5 kg is allowed free
        Next 5 , i.e. 6-10 kg charged at 10 euro per kilo eg. 7 kg luggage will cost 20 euro
        Above 10 kg charged at 20 euro per kilo eg. 11 kg will cost 70 euro
        Priority check in helps you avoid queues but costs 10 euro
        NoFrills have special offer whereby if you agree to sit in their extra small seats, they will give you a 20%
        discount on your total fare.

        You have to develop a python program to implement the above policy.

        Program asks user following questions:
            1. What weight is your luggage in kg?
            2. Do you want priority check in (Y or N)?
            3. Do you want a 20% discount by sitting in super economy seats (Y or N)?

        Program calculates total bill and prints this out. (15)
"""

# A (b)
A = int(input('Enter first number: '))
B = int(input('Enter second number: '))
C = int(input('Enter third number: '))

print(A * B**C)
print((A + B)**B + C)
print(A**B / (B + C))

# A (c)

total = 0
standard_fee = 40

# Add fee to total
total += standard_fee

# Take inputs
weight = float(input('What weight is your luggage (kg)?'))
priority = input('Priority check-in?')
small_seat = input('Do you want a small seat?')

weight_charges = 0
free_weight = 5

# Calculate weight charges
if weight <= free_weight:
    weight_charges = 0
elif weight <= 10:
    weight_charges = (weight - free_weight) * 10
else:
    weight_charges = (10 - free_weight) * 10 + (weight - 10) * 20

# Add weight charges to the total
total += weight_charges

# Check for priority
if priority.lower() == 'y':
    total += 10

# Check for small seat discount
if small_seat == 'y':
    total -= total * .20

# Show the total
print(total)