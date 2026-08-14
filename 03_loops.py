"""
03 - Loops (for, while)
------------------------
Loops let you repeat actions. Python has two main loop types:
'for' (iterate over a sequence) and 'while' (repeat until a
condition becomes False).
"""

# --- for loop over a range ---
# range(5) generates 0, 1, 2, 3, 4 (stops BEFORE 5)
for i in range(5):
    print("range loop:", i)

# range(start, stop, step)
for i in range(2, 10, 2):
    print("even number:", i)

# --- for loop over a list ---
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("fruit:", fruit)

# enumerate() gives you both the index and the value
for index, fruit in enumerate(fruits):
    print(f"index {index}: {fruit}")

# --- for loop over a dictionary ---
prices = {"apple": 200, "banana": 100, "mango": 350}
for key, value in prices.items():
    print(f"{key} costs {value} naira")

# --- while loop ---
# Repeats as long as the condition is True
count = 0
while count < 3:
    print("while count:", count)
    count += 1  # shorthand for count = count + 1

# --- break and continue ---
# break exits the loop immediately
# continue skips to the next iteration
for n in range(10):
    if n == 5:
        break        # stop the loop entirely once n reaches 5
    if n % 2 == 0:
        continue     # skip even numbers, go to next n
    print("odd number before break:", n)

# --- loop with else ---
# The 'else' block runs only if the loop completes WITHOUT hitting 'break'
for n in range(3):
    print("searching...", n)
else:
    print("loop finished without a break")

# --- list comprehension (compact way to build a list from a loop) ---
squares = [x**2 for x in range(6)]
print("squares:", squares)

# comprehension with a condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("even_squares:", even_squares)
