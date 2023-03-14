
def reverse_int(x):
    if x < 0:
        print("-" + (str(x)[:0:-1]))
    else:
        print(str(x)[::-1])


reverse_int(-678)
reverse_int(123)