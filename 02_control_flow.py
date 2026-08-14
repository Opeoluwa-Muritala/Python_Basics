"""
02 - Control Flow (if / elif / else)
-------------------------------------
Control flow lets your program make decisions and take different
paths depending on conditions. Python uses indentation (whitespace)
instead of braces {} to define code blocks.
"""

score = 72

# Basic if / elif / else chain
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} -> Grade {grade}")

# Comparison operators: == != > < >= <=
# Logical operators: and, or, not
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Ternary (inline if/else) - useful for short conditional assignments
status = "adult" if age >= 18 else "minor"
print("status:", status)

# Truthy / Falsy values
# Falsy: 0, 0.0, "", [], {}, None, False
# Everything else is generally truthy
value = ""
if value:
    print("value is truthy")
else:
    print("value is falsy (empty string)")

# 'in' operator checks membership
fruits = ["apple", "banana", "mango"]
if "banana" in fruits:
    print("banana is in the list")

# match statement (Python 3.10+) - similar to switch/case in other languages
def describe_number(n):
    match n:
        case 0:
            return "zero"
        case 1 | 2 | 3:
            return "small"
        case _ if n < 0:
            return "negative"
        case _:
            return "large"

for n in [0, 2, -5, 100]:
    print(f"{n} -> {describe_number(n)}")
