__author__ = 'Conor'

"""
    Q3.
    (a) The Met Office want you to write a python program that uses a loop to read in the weekly rainfall in 5 locations
     and determines the average rainfall. It also determines the maximum and the minimum rainfall. Your application
     should use input validation to ensure that only values >=0 are entered. It then prints out the 5 values, the
     average as well as the minimum and maximum. (20)

    (b) Use nested loops to print out the following patterns.

    1.  *****
        *****

    2. ******
       *****
       ****
       ***
       **
       *
    (10)
"""

# A (a)

# Initialize empty list
rainfall_in_locations = []

# Take inputs
for location in range(1, 6):
    rainfall = float(input('Enter rainfall for location %s: ' % location))
    valid = False

    # Input validation
    while not valid:
        if rainfall < 0:
            rainfall = float(input('Enter rainfall for location %s' % location))
        else:
            valid = True

    # Once valid, add to list
    rainfall_in_locations.append(rainfall)

# Output the required values
print(rainfall_in_locations)
print(max(rainfall_in_locations))
print(min(rainfall_in_locations))
print(sum(rainfall_in_locations) / len(rainfall_in_locations))

# A (b)

for x in range(0, 2):
    pattern = ''
    for y in range(0, 5):
        pattern += '*'
    print(pattern)

for x in range(6, 0, -1):
    pattern = ''
    for y in range(0, x):
        pattern += '*'
    print(pattern)
