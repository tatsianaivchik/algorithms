# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique.

def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return 0

    min_item = max_item = arr[0]
    min_index = max_index = 0
    i = 1
    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test_list1 = [2, 1, 5, 7, 8, 4]
test_list2 = [2, 9, 5, 7, 2, 1]
test_list3 = [1, 2]

print(sum_between_min_and_max(test_list1))
print(sum_between_min_and_max(test_list2))
print(sum_between_min_and_max(test_list3))