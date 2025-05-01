


# inheritance is a way to create a new class that is a modified version of an existing class. The new class is called the child class, and the existing class is called the parent class. The child class inherits all the attributes and methods of the parent class, and can also have its own attributes and methods.



# parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is a {self.species}"
    
# child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the parent class constructor
        self.breed = breed
        

    def make_sound(self):
        return "Woof Woof"
    
    
def info(self):
    return f"{self.name} is a {self.species} of breed {self.breed}"



# Create an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.info())  # Output: Buddy is a Dog of breed Golden Retriever
print(my_dog.make_sound())  # Output: Woof Woof
print(my_dog.species)  # Output: Dog
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
print(info(my_dog))  # Output: Buddy is a Dog of breed Golden Retriever