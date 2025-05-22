user_string = input("Enter the string: ")
number_list = []
for char in user_string:
    if char.isdigit():
        number_list.append(char)
print(number_list)