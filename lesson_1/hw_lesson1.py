# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# O(n)
def sum_of_digits(n: int):
    result = 0
    for i in range(0, n + 1):
        result += i
    print(result)

# sum_of_digits(10)
# sum_of_digits(44)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

# O(n)
def find_max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num3:
        print(num2)
    else:
        print(num3)

# find_max_num(12, 5, 25)
# find_max_num(12, 5, 12)
# find_max_num(0, 4, 1)


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

# Third task: O(n)
def count_odd_and_even_digits(num):
    count_odd = 0
    count_even = 0
    origin_num = num

    while num != 0:
        temp = num % 10
        num = num // 10
        if temp % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print(f'{origin_num} number where {count_odd} odd and {count_even} even digits')


count_odd_and_even_digits(34560)
count_odd_and_even_digits(66231923000)


