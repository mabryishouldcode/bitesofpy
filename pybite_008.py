# ###################################
# Bite 008 - Rotate string characters
# ###################################

# _HINTS_
# deque, slicing

#_DESCRIPTION_
# Write a function that rotates characters in a string, in both directions:

# if n is positive move characters from beginning to end, 
#     e.g.: rotate('hello', 2) would return llohe

# if n is negative move characters to the start of the string, 
#     e.g.: rotate('hello', -2) would return lohel

import collections

def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """

    deq = collections.deque(string)

    deq.rotate(-n)
    
    return ''.join(deq)