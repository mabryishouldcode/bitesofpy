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

NOW = datetime.now()

class Promo:
    
    def __init__(self, name):
        self.name = name

#     def __str__(self, name):
#         return '{}, {}'.format(self.name, )

#     def expired(self, name):
#         if not NOW:
#             return False

# some_value = Promo('Twitter')


