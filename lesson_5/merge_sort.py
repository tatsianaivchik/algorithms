def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
def merge_arrays(left_arr, right_arr):
    merge_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merge_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merge_list.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] <= right_arr[j]:
            merge_list.append(left_arr[i])
            i += 1
        else:
            merge_list.append(right_arr[j])
            j += 1

    return merge_list


test_list = [9, 4, 3, 1, 6, 2, 5]
print(test_list)
print(merge_sort(test_list))