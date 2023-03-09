# O(log n)
def is_leap_year(year: int):
    if year % 4 == 0:
        if year % 100 != 0:
            print(f'{year} year is a leap year')
        else:
            if year % 400 == 0:
                print(f'{year} year is a leap year')
            else:
                print(f'{year} year is not a leap year')
    else:
        print(f'{year} year is not a leap year')

is_leap_year(2000)
is_leap_year(2424)
is_leap_year(1900)
is_leap_year(2604)
is_leap_year(3000)