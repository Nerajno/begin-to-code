a_list = ['I', 'am', 'a', 'teapot', 'short', 'and', 'stout']

new_list = []
for i in range(1, len(a_list), 2):
    new_list.append(a_list[i])

print(new_list)
