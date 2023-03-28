# Given an array of integers. Calculate sum and multiplication of elements.
# Return the list, calculated sum, and multiplication of elements
# Example: [1, 7, 3] Return: [11, 21]

def print_sum_and_mult(arr):
    sum = 0
    multiplication = 1
    for i in arr:
        sum += i
        multiplication *= i
    print(arr)
    print(sum)
    print(multiplication)


print(print_sum_and_mult([1, 7, 3]))