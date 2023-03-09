# O(n) OR O(1)
def sum_of_three(num: int):
    result = 0
    original_n = num

    while num != 0:
        result += (num % 10)
        num = num // 10

    print(f'Sum of all digits {original_n} is {result}')

sum_of_three(129)