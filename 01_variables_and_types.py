"""
01 - Variables and Data Types
-----------------------------
Python is dynamically typed, meaning you don't declare a variable's
type explicitly. The type is inferred from the value assigned to it.
"""

# Integers - whole numbers, positive or negative
import utils.session
age = 25
print("age:", age, "| type:", type(age))

# Floats - numbers with a decimal point
height_meters = 1.75
print("height_meters:", height_meters, "| type:", type(height_meters))

# Strings - text, wrapped in single or double quotes
name = "Opeoluwa"
print("name:", name, "| type:", type(name))

# Booleans - True or False (note the capital letters)
is_student = True
print("is_student:", is_student, "| type:", type(is_student))

# None - represents "no value" or "nothing"
middle_name = None
print("middle_name:", middle_name, "| type:", type(middle_name))

# You can reassign a variable to a different type at any time
x = 10          # x is an int
x = "ten"       # now x is a str
print("x is now:", x, "| type:", type(x))

# Multiple assignment in one line
a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

# f-strings (formatted string literals) let you embed variables in text
print(f"{name} is {age} years old and {height_meters}m tall.")

# Type conversion (casting)
age_as_text = str(age)      # int -> str
text_as_number = int("42")  # str -> int
pi_as_int = int(3.99)       # float -> int (truncates, does not round)
print("age_as_text:", age_as_text, type(age_as_text))
print("text_as_number:", text_as_number, type(text_as_number))
print("pi_as_int:", pi_as_int)
