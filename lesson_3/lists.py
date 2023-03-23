my_list = [2, 5, 6, 1, 2, 2]
my_second_list = [9, 15]

new_list = my_list + my_second_list
new_list.append(77)
print(new_list)

# new_list.clear()
total_twos = new_list.count(2)
index_six = new_list.index(6)
new_list.insert(1, 99)
new_list.pop(5)
print(new_list)

index_to_pop = new_list.index(77)
new_list.pop(index_to_pop)

new_list.remove(2)
new_list.reverse()
new_list.sort()

# print(total_twos)
# print(index_six)
print(new_list)
# print(new_list[-1])