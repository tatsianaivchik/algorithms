# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# 0(n)
def calculate_fibonacci_num(num):
    fib_list = [0, 1]
    for num in range(2, num + 1):
        fib_list.append(fib_list[num-1] + fib_list[num-2])

    print(fib_list[num])
    print(fib_list)

calculate_fibonacci_num(10)
calculate_fibonacci_num(100)