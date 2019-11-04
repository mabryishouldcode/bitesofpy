# ###########################
# PyBite 105 - Slice and Dice
# ###########################

# _HINTS_
# list comprehensions, modulo

# _DESCRIPTION_
# Complete the function below that receives a list of numbers 
#     and returns only the even numbers that are > 0 and even (divisible by 2).

# The challenge here is to use Python's elegant list comprehension feature 
#     to return this with one line of code (while writing readable code).

numbers = [-1, 3, 99, 100, 22]

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    
    results = [items for items in numbers if (items > 0) and (items %2 == 0)]
    
    return results