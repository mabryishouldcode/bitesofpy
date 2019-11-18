
# ################################
# Bite 115 - Count leading spaces
# ###############################

# _HINTS_

# _DESCRIPTION_
# A small but interesting Bite: 
#     given a string with leading indent spacing, 
#     calculate the amount of space (literal space, not tab or newline) characters:

# 'string  ' -> 0 (we only care about leading spacing)
# '  string' -> 2
# '    string' -> 4

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(' '))

# some_string = '         test'
# print(some_string)
# print(len(some_string.lstrip(' ')))
# print(len(some_string)-len(some_string.lstrip(' ')))

# _TESTS_

# import pytest

# from indents import count_indents


# @pytest.mark.parametrize("input_string, count", [
#    ('string  ', 0),
#    ('  string', 2),
#    ('    string', 4),
#    ('            string', 12),
#    ('\t\tstring', 0),
#    ('  str  ing', 2),
#    ('  str  ', 2),
# ])
# def test_count_indents(input_string, count):
#     assert count_indents(input_string) == count