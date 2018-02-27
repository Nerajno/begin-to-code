def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
new_numbers = map(double, numbers)

new_numbers = []
for x in numbers:
    new_x = x * 2
    new_numbers.append(new_x)

for n in new_numbers:
    print(n)

new_numbers_2 = map(lambda x: x * x, numbers)

for n in new_numbers_2:
    print(n)
