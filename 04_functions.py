"""
04 - Functions
---------------
Functions let you package up reusable blocks of logic.
Defined with 'def', they can accept inputs (parameters) and
return outputs.
"""

# Basic function definition
def greet(name):
    """Docstring: explains what the function does.
    This one returns a greeting message for the given name."""
    return f"Hello, {name}!"

message = greet("Opeoluwa")
print(message)

# Default parameter values - used if the caller doesn't provide one
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Adebayo"))
print(greet_with_title("Ade", title="Dr."))

# Multiple return values (Python packs them into a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([4, 9, 1, 7])
print("lowest:", lowest, "| highest:", highest)

# *args - collect any number of positional arguments into a tuple
def add_all(*numbers):
    return sum(numbers)

print("add_all:", add_all(1, 2, 3, 4))

# **kwargs - collect any number of keyword arguments into a dict
def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_profile(name="Opeoluwa", role="developer", city="Lagos")

# Functions are first-class objects: you can pass them around
def apply_twice(func, value):
    return func(func(value))

def add_five(x):
    return x + 5

print("apply_twice:", apply_twice(add_five, 10))  # 10 -> 15 -> 20

# Lambda - a small anonymous function, useful for short one-off logic
square = lambda x: x ** 2
print("square(6):", square(6))

# Common use: lambda as a sort key
people = [("Ada", 30), ("Bola", 25), ("Chike", 35)]
people_sorted = sorted(people, key=lambda person: person[1])
print("sorted by age:", people_sorted)

# Type hints (optional, but good practice for clarity/tooling)
def multiply(a: int, b: int) -> int:
    return a * b

print("multiply(3, 4):", multiply(3, 4))
