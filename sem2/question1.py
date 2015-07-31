__author__ = 'Conor'

"""
Q1.
    (a) Outline briefly the various advantages of modular programming [5]
    A. http://pnagila.blogspot.ie/2012/05/advantages-and-disadvantages-of-modular_15.html

    (b) As expenses, a travelling sales representative receives 50c for the first 500 kilometres travelled and 75c for
    any remaining kilometres travelled. Write the program to calculate the amount due to the sales representative. You
    should pass the amount of kilometres travelled to a UDF and return the amount due.

    The sales representative also earns a monthly bonus based on the gross sales for that month. Pass the gross monthly
    sales to a UDF and return the bonus based on the following information:

        a. sales <= 100 bonus is €10
        b. sales between 101 and 1000 bonus is € 20
        c. sales between 1001 and 5000 bonus is €50
        d. sales > 5000 bonus is €100

    Print out the value of the total cheque, ie: the expenses plus the bonus
    [20]
"""

# A (b)


# Calculates the amount due for distance travelled
def calculate_amount_due(kilometres):
    if kilometres <= 500:
        return .50 * kilometres
    else:
        return (500 * .50) + ((kilometres - 500) * .75)


# Calculates the bonus
def calculate_bonus(sales):
    if sales <= 100:
        return 10
    elif sales <= 1000:
        return 20
    elif sales <= 5000:
        return 50
    else:
        return 100

# Test UDFs
print(calculate_amount_due(500))
print(calculate_amount_due(600))
print(calculate_bonus(90))
print(calculate_bonus(800))
print(calculate_bonus(3500))
print(calculate_bonus(9000))

# Output total cheque
print(calculate_amount_due(600) + calculate_bonus(3500))