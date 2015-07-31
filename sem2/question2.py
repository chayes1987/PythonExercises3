__author__ = 'Conor'

"""
    Q2
    (a) Write a program that:
        • First prompts the user for the number of temperatures to be processed.
        • Program reads in and stores the temperature values
        • Program prints out the maximum value, the minimum value, the average and the variance from average

        Note 1: Use input validation to ensure that a positive value is entered for the number of temperatures to be
        processed i.e. > 0. Print a message each time that an invalid temp. is entered.
        Note 2: Use input validation to ensure that temperatures read in are all >= 0. Print a message if a negative
        value is entered.
    [20]

    (b) Describe what is meant by parallel lists in Python. [5]
    A. http://stackoverflow.com/questions/5559159/what-is-meant-by-parallel-lists-in-python
"""

# A (a)
temperatures = []

num_temperatures = int(input('Enter the number of temperatures: '))
valid = False

while not valid:
    if num_temperatures < 0:
        print('Number of temperatures entered is not valid. Must be greater than zero.')
        num_temperatures = int(input('Enter the number of temperatures: '))
    else:
        valid = True

for num in range(1, num_temperatures + 1):
    temperature = float(input("Enter temperature %s: " % num))
    valid = False

    while not valid:
        if temperature < 0:
            print('Invalid temperature entered. Must be greater than zero.')
            temperature = float(input("Enter temperature %s: " % num))
        else:
            valid = True

    temperatures.append(temperature)

print(max(temperatures))
print(min(temperatures))
print(sum(temperatures) / len(temperatures))