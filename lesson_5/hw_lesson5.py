###### Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list1 = [5, 3, 6, 1, 44, 2, 9, 101]
# print(selection_sort(test_list1))


###### Bubble Sort
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_list2 = [5, 4, 7, 9, 1, 6, 55, 11, 2]
# print(bubble_sort(test_list2))


###### Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


test_list3 = [5, 4, 7, 9, 1, 6, 87, 11, 0]
# print(insertion_sort(test_list3))


###### Merge Sort
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
        if left_arr[i] >= right_arr[j]:
            merge_list.append(left_arr[i])
            i += 1
        else:
            merge_list.append(right_arr[j])
            j += 1

    return merge_list


test_list4 = [33, 9, 4, 3, 0, 6, 2, 5, 77]
# print(merge_sort(test_list4))