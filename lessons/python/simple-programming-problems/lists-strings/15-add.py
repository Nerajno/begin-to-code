number1 = [4, 5, 6, 1, 2, 4]
number2 = [5, 6, 5, 9, 3, 2, 5, 9, 1]
max_len = len(number1)
if len(number2) > max_len:
    max_len = len(number2)
result = [0] * max_len
for i in range(max_len):
    digit1 = 0
    if i < len(number1):
        digit1 = number1[i]
    digit2 = 0
    if i < len(number2):
        digit2 = number2[i]
    result[i] += digit1 + digit2
    if result[i] >= 10:
        result[i] -= 10
        result[i + 1] += 1

print(result)
