# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(arr):
    even_index = 0
    odd_index = len(arr) - 1
    while even_index < odd_index:
        if arr[even_index] % 2 == 0:
            even_index += 1
        else:
            arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
            odd_index -= 1
    return arr

test_arr = [7, 3, 5, 6, 4, 10, 3, 2]
test_arr2 = [5, 3, 4, 6, 10, 9, 11]
#
# print(even_first(test_arr))
# print(even_first(test_arr2))


# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def plus_one(digits):
    new_dun = "".join(str(x) for x in digits)
    new_dun = str(int(new_dun) + 1)
    return [i for i in new_dun]

# second approach
#     carry = 1
#     for i in range(len(digits)-1, -1, -1):
#         digits[i] += carry
#         if digits[i] == 10:
#             digits[i] = 0
#             carry = 1
#         else:
#             carry = 0
#             break
#     if carry == 1:
#         digits.insert(0, 1)
#     return digits
#
#
digits_test = [1, 2, 9]
digits_test2 = [1, 8, 9, 1]
print(plus_one(digits_test))
print(plus_one(digits_test2))