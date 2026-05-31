


class Car:
    # The __init__ method is the constructor that initializes the attributes of the Car class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # The info method returns a formatted string with the car's details
    def info(self):
        return f"{self.year} {self.make} {self.model}"
    
    
    # The show_make method returns the make of the car
    def show_make(self):
        return f"Car Make: {self.make}"
    
    def show_model(self):
        return f"Car Model: {self.model}"

    def show_year(self):
        return f"Car Year: {self.year}"
    
my_car = Car("Toyota", "Camry", 2020) # create an instance of the Car class

print(my_car.info())  # Output: 2020 Toyota Camry
print(my_car.show_make())  # Output: Car Make: Toyota
print(my_car.show_model())  # Output: Car Model: Camry
print(my_car.show_year())  # Output: Car Year: 2020