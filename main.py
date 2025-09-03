from data import DataProgram
from operations import Operations

def main():
    data_program = DataProgram()
    operations = Operations(data_program)
    continue_flag = "YES"

    while continue_flag != "NO":
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")

        try:
            user_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")
            continue

        if user_choice == 1:
            operations.process("TOTAL")
        elif user_choice == 2:
            operations.process("CREDIT")
        elif user_choice == 3:
            operations.process("DEBIT")
        elif user_choice == 4:
            continue_flag = "NO"
        else:
            print("Invalid choice, please select 1-4.\n")

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()