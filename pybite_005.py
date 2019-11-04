# ################################
# Bite 005 - Parse a list of names
# ################################

# _HINTS_
# lambda, list comprehensions, min, sorting

# _DESCRIPTION_
# In this bite you will work with a list of names.
# First you will write a function to take out duplicates and title case them.
# Then you will sort the list in alphabetical descending order by surname 
#     and lastly determine what the shortest first name is. 
#     For this exercise you can assume there is always one name and one surname.

# With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""

    # remove duplicates from [names] with set() and cast to list([del_dupes])
    del_dupes = list(set(names))

    # iterate through del_dupes and .title() case items, assign to [names]       
    names = [_.title() for _ in del_dupes]

    # output: ['Sandra Bullock', 'Alec Baldwin', 'Julbob Pybites', 'Matt Damon', 'Al Pacino', 'Keanu Reeves', 'Bob Belderbos',...]
    return sorted(names)

# TEST VALS
# def test_dedup_and_title_case_names():
#     names = dedup_and_title_case_names(NAMES)
#     assert names.count('Bob Belderbos') == 1
#     assert names.count('julian sequeira') == 0
#     assert names.count('Brad Pitt') == 1
#     assert len(names) == 10
#     assert all(n.title() in names for n in NAMES)



def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""

    # input: ['Sandra Bullock', 'Alec Baldwin', 'Julbob Pybites', 'Matt Damon', 'Al Pacino', 'Keanu Reeves', 'Bob Belderbos',...]
    names = dedup_and_title_case_names(names)

    # sort names in descending order
    # ['Julian Sequeira', 'Arnold Schwarzenegger', 'Keanu Reeves', 'Julbob Pybites', 'Brad Pitt', 'Al Pacino', 'Matt Damon', 'Sandra Bullock', 'Bob Belderbos', 'Alec Baldwin']
    names = sorted(names, key=lambda x: x.split(' ')[-1], reverse=True)

    # output: ['Julian Sequeira', 'Arnold Schwarzenegger', 'Keanu Reeves', 'Julbob Pybites', 'Brad Pitt', 'Al Pacino', 'Matt Damon', 'Sandra Bullock', 'Bob Belderbos', 'Alec Baldwin']
    return names
    
def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    # input: ['Julian Sequeira', 'Arnold Schwarzenegger', 'Keanu Reeves', 'Julbob Pybites', 'Brad Pitt', 'Al Pacino', 'Matt Damon', 'Sandra Bullock', 'Bob Belderbos', 'Alec Baldwin']
    names = dedup_and_title_case_names(names)

    # fname_lname = [('Keanu', 'Reeves'), ('Julbob', 'Pybites'), ('Julian', 'Sequeira'), ('Matt', 'Damon'), ('Arnold', 'Schwarzenegger'), ('Brad', 'Pitt'), ('Alec', 'Baldwin'), ('Bob', 'Belderbos'), ('Sandra', 'Bullock'), ('Al', 'Pacino')]
    fname_lname = [tuple(_.split()) for _ in names]
    
    # iterate through [(fname_lname)] and assign 'first name' to [f_name]
    f_name = [x[0] for x in fname_lname]

    # grab min [f_name] using len()
    f_name = min(f_name, key=len)

    return f_name