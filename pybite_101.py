# #########################################
# Bite 101 - f-strings and a simple if/else
# #########################################

#_HINTS_
# f-strings, if/else

#_DESCRIPTION_

# The latest way to print to the screen in Python (>= 3.6) is with f-strings.

# In this Bite we'll get you to calculate whether a person is able to drive 
#     or not based on their minimum age which is stored in the constant MIN_DRIVING_AGE.

# Print (not return) name is allowed to drive 
#     or name is not allowed to drive (note there is no period (.) at the end), 
#     based on the age being equal or greater than MIN_DRIVING_AGE.

MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
    checking the passed in age against the MIN_DRIVING_AGE constant"""
    
    if age >= MIN_DRIVING_AGE:
        print(f'{name} is allowed to drive')
    else: 
        print(f'{name} is not allowed to drive')
        
allowed_driving('tim', 17)
allowed_driving('bob', 18)
allowed_driving('julian', 19)