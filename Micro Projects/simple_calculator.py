def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    user_operation = int(input("Enter your choice: "))

    if user_operation not in [1, 2, 3, 4, 5]:
        print("Invalid Choice!")
        continue
    elif user_operation == 5:
        break

    first_number = int(input("Enter First number: "))
    second_number = int(input("Enter Second number: "))

    if user_operation == 1:
        print(f'Sum of {first_number} and {second_number} is {add(first_number, second_number)}')
    elif user_operation == 2:
        print(f'Difference of {first_number} and {second_number} is {subtract(first_number, second_number)}')
    elif user_operation == 3:
        print(f'Product of {first_number} and {second_number} is {multiply(first_number, second_number)}')
    else:
        print(f'Quotient of {first_number} and {second_number} is {divide(first_number, second_number)}')