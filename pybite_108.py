# ####################################################################
# Bite 108 - Loop over a dict of namedtuples calculating a total score
# ####################################################################


# _HINTS_
# counting, dict, namedtuple()

# _DESCRIPTION_

# In this Bite you calculate the total amount of points earned with Ninja Belts 
#     by accessing the given ninja_belts dict.

# You learn how to access score and ninjas (= amount of belt owners) 
#    from no less than a namedtuple (if you're new to them, check out the basic Point example in the docs).

# Why a namedtuple, you did not even mention a tuple yet?!

# Good point, well in our Bites we might actually use them even more 
#    so let's get to know them here 
#    (if you have a free evening read up on the collections module as well and thank us later).

# The function returns the total score int. You learn to write generic code 
#    because we test for an updated ninja_belts dict as well, see the TESTS tab.

from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

def get_total_points(belts=ninja_belts):
   """Calculate the amount of points rewarded on PyBites given the
      ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
      (of course there are more points but let's keep it simple)

      Make your code generic so if we update ninja_belts to include
      more belts (which we do in the tests) it will still work.

      Ah and you can get score and ninjas from the namedtuple with nice
      attribute access: belt.score / belt.ninjas (reason why we get
      you familiar with namedtuple here, because we love them and use
      them all over the place!)

      Return the total number of points int from the function.""" 
   
   total = []
   
   for belt in belts:
      belt_total = belts[belt].ninjas * belts[belt].score
      total.append(belt_total)

   return(sum(total))