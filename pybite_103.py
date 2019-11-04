# #########################################################
# Bite 103 - Loop through a dictionary and pluralise a word
# #########################################################

# _HINTS_
# dict, looping

# _DESCRIPTION_

# You're given a dictionary of people and the number of games they've won.

# Use a for loop to iterate over the dictionary 
#     and print out the users name and how many games they've won in the following format: 
#     sara has won n games

# To make it human readable, pluralise the word game to suit the number of games won.

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won=games_won):
    for key, value in games_won.items():
        if value == 1:
            print(f'{key} has won {value} game')
        else:
            print(f'{key} has won {value} games')