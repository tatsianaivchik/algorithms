# Given an array of integers, return true if the following conditions are fulfilled:
# - length of the array is bigger than or equal to 3
# - there exists some index i such that:
# a[0] < a[1] < ... < a[i]
# a[i] > a[i+1] > ... > a[a.size-1]
#
# Basically, find if there is an increasing subarray followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true

def is_mountain(arr):
    i = 1

    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1
    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i - 1] > arr[i]:
        i += 1

    if i == len(arr):
        return True

    return False

test_pos = [1, 3, 6, 7, 5]
test_neg = [1, 2, 4, 2, 3]

print(is_mountain(test_pos))
print(is_mountain(test_neg))