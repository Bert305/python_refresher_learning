


# return the minimum and maximum numbers of the data structure in a list [min, max]
def min_max(data):
    
    min = data[0]
    
    max = data[0]
    
    
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
            
        elif data[i] > max:
            max = data[i]
            
    return [min,max]
    
    
print(min_max([2,1,4,5,3])) # [1,5]

# verify if the list contains the name "Bob" and return True or False
def name_function(names):
    
    if "Bob" in names:
        return True
    else:
        return False    
    
print(name_function(["Norbert", "Bob", "Max", "Sasha"])) # True


# return the odd characters of the string
def return_odd_characters(name):
    
    string = ""
    
    for i in range(len(name)):
        
        if i % 2 == 0:
            string += name[i]
            
    return string
         
print(return_odd_characters("Norbert")) # "Nret"




def odd_even(numbers):
    
    odd = []
    
    even = []
    
    for i in range(len(numbers)):
        
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
            
        else:
            odd.append(numbers[i])
            
    return odd + even
    
print(odd_even([1,2,3,4,5,6])) # [1,3,5,2,4,6]


# return the index of the element "Florida" in the list states
states = ["California", "Texas", "Florida", "New York", "Illinois"]

for i in range(len(states)):
    if states[i] == "Florida":
        print(f"Florida is at index {i}") # Florida is at index 2
    else:
        print("This is not Florida")
        
        
        
        
a = 10

if a == 10:
    print("a is equal to 10")
else:
    print("a is not equal to 10")
    

c = 20

d = 20

if c == 20 and d == 20:
    print("c and d are equal to 20")
elif c == 20 or d == 20:
    print("c or d is equal to 20")
else:
    print("c and d are not equal to 20")
    
    

e = 6

f = 9

if e < f:
    print("e is less than f")
else:
    print("e is not less than f")
    
    
not(True) # False
not(False) # True




    
    
    
    
        
        
    

