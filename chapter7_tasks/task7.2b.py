ignore = [ "duplex", "alias", "Current configuration" ]
#

# version 1

# with open("switch_config.txt", "r") as config:
#     with open("new_file2","w") as new_file:
#         for line in config:
#             words = line.split()
#             words_intersection = set(words) & set(ignore)
#             if not line.startswith("!") and not words_intersection:
#                 line.rstrip()
#                 new_file.write(line)

# version 2

with open("switch_config.txt", "r") as config , open("new_file4", "w") as new_file:
    for line in config:
        words = line.split()
        words_intersection = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersection:
            line.rstrip()
            new_file.write(line)
