# A COMMAND-LINE CALCULATOR

# main function
def main():
    # Take user input
    num1 = float(input("Input first number: "))
    operator = input("Input operator: ")
    num2 = float(input("Input second number: "))

    # check for the arithemtic operator and call it function
    if operator == "+":
        print(addition(num1, num2))

    elif operator == "-":
        print(substraction(num1, num2))

    elif operator == "/":
        print(division(num1, num2))

    elif operator == "*":
        print(multiplication(num1, num2))

    else:
        print("Error! operator not defined")

        
# addition function
def addition(a,b):
    # add and return the value
    return a + b


# substraction function
def substraction(a,b):
    # subsrtact and return the value
    return a - b

# division function
def division(a,b):
    # divide and return the value
    if b == 0:
        return "Undefined"
    return a / b

# multiplication function
def multiplication(a,b):
    # multiply and return the value
    return a * b

if __name__ == "__main__":
    main()