

# A class is a blueprint or template for creating objects. It defines the structure and behavior that its objects will have.



class User():
    
    def __init__(self,name,age,email,gender):
        # holds details about the user
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
        
user_1 = User("Bob", 30, "bob@gmail.com", "Male")

user_2 = User("Ashley", 25, "ashley@gmail.com", "Female")

print(user_1.name)
print(user_2.age)
print(f"My name is {user_1.name} and I am {user_1.age} years old.")


class Colors():
    def __init__(self,color):
        self.color = color

red = Colors("red")
green = Colors("green")
blue = Colors("blue")        
    

print(f"My favorite color is {red.color}")


class MyCar:
    def __init__(self, car):
        self.car = car
 
 
x = MyCar('Honda')
y = MyCar("Toyota")

print(f"I was able to purchase a new {x.car} today from the dealership.")