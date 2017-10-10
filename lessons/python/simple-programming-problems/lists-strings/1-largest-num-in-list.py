largest = 0
numbers = [2, 8, 4, 9, 12, 3, 4]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is %d." % largest)
