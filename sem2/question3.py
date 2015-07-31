__author__ = 'Conor'

"""
    Q3
    (a) Write a python program that solves a common problem in web-based data
    entry. This is where web users are asked a question online and are asked to type in „yes‟ or „no‟. However, a user
    may type in Yes,yes,Y,y,No,NO,nO,N,n etc…

    Your code should read in the answer and robustly determine what was entered.
    Output an error message if you deem the input to be indecipherable as a yes/no response.
    [20]

    (b) Distinguish between the sequential and binary split search.
    A. http://stackoverflow.com/questions/700241/what-is-the-difference-between-linear-search-and-binary-search
    [5]
"""

# A (a)
answer = input('Enter answer: ')

if answer.lower() == 'yes' or answer.lower() == 'y':
    print('User entered some form of Yes')
elif answer.lower() == 'no' or answer.lower() == 'n':
    print('User entered some form of No')
else:
    print('User entered something other than Yes or No')