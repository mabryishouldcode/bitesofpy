# ###############################
# Bite 16. PyBites date generator
# ###############################

#_HINTS_
# datetime, generators

#_DESCRIPTION_

# Write a generator that returns special dates for PyBites:

# Every year mark counting from PYBITES_BORN date (so 19th of Dec 2017, 19th of Dec 2018, etc)
# Every 100 days mark counting from PYBITES_BORN (29th of March 2017, 7th of July 2017, etc)
# See the tests for more details how your code will be tested: as this is a beginner's 
#     challenge we only calculate a few years ahead, leaving the next leap year (2020) out of this challenge.

# We will revisit this in an intermediate challenge. Have fun!

from datetime import datetime
from datetime import timedelta

# dynamic date
# add 100 days to date and store new value

def gen_special_pybites_dates():
    PYBITES_BORN = datetime(year=2016, month=12, day=19)
    # start = PYBITES_BORN
    start = PYBITES_BORN
    hundred_days = datetime(year=2016, month=12, day=19)
    year = datetime(year=2016, month=12, day=19)
    stop = datetime(year=2019, month=2, day=28)
    #   

    # start = 12.19.2016, until = 2.28.2019
    while start != stop:
        # daycount
        # 12.19.2016, add 1 day
        start += timedelta(days=1)

        if start == hundred_days + timedelta(days=100):
            yield start
            hundred_days += timedelta(days=100)

        if start == year + timedelta(days=365):
            yield start
            year += timedelta(days=365)

# gen = gen_special_pybites_dates()
# print(list(gen))

############################################################################
# _TESTS_
# from datetime import datetime
# from itertools import islice

# from gendates import gen_special_pybites_dates


# def test_gen_special_pybites_dates():
#     gen = gen_special_pybites_dates()
#     dates = list(islice(gen, 10))

#     expected = [datetime(2017, 3, 29, 0, 0),
#                 datetime(2017, 7, 7, 0, 0),
#                 datetime(2017, 10, 15, 0, 0),
#                 datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
#                 datetime(2018, 1, 23, 0, 0),
#                 datetime(2018, 5, 3, 0, 0),
#                 datetime(2018, 8, 11, 0, 0),
#                 datetime(2018, 11, 19, 0, 0),
#                 datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
#                 datetime(2019, 2, 27, 0, 0)]

#     assert dates == expected