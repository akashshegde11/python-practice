# Simple Calculator Program


def add_num(num1, num2):
    return num1 + num2


def subtract_num(num1, num2):
    return num1 - num2


def multiply_num(num1, num2):
    return num1 * num2


def divide_num(num1, num2):
    return num1 / num2


print(
    "Please select operation:\n"
    "1. Add\n"
    "2. Subtract\n"
    "3. Multiply\n"
    "4. Divide\n"
)


select = input("Select your desired operation from the above given list: ")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if select == '1':
    print(num_1, "+", num_2, "=", add_num(num_1, num_2))

elif select == '2':
    print(num_1, "-", num_2, "=", subtract_num(num_1, num_2))

elif select == '3':
    print(num_1, "*", num_2, "=", multiply_num(num_1, num_2))

elif select == '4':
    print(num_1, "/", num_2, "=", divide_num(num_1, num_2))

else:
    print("Invalid input")
