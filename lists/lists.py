# append --->  takes an item as an argument to add the item to the end of a list.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99) # appends 99 at the end of the list


# remove --> The built-in method .remove() removes an item that’s passed as the argument.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.remove(62) # removes 62 from the list


# pop ---> If no index is provided, it takes the last item from the list. Otherwise, if argument is passed, it removes that index.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'


my_list = [10, 100, 5, 8, 2]

last_one = my_list[len(my_list)-1]

my_list[2] = 10

print(my_list) # [10, 100, 10, 8, 2]
print(last_one) # 2
print(my_list[-1]) # 2


delete_number_2_from_list = [1,2,3,4,5,6]
delete_number_2_from_list.remove(2) # removes 2 from the list
del(delete_number_2_from_list[1]) # removes 2 from the list

print(delete_number_2_from_list) # [1,3,4,5,6]



turn_string_to_list = "Hello"
turn_string_to_list = list(turn_string_to_list) # converts string to list
print(turn_string_to_list) # ['H', 'e', 'l', 'l', 'o']

turn_string_to_list2 = "Hello"
print(turn_string_to_list2.split(",")) # converts string to list
# ['Hello']


my_list3 = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list3.count(2) 
print(count) 
# Output: 4

# find max number
find_max = [1,2,3,4,5]
max_number = max(find_max)
print(max_number) # 5

# find smallest number
find_min = [1,2,3,4,5]
min_number = min(find_min)
print(min_number) # 1


B=[1,2,[3,'a'],[4,'b']]
print(B[3][1]) # 'b'

[1,2,3] + [1,1,1] # [1,2,3,1,1,1]

#remember that the list is mutable, so we can change the value of the list