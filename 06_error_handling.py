"""
06 - Error Handling (try / except)
------------------------------------
Errors (exceptions) happen at runtime. Instead of letting them
crash your program, you can catch and handle them gracefully.
"""

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught error: cannot divide by zero")

# Catching multiple specific exception types
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number")
        return None
    except TypeError:
        print(f"{value} has an invalid type for conversion")
        return None

print(safe_convert("42"))
print(safe_convert("abc"))
print(safe_convert(None))

# else runs only if no exception occurred
# finally always runs, whether there was an error or not (good for cleanup)
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    else:
        print("Division succeeded")
        return result
    finally:
        print("divide() finished running")

divide(10, 2)
divide(10, 0)

# Raising your own exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(1000, 5000)
except ValueError as e:
    print("Transaction failed:", e)

# Custom exception classes - useful for domain-specific errors
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass

def withdraw_v2(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Tried to withdraw {amount}, balance is {balance}")
    return balance - amount

try:
    withdraw_v2(500, 800)
except InsufficientFundsError as e:
    print("Custom error caught:", e)
