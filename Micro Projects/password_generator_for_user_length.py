import random
length_of_password = int(input("Enter password length: "))
characters = []
for i in range(length_of_password):
    characters.append(chr(random.randint(32, 126)))
password = "".join(characters)
print(f"Password: {password}")