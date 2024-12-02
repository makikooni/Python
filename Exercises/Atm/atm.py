#lets get this modular
from Atm.atmmodule import *

def main():
    # Initialize ATM with a sample account holder and initial balance
    atm = ATM("John Doe", 1000)

    # Main menu for the ATM
    while True:
        print("Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        # Get user input
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            atm.transaction_history()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
