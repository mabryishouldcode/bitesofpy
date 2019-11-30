# ###############################################
# Bite 74. What day of the week were you born on?
# ###############################################

# _HINTS_
# calendar

# _DESCRIPTION_

# Complete weekday_of_birth_date which takes a date object of a birthday 
#     and returns the corresponding weekday string.

# For example Bob and Julian's birthdays return Saturday and Monday 
#     (that's why Bob is meant to relax and Julian to do all the work chuckle).

# For this Bite you want to look at the datetime and calendar modules. Have fun!

import calendar
import datetime

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # Monday = 0 ... Sunday = 6
    days_of_week = [x for x in calendar.day_name]
    birth_day = date.weekday()
    
    return days_of_week[birth_day]

# _TEST_

# def test_leonardo_dicaprio_bday():
#     dt = date(1974, 11, 11)
#     assert weekday_of_birth_date(dt) == 'Monday'

