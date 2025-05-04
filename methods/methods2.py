
# reverse list of numbers
my_list = [1,2,3,4,5]
reversed_list = list(reversed(my_list))
print(reversed_list) # [5, 4, 3, 2, 1]

# reverse list of strings
fruits = ['apple', 'orange', 'banana']
x = list(reversed(fruits))
print(x)

# append list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits) # ['apple', 'banana', 'cherry', 'orange']


# extend list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


# remove list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

# insert list
insert_list = [1,2,3,4,5]
insert_list.insert(0,11)
print(insert_list)  # [11,1,2,3,4,5]

# clear list
clear_list = [1,2,3,4,5]
clear_list.clear()
print(clear_list) # []

# find max number
find_max = [1,2,3,4,5]
max_number = max(find_max)
print(max_number) # 5

# find smallest number
find_min = [1,2,3,4,5]
min_number = min(find_min)
print(min_number) # 1

my_list3 = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list3.count(2) 
print(count) 
# Output: 4

# sort numbered list
sort_list = [2,1,4,3,5]
sort_list.sort()
print(sort_list) # [1,2,3,4,5]


# remove from back
delete_from_back = [1,2,3,4,5,6]
delete_from_back.pop()
print(delete_from_back) # [1,2,3,4,5]

# removes based on index
remove_index_one = [1,2,3,4,5]
remove_index_one.pop(1)
print(remove_index_one) # [1,3,4,5]



# Tuple Methods

# max ---> returns the tuple’s maximum value.

my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
 
# my_tuple = ('abc', 234, 567, 'def')
# max(my_tuple) # throws an error!



# min --->  returns the tuple’s minimum value

my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"

# my_tuple = ('abc', 234, 567, 'def')
# min(my_tuple) # throws an error!



# index ---> takes in a value as the argument to find its index in the tuple.

my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2


# count ---> takes in a value as the argument to find the number of occurrences in the tuple.

my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1






