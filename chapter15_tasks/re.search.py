"""
The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where
the RegEx pattern produces a match with the string.
If the search is successful, re.search() returns a match object; if not, it returns None.
"""

import re

string = "ASython Xython is fun ,Xython is fun to learn,;et's learn python fas "
# check if 'Python' is at the beginning
match = re.search('[Pp]ython', string)



if match:
    print("pattern found inside the string")
    print(match.group())
else:
    print("pattern not found")

# Search will try to find 1st pattern ,next outputs are ignored.

