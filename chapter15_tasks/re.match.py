import re

target_string = "Emmais a basketball Emma player \n who was born on June 17, 1993"

result = re.match(r"\w{4}", target_string)

print(result.group())
print(type(result))

# Match is used to match only for beginning of string ,if there is no match it will return None
# in case of match it will return Match object
