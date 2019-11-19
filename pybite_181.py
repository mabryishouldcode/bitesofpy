# ########################################
# Bite 181. Keep a list sorted upon insert
# ########################################

# _HINTS_
# bisect, classes, data structures, __str__

# _DESCRIPTION_
# Complete the add method of the OrderedList class 
#     which takes a num argument and adds that to the self._numbers list 
#     keeping it ordered upon insert.

# Using a manual .sort() or .sorted() each time is not allowed. Look into the bisect module how to do it ...

# Here is how it should works:

# order = OrderedList()
# order.add(10)
# print(order)  # __str__ already provided
# order.add(1)
# print(order)
# order.add(16)
# print(order)
# order.add(5)
# print(order)
# Output:

# 10
# 1, 10
# 1, 10, 16
# 1, 5, 10, 16

import bisect

class OrderedList:

    # instantiate as list object
    def __init__(self):
        self._numbers = []

    def add(self, num):
        # you complete
        return bisect.insort_left(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)

# order = OrderedList()
# order.add(10)
# print(order)  # __str__ already provided
# order.add(1)
# print(order)
# order.add(16)
# print(order)
# order.add(5)
# print(order)

# _TEST_

# import inspect

# import pytest

# from order import OrderedList

# @pytest.fixture(scope='module')
# def order():
#     return OrderedList()


# @pytest.mark.parametrize("num, expected", [
#     (10, '10'),
#     (9, '9, 10'),
#     (16, '9, 10, 16'),
#     (2, '2, 9, 10, 16'),
#     (7, '2, 7, 9, 10, 16'),
#     (1, '1, 2, 7, 9, 10, 16'),
#     (5, '1, 2, 5, 7, 9, 10, 16'),
# ])
# def test_order(order, num, expected):
#     order.add(num)
#     assert str(order) == expected