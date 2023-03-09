# O(n)
def factorial(num: int):
    result = 1
    for i in range(2, num + 1):
        result *= i
    print(f'Factorial of {num} is {result}')

factorial(5)
