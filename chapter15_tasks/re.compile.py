import re

# Target String one
str1 = "Java's luck numbers are 251 761 231 451"

# pattern to find three consecutive digits
string_pattern = r"\d{3}"

# compile string pattern to re.Pattern object

regex_pattern = re.compile(string_pattern)

print(type(regex_pattern))

# find all the matches in string one

# Target String two

str2 = "Kelly's luck numbers are 111 212 415"

result = regex_pattern.findall(str1)
result2 = regex_pattern.findall(str2)
result3 = regex_pattern.match(str2)
result4 = regex_pattern.search(str2)
result5 = regex_pattern.finditer(str2)
print(result2)
print(result3)
for k in result5:
    print(k.group())

comp = re.compile("[Jj]ava")

re_object = comp.search(str1)
re_object2 = comp.match(str1)

print(re_object.group())
print(re_object2.group())