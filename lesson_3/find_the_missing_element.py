# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# [1,2,3,4,5,6,7], [3,7,2,1,4,6]
#
# Output:
# 5 is the missing number

def find_missing_num(arr1, arr2):
    arr1.sort()
    arr2.sort()

    # for i in range(len(arr2) - 1):
    #     if arr1[i] != arr2[i]:
    #         return arr1[i]
    # return arr1[-1]

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

test_arr1 = [1,2,3,4,5,6,7]
test_arr2 = [3,7,2,1,4,6]
print(find_missing_num(test_arr1, test_arr2))