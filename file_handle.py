try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
try:
    num = int(input("Enter an integer: "))
    print(num)
except ValueError:
    print("Invalid input! Enter only numbers")
