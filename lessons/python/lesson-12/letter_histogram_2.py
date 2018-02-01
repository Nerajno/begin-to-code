string = "bananas"
histogram = {}
for letter in string:
    if letter not in histogram:
        histogram[letter] = 0
    histogram[letter] += 1
print(histogram)
