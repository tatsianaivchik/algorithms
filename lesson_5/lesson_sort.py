list_int = [2, 4, 1, 87, 45, 33]
# list_int.sort()
list_int.sort(reverse=True)
# print(list_int)


list_words = ['banana', 'strawberry', 'apple', 'orange', 'kiwi']
# result_list = sorted(list_words)
# result_list = sorted(list_words, key=len)
result_list = sorted(list_words, key=len, reverse=True)
print(result_list)