string = "To be or not to be"
tally = {}
for letter in string:
    letter = letter.lower()
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)

for entry in tally.items():
    print(entry[0], ":", entry[1])
