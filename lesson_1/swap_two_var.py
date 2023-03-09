# O(1)
def swap_variables(a: int, b: int):
    print(f'Before swap: a = {a} and b = {b}')
    # temp = a
    # a = b
    # b = temp

    # a = a + b
    # b = a - b
    # a = a - b

    a, b = b, a

    print(f'After swap: a = {a} and b = {b}')


swap_variables(50, 100)