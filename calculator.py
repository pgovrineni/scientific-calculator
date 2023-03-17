import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Welcome to the Scientific Calculator!")

while True:
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Goodbye!")
        break

    elif choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result: ", add(num1, num2))

        elif choice == 2:
            print("Result: ", subtract(num1, num2))

        elif choice == 3:
            print("Result: ", multiply(num1, num2))

        elif choice == 4:
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result: ", divide(num1, num2))

    elif choice == 5:
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        print("Result: ", power(num1, num2))

    elif choice == 6:
        num = float(input("Enter number: "))
        if num < 0:
            print("Cannot take square root of a negative number")
        else:
            print("Result: ", sqrt(num))

    elif choice == 7:
        num = float(input("Enter angle in radians: "))
        print("Result: ", sin(num))

    elif choice == 8:
        num = float(input("Enter angle in radians: "))
        print("Result: ", cos(num))

    elif choice == 9:
        num = float(input("Enter angle in radians: "))
        print("Result: ", tan(num))

    else:
        print("Invalid choice. Please try again.")
