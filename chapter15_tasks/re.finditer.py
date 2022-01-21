import re

target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with a scoring " \
                "average of 26.12 points per game. Her weight is 51 kg. "

# finditer() with regex pattern and target string
# \d{2} to match two consecutive digits
result = re.finditer(r"\d{2}", target_string)
print(result)
print(type(result)) # Callable Iterator


for match_obj in result:
    # print each re.Match object
    print(match_obj)
    # extract each matching number
    print(match_obj.group())
