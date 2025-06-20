# Command-Line Calculator
import sys

def addition(a, b):
    """Return the sum of a and b."""
    return a + b

def subtraction(a, b):
    """Return the difference of a and b."""
    return a - b

def division(a, b):
    """Return the division of a by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def multiplication(a, b):
    """Return the product of a and b."""
    return a * b

def modulo(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        return "Error: Modulo by zero"
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

OPERATORS = {
    "+": ("Addition", addition),
    "-": ("Subtraction", subtraction),
    "/": ("Division", division),
    "*": ("Multiplication", multiplication),
    ".": ("Multiplication", multiplication),
    "%": ("Modulo", modulo),
    "**": ("Power", power)
}

def print_menu():
    print("\nAvailable operators:")
    for op, (name, _) in OPERATORS.items():
        print(f"  {op:3} : {name}")
    print()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operator():
    print_menu()
    while True:
        op = input("Input operator: ").strip()
        if op in OPERATORS:
            return op
        print("Error! Operator not defined. Please choose from the list above.")

def main():
    print("Welcome to the Command-Line Calculator!")
    history = []
    while True:
        num1 = get_number("Input first number: ")
        operator = get_operator()
        num2 = get_number("Input second number: ")

        op_name, func = OPERATORS[operator]
        result = func(num1, num2)
        print(f"Result: {num1} {operator} {num2} = {result}")
        history.append(f"{num1} {operator} {num2} = {result}")

        while True:
            action = input("\n'y' to continue, 'h' for history, 'q' to exit: ").strip().lower()
            if action == "y":
                break
            elif action == "h":
                print("\nCalculation History:")
                for entry in history:
                    print("  " + entry)
            elif action == "q":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid option. Please enter 'y', 'h', or 'q'.")

if __name__ == "__main__":
    main()