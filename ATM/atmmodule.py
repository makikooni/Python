class ATM:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []  # To store transactions

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount:.2f}")
                return True
            else:
                self.transaction_history.append(f"Failed withdrawal of ${amount:.2f} (Insufficient funds)")
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def show_transaction_history(self):
        return self.transaction_history
