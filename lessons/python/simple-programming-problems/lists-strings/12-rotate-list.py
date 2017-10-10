
def rotate(lst, k):
    result_list = []
    for i in range(len(lst)):
        idx = i + k
        if idx >= len(lst):
            idx = idx % len(lst)
        result_list.append(lst[idx])
    return result_list

a_list = [1, 2, 3, 4, 5, 6]
print(rotate(a_list, 13))
