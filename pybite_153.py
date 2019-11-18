# ######################################
# Bite 153 - Round a sequence of numbers
# ######################################

# _HINTS_
# list comprehensions, math, rounding

# _DESCRIPTION_

# It's time to get mathematical! 
#     In this Bite we ask that you complete the round_up_or_down function 
#     that receives a transactions list of floats and an optional up argument.

# If up is True (default) you round them up to the nearest full integer, 
#     if it is False, you round down to the nearest full integer. 
#     Return a new list with the rounded int values.

# Use whatever method you see fit, good luck!

import math

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        round_up = [math.ceil(_) for _ in transactions]

        return round_up
    else: 
        round_down = [math.floor(_) for _ in transactions]

        return round_down

# round_up_or_down(transactions = list, boolean up=True)


#_TEST_
# from rounding import round_up_or_down

# transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
# transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]


# @pytest.mark.parametrize("transactions, up_arg, expected", [
#     (transactions1, True, [3, 4, 5, 11, 101]),
#     (transactions1, False, [2, 3, 4, 10, 100]),
#     (transactions2, True, [2, 10, 6, 7, 3]),
#     (transactions2, False, [1, 9, 5, 6, 2]),
# ])
# def test_round_up_or_down(transactions, up_arg, expected):
#     assert round_up_or_down(transactions, up=up_arg) == expected

