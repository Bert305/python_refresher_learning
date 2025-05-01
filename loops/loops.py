




colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color) # prints each color in the list
    
    
names = ['Jenny', 'Parker', 'John', 'Jane']
for name in names:
    print(name) # prints each name in the list
    
    
# Using range() to iterate over a sequence of numbers
for i in range(5):
    print(i) # prints numbers from 0 to 4
    
# start, stop, increment
for i in range(0, 21, 4):
    print(i) # 4 8 12 16 20
    
    
# while loop

count = 0
while count < 5:
    print(count) # prints numbers from 0 to 4
    count += 1
    
    
student = {"name": "Jenny", "age": 26, "grade": "A"}
for key in student:
    print(f"{key} : {student[key]}") # prints each key and value in the dictionary
    # prints name : Jenny, age : 26, grade : A
    
    
for i, x in enumerate(['A', 'B', 'C']):
    print(i, x) # prints index and value of each element in the list
    
    
