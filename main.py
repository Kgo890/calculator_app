def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x or y == 0:
        return "Cannot divide by zero"
    else:
        return x / y


def calculator():
    print("Welcome to Mr. Gore's calculator")
    response = input("Select what operation you want (add, subtract, multiply and divide): ")
    f_or_i = input("Do you want your numbers to be a float or a integer: ")

    if f_or_i == "float":
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
    elif f_or_i == "integer":
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
    else:
        return "Invalid response"

    if response == "add":
        result = add(num1, num2)
    elif response == "subtract":
        result = subtract(num1, num2)
    elif response == "multiply":
        result = multiply(num1, num2)
    elif response == "divide":
        result = divide(num1, num2)
    else:
        result = "Invalid input...Please read the instructions"

    print(f"Result: {result}")


calculator()
