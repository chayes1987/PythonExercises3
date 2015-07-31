__author__ = 'Conor'

"""
    Q4
    (a) Explain why file handling is a critical requirement for any programming language. [5]
    A. Files can be unpredictable, e.g. doesn't exist, already opened by someone else

    (b) Write a program that reads in the text from a file and copies it to a second file. User is asked to enter the
    name of the original input file and the created copyfile.
    [15]

    (c) Explain the following : f= open(“StudentData.dat”, “w”)
    A. Opening a file in write mode
    [5]
"""

# A (b).

# Get name of file
original_file = input('Enter name of file: ')

# Try block to catch exceptions
try:
    # Open file
    my_file = open(original_file)
    # Store contents
    contents = my_file.read()
    my_file.close()
except FileNotFoundError:
    print('The file \'%s\' was not found.' % original_file)
    pass

# Get name of destination file
destination_file = input('Enter name of destination file: ')

# Try block to catch exceptions
try:
    # Open file, a for append mode
    dest_file = open(destination_file, 'a')
    # Write the contents of the first file
    dest_file.write(contents)
    dest_file.close()
except Exception:
    print('Error writing file')
    pass

# Open in read mode to show contents
print(open(destination_file, 'r').read())
