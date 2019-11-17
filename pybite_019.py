# ################################
# Bite 19. Write a simple property
# ################################

# _HINTS_

#_DESCRIPTION_
# Write a simple Promo class. Its constructor receives a name str and expires datetime.
# Add a property called expired which returns a boolean value indicating 
#     whether the promo has expired or not.

# Checkout the tests and datetime module for more info. Have fun!

from datetime import datetime
from datetime import timedelta


NOW = datetime.now()

# print(NOW > NOW - timedelta(seconds=1))

class Promo:

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
    
    @property
    def expired(self):
        if NOW > self.deadline:
            return True
        else:
            return False



# print(coupon.deadline)
# print(coupon.expired())

# print(NOW > past_time)
# print(NOW < future_date)


# _TESTS_
#####################################################################
# def expired(name):
#     pass

# from datetime import timedelta
# import inspect

# from simple_property import Promo, NOW


# def test_promo_expired():
#     past_time = NOW - timedelta(seconds=3)
#     twitter_promo = Promo('twitter', past_time)
#     assert twitter_promo.expired


# def test_promo_not_expired():
#     future_date = NOW + timedelta(days=1)
#     newsletter_promo = Promo('newsletter', future_date)
#     assert not newsletter_promo.expired


# def test_uses_property():
#     assert 'property' in inspect.getsource(Promo)



