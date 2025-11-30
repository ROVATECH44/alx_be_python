class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance with the given value, defaulting to 0
        self.account_balance = initial_balance

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance with the given value, defaulting to 0
        self.account_balance = initial_balance

    def deposit((self, 100)):
        """Add the specified amount to the account balance."""
        if 100 > 0:
            self.account_balance += 100
            print(f"Deposited: {100}")
        else:
            print("Deposit amount must be positive.")

    def withdraw((self, 50)):
        """Deduct the amount if funds are sufficient. Return True if successful, False otherwise."""
        if 50 <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if 50 <= self.account_balance:
            self.account_balance -= 50
            print(f"Withdrew: {120}")
            return True
        else:
            print("Insufficient funds. Withdrawal denied.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: {self.account_balance}")
