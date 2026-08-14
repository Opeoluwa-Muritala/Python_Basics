"""
07 - Classes and OOP (Object-Oriented Programming)
-----------------------------------------------------
Classes are blueprints for creating objects that bundle together
data (attributes) and behavior (methods).
"""

class BankAccount:
    """A simple bank account class."""

    # Class attribute - shared by ALL instances of this class
    bank_name = "Mainstreet MFB"

    def __init__(self, owner, balance=0):
        # __init__ is the constructor - runs when a new object is created
        # 'self' refers to the specific instance being created
        self.owner = owner        # instance attribute
        self.balance = balance    # instance attribute

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Remove money from the account, if funds allow."""
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        # Defines what print(obj) or str(obj) displays
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


# Creating instances (objects) of the class
account1 = BankAccount("Opeoluwa", 1000)
account2 = BankAccount("Ada")  # balance defaults to 0

account1.deposit(500)
account1.withdraw(200)
print(account1)
print("Bank name (class attribute):", account1.bank_name)


# --- Inheritance: a class can extend another class ---
class SavingsAccount(BankAccount):
    """A bank account that also earns interest."""

    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)   # call the parent's __init__
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)  # reuse the parent's deposit method

    def __str__(self):
        # Overriding the parent's __str__ method
        return f"SavingsAccount(owner={self.owner}, balance={self.balance}, rate={self.interest_rate})"


savings = SavingsAccount("Bola", 10000, interest_rate=0.05)
savings.apply_interest()
print(savings)

# isinstance() checks whether an object belongs to a class (or its subclasses)
print("Is savings a BankAccount?", isinstance(savings, BankAccount))
