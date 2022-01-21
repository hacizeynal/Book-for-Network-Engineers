import re

target_string = "Emma is a basketball player who was born on June 17, 1993. She played 112 matches with scoring " \
                "average 26.12 points per game. Her weight is 51 kg. "
result = re.findall(r"\d+", target_string)

print(type(result))
print(result)

# findall method is used to find to all matches
