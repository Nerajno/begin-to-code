string = "bananas"
histogram = {}
for letter in string:
    if letter in histogram:
        histogram[letter] += 1
    else:
        histogram[letter] = 1
# print(histogram)

# for entry in histogram.items():
#     print(entry[0], ":", entry[1])

print(histogram.items())
