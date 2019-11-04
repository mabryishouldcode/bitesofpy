# #####################
# Bite 1. Sum n numbers
# #####################

#_HINTS_

#_DESCRIPTION_
# Write a function that can sum up numbers:

# It should receive a list of n numbers.
# If no argument is provided, return sum of numbers 1..100.
# Look closely to the type of the function's default argument ...
# Have fun!

def sum_numbers(numbers=None):
    if numbers is None:
        numbers = sum(range(0,101))

        return numbers
    else:
        return sum(numbers)
