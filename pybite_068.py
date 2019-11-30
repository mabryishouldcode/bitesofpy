# ####################################################
# Bite 68. Remove punctuation characters from a string
# ####################################################

#_HINTS_
# string manipulation, string module

# Complete remove_punctuation which receives an input string 
#     and strips out all punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~).

# Return the resulting string. 
#     You can go full loop, 
#     list comprehension 
#     or maybe some nice stdlib functionality?

import string

input_string = '*(#)@touch#@!&$myballs'

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    no_punc = [char for char in input_string if char not in string.punctuation]
    return ''.join(no_punc)