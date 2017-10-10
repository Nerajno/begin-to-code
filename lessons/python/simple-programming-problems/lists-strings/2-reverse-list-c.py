import math

a_list = ['I', 'am', 'a', 'teapot']

for i in range(math.floor(len(a_list) / 2) - 1):
    a_list[i], a_list[len(a_list) - i - 1] = a_list[len(a_list) - i - 1], a_list[i]

print(a_list)
