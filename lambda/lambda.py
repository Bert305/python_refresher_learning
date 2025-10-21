


lambda x: x + 10  # A lambda function that adds 10 to the input x
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15


multiply = lambda x, y: x * y  # A lambda function that multiplies two inputs x and y
print(multiply(2, 3))  # Output: 6


square = lambda x: x ** 2  # A lambda function that squares the input x
print(square(4))  # Output: 16



# Using lambda with map() to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# Using lambda with filter() to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]