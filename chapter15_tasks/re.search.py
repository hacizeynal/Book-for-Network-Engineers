import re

string = "ASython Xython is fun ,Xython is fun to learn,;et's learn python fas "
# check if 'Python' is at the beginning
match = re.search('[Pp]ython', string)

if match:
    print("pattern found inside the string")
    print(match.group())
else:
    print("pattern not found")

# Search will try to find 1st match ,next outputs are ignored.