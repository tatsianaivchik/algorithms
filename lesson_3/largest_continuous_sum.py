# Given an array of integers (positive and negative) find the largest continuous sum.

def find_sum(arr):
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


test_arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]  # 29
result = find_sum(test_arr)
print(result)