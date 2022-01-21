import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(type(match))    # type is Match Object
    print(type(match.group()))    # type is String
    print(type(match.groups()))   # type is Tuple
else:
    print("pattern not found")

# Output: 801 35
