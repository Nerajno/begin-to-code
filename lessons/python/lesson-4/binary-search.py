import math

numbers_input = input('Enter integers separated by commas: ')
numbers_list = list(map(int, numbers_input.split(',')))

target = int(input('Enter integer to look for: '))

left = 0
right = len(numbers_list) - 1
found_idx = -1
while True:
    middle = math.floor((right - left) / 2)
    print('middle %d, left %d, right %d' % (middle, left, right))
    number = numbers_list[middle]
    if number == target:
        found_idx = middle
        break
    elif number < target:
        left = middle
    else:
        right = middle
    if right == left:
        break

print("Found IDX: %d" % found_idx)
