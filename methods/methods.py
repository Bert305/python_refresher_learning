

# Lambda function to convert a string to uppercase and lowercase

lower_to_upper = lambda s: s.upper()
upper_to_lower = lambda s: s.lower()

print(lower_to_upper("hello world"))
print(upper_to_lower("HELLO WORLD"))


# String methods

# str.upper() - Converts all characters in a string to uppercase
red_to_RED = "red".upper()
print(red_to_RED)

# str.lower() - Converts all characters in a string to lowercase
Green_to_green = "GREEN".lower()
print(Green_to_green)

# The replace() method replaces a specified phrase with another specified phrase.
mom_replace = "I love my mom".replace("mom", "dad")
print(mom_replace)


# strip() - Removes any leading and trailing whitespace from the string.
my_string="Hello" 
trimmed = my_string.strip()
print(trimmed) # 'Hello' --->  Removes any leading and trailing whitespace from the string.


# split() - Splits the string into a list of substrings based on the specified separator (in this case, a comma).
my_string="Hello" 
split_text = my_string.split(",")
print(split_text) # ['Hello'] --->  Splits the string into a list of substrings based on the specified separator (in this case, a comma).



string_to_int = "123"
int_value = int(string_to_int)
print(int_value) # 123 --->  Converts a string to an integer.

int_to_string = 123
string_value = str(int_to_string)
print(string_value) # '123' --->  Converts an integer to a string.

float_to_int = 123.45
int_value = int(float_to_int)
print(int_value) # 123 --->  Converts a float to an integer.

int_to_float = 123
float_value = float(int_to_float)
print(float_value) # 123.0 --->  Converts an integer to a float.


print(type(123)) # <class 'int'> --->  Returns the type of the object.

print(type(123.45)) # <class 'float'> --->  Returns the type of the object.

print(type("123")) # <class 'str'> --->  Returns the type of the object.

print(type(True)) # <class 'bool'> --->  Returns the type of the object.

