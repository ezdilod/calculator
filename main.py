from art import logo
from replit import clear

print(logo)

# Add


def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Devide


def devide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}


def calculator():
    num1 = float(input("What's the fist number? "))
    for sym in operations:
        print(sym)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue colculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
