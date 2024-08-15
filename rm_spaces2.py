old_strings = [" hello ", "world ", " python", "computer science"]

new_strings = list(map(lambda s: s.strip(), old_strings))

print(new_strings)