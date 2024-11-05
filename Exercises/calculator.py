#Calculator
import math 

def display_menu():
    print("Menu:")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("5. Square root")
    print("7. Exit")
    
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an operation (1-76): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")    
    
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Only numeric values.")
            
def perform_calculation(choice,num1,num2):
    if choice ==1:
        output = num1 + num2
        return output
    elif choice ==2:
        output = num1 - num2
        return output
    elif choice == 3:
        output = num1 * num2 
        return output
    elif choice == 4:
        if num2 != 0:
            output = num1/num2 
            return output
        else:
            print("Error: Dvision by 0 doesn't exist.")
    elif choice == 5:
        output = num1**num2
        return output
    elif choice == 6:
        output = math.sqrt(num1)
    else:
        pass

def main():
    while True:
        num1 = 0
        num2 = 0
        display_menu()
        choice = get_user_choice()
        if choice == 7:
            print("Exiting...")
            break
        
        num1,num2 = get_numbers()
        output = perform_calculation(choice, num1, num2)
        print("Output: " + str(output))
        print("*****************")
        repeat = input("Again?")
        if repeat != 'yes':
            print("Exiting...")
            break
main()
