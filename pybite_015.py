# ################################
# Bite 015 - Enumerate 2 sequences
# ################################

#_HINTS_
# enumerate, string formatting

#_DESCRIPTION_

# Iterate over the given names and countries lists, 
#     printing them prepending the number of the loop (starting at 1). 
#     Here is the output you need to deliver:

# 1. Julian     Australia
# 2. Bob        Spain
# 3. PyBites    Global
# 4. Dante      Argentina
# 5. Martin     USA
# 6. Rodolfo    Mexico

# Notice that the 2nd column should have a fixed width of 11 chars, 
#     so between Julian and Australia there are 5 spaces, 
#     between Bob and Spain, there are 8. 
#     This column should also be aligned to the left.

# Ideally you use only one for loop, but that is not a requirement.

# Good luck and keep calm and code in Python!

formatted_records = []

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

# just in case
fixed_width = 11

# map names/countries
name_map = dict(zip(names, countries))

def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    
    # return first column formatting
    # (ex: '1. Julian') 
    for count, name in enumerate(name_map, start=1):
        # return first column formatting
        # (ex: '1. Julian') 
        first_column = str(count) + '. ' + name

        # get number of spaces
        spaces = fixed_width - len(name)
    
        # append that many spaces and store in first_column_space add countries
        first_column += ' ' * spaces + countries[count-1]
        print(first_column)

        # add to formatted_records
        # formatted_records.append(first_column)
    
    # return formatted_records


enumerate_names_countries()



# ###################################################################
# _TESTS_
# import pytest

# from enumerate_data import enumerate_names_countries

# expected_lines = ['1. Julian     Australia',
#                   '2. Bob        Spain',
#                   '3. PyBites    Global',
#                   '4. Dante      Argentina',
#                   '5. Martin     USA',
#                   '6. Rodolfo    Mexico']


# @pytest.mark.parametrize("line", expected_lines)
# def test_enumerate_names_countries(capfd, line):
#     enumerate_names_countries()
#     output = capfd.readouterr()[0]
#     assert line in output, f'{line} not in output'

