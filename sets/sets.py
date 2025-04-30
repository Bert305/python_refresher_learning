

# Sets are one of the built-in data structures in Python.

# A set is an immutable, unordered collection of unique elements that can consist of integers, floats, strings and tuples.



# A set is created with curly braces {} with items inside the braces separated by commas.
set1 = {'Jenny', 26, 'Parker', 10.5} 
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}





# The built-in function set() can be used with a list argument to create a set from that list.
lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set2 = set(lst)
print(set2) # prints {10.5, 26, 'Jenny', 'Parker'}



# Sets do not have indexes or keys. We can use keyword in to check to see if the element exists in the set:

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
print('Chau' in students) # returns True




# add

# Because sets are immutable, existing elements within the sets cannot be changed.

# However, new elements can be added using the built-in method add()

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
students.add('George')
print('George' in students) # returns True


# update
# The built-in method .update() takes in any iterable object, such as tuples, lists, dictionaries or sets, 
# and adds the object to an existing set. Any duplicated elements will not be added.
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students1.update(students2)

print(students1) # returns {'Lily', 'Carlos', 'Alice', 'Dmitry', 'Zhuo', 'Jane', 'Amy', 'Bridgette', 'Chau'}



# remove
# The built-in method .remove() takes in an element and removes it from the set.
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students.remove('Bridgette')
print(students) # {'Jane', 'Carlos', 'Chau', 'Dmitry', 'Amy'}


# Because sets are iterable, we can utilize a for loop to iterate through a set.
count_down = set([9, 8, 7, 6, 5, 4, 3, 2, 1])
for num in count_down:
   print(num, 'seconds left!')
   
   
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1 & set2
print(set3) # {4, 5} --->  Representing a venn diagram, the intersection is the area where two circles overlap.

# Add a new element to a set
V={'A','B'}
V.add('C')
print(V) # {'A', 'B', 'C'}

