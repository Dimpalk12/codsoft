def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def calculator():
    print(color_text("\n Welcome to Simple Python Calculator", "96"))
    print(color_text("Available operations: +   -   *   /", "93"))

    # Input numbers
    num1 = float(input(color_text(" Enter the first number: ", "35")))
    operation = input(color_text("️  Choose an operation (+, -, *, /): ", "35"))
    num2 = float(input(color_text(" Enter the second number: ", "35")))

    #  calculation
    if operation == '+':
        result = num1 + num2
        print(color_text(f"{num1} + {num2} = {result}", "92"))

    elif operation == '-':
        result = num1 - num2
        print(color_text(f" {num1} - {num2} = {result}", "92"))

    elif operation == '*':
        result = num1 * num2
        print(color_text(f" {num1} * {num2} = {result}", "92"))

    elif operation == '/':
        if num2 == 0:
            print(color_text(" Error Division by zero is not allowed.", "91"))
        else:
            result = num1 / num2
            print(color_text(f" {num1} / {num2} = {result}", "92"))

    else:
        print(color_text("Invalid operation selected.", "91"))

calculator()