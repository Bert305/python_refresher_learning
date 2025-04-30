my_tuple = ("red", "blue", "green")

for data in my_tuple:
    print(data)
    
    
for i in range(len(my_tuple)):
    print(my_tuple[i])
    
    
print(my_tuple[-1])


# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. 
# This means that tuples cannot be changed while the lists can be modified. 
# Tuples are more memory efficient than the lists