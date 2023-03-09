# Numbers from 1 to 100
# /3 -> "Fizz"
# /5 -> "Buzz
# /5 and /3 -> "FizzBuzz"

# O(n)

def fizzbuzz(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(30)