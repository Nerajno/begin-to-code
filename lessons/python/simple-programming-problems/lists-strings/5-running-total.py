a_list = [2, 8, 1, 9, 12, 6]

running_totals = []
total = 0
for num in a_list:
    running_totals.append(total)
    total += num

print(running_totals)
