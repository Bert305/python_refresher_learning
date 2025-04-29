my_list = [1,2,3,4,5]

print(my_list[ :2]) # [1,2] ---> grabbing the first 2 (length 2)
print(my_list[-1]) # 5 ---> last index of the array
print(my_list[2:-1]) # [3,4] ---> monkey in the middle (index 2 and minus length 1)
print(my_list[-3: ]) # [3,4,5] ---> grabbing the last 3 (length 3)
print(my_list[2: ]) # [3,4,5]  --> everything not counting the first 2 (not grabbing length 2)
print(my_list[ :-4]) # [1] ---> subtract length 4
print(my_list[0:2]) # [1,2] ---> first index (0) as well as the end index (2)


intro = "My name is Jeff!"

print(intro[-5:-1]) #'Jeff' --->  We can also use negative indices to print the letters from the back.
print(intro[0:2]) # 'My'



my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[3:5]) # prints (456, 789) ---> index stop at 3, cut off at length 5


print(my_list[::2]) # [1,3,5] ---> 2 is the step size, so it will print every second element