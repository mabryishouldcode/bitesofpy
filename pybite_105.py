# ########################
# Bite 105. Slice and dice
# ########################

# _HINTS_
# replace, slicing, split, string module, strip

# _DESCRIPTION_
# Take the block of text provided and strip off the whitespace at both ends. 
#     Split the text by newline (\n).

# Loop through the lines, for each line:

# strip off any leading spaces,
#    check if the first character is lowercase,
#    if so, split the line into words and get the last word,
#    strip the trailing dot (.) and exclamation mark (!) from this last word,
#    and finally add it to the results list.
#    Return the results list.

from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
    See the Bite description for step by step instructions"""

    # list for holding only lines in lowercase with whitespace removed 
    lowercase_sort = []

    # temporary holding for items in lowercase_sort list
    container = []

    # list for holding last words
    results = []

    # STEP ONE - strip off whitespace
    text = text.strip()

    # STEP TWO - split text on new line and put into a list
    text_split = text.split('\n')

    # STEP THREE - loop through lines, strip off leading spaces in list(text_split)
    text_split_nowhitespace = [line.strip() for line in text_split]

    # STEP FOUR - check if first character lowercase, if so, add to lowercase_sort
    for line in text_split_nowhitespace:
      if line[0] not in ascii_lowercase:
        continue
      else:
        lowercase_sort.append(line)

    # STEP FIVE - split the line and .append() last word into new variable
    for line in lowercase_sort:
      container = line.split()
      results.append(container[-1].strip('.!'))

    # STEP SIX - strip (.) and (!) off last_word and store in list(results)
    return results