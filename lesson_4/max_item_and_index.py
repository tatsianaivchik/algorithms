# Given a list of random numbers.
# Find and return the max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10], print [3, 76]

# O(n)
def find_max_element(arr):
    max_index = 0
    max_num = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i
    print(max_num, max_index)
    

find_max_element([1, 45, 33, 76, 9, 10, 101])