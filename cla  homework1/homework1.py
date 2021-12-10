my_list= list(range(2,299,2))
print(my_list)

length=len(my_list)
print(length)

squared_list = [number ** 2 for number in my_list]
print(squared_list)

contains_num = 57 in my_list
print(contains_num)