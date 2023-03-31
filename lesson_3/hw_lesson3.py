# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def arithmetical_mean(arr):
    # 1st solution

    # sum = 0
    # for i in arr:
    #     sum += i
    #
    # arithmetical_mean = sum / len(arr)
    # new_arr = []
    # for i in arr:
    #     if i < arithmetical_mean:
    #         new_arr.append(i)
    # return new_arr

    # 2nd solution
    arithmetical_mean = sum(arr) / len(arr)
    new_arr = [i for i in arr if i < arithmetical_mean]
    return new_arr

arr1 = [1, 3, 5, 6, 4, 10, 2, 3]

print(arithmetical_mean(arr1))


# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest_nums(arr):
    # lowest1 = arr[0]
    # lowest2 = arr[1]
    # if lowest1 > lowest2:
    #     lowest1, lowest2 = lowest2, lowest1
    #
    # for i in range(2, len(arr)):
    #     if arr[i] < lowest1:
    #         lowest2 = lowest1
    #         lowest1 = arr[i]
    #     elif arr[i] < lowest2:
    #         lowest2 = arr[i]
    #
    # return lowest1, lowest2

    arr.sort()
    return arr[:2]

arr2 = [198, 3, 4, 9, 10, 9, 2]
print(find_two_lowest_nums(arr2))


