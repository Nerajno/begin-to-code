def merge_sorted_lists(l1, l2):
    index1 = 0
    index2 = 0
    merged_list = []
    while index1 < len(l1) or index2 < len(l2):
        if index1 == len(l1):
            merged_list.append(l2[index2])
            index2 += 1
        elif index2 == len(l2):
            merged_list.append(l1[index1])
            index1 += 1
        elif l1[index1] < l2[index2]:
            merged_list.append(l1[index1])
            index1 += 1
        else:
            merged_list.append(l2[index2])
            index2 += 1
    return merged_list

print(merge_sorted_lists([1,4,6], [2,3,5]))
print(merge_sorted_lists([3,4,8, 11], [2,3,5, 10, 14]))
