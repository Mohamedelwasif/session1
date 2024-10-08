def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter the number of the operation you'd like to perform: ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = num1 + num2
                operation = "adding"
            elif choice == '2':
                result = num1 - num2
                operation = "subtracting"
            elif choice == '3':
                result = num1 * num2
                operation = "multiplying"
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = "dividing"

            print(f"The result of {operation} {num1} and {num2} is {result}.")
        else:
            print("Invalid choice. Please choose a valid operation.")

        again = input("Would you like to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
