ignore = [ "duplex", "alias", "Current configuration" ]

with open("switch_config.txt", "r") as config:
    for line in config:
        words = line.split()
        words_intersection = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersection:
            print(line.rstrip())
