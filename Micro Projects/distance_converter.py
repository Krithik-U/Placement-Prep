def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    print(f"{kilometers} kilometers is equal to {miles:.6f} miles\n")

def miles_to_kilometers(miles):
    kilometers = miles * 1.609344
    print(f"{miles} miles is equal to {kilometers:.6f} kilometers\n")

while True:
    print("1. Kilometers to Miles\n2. Miles to Kilometers\n3. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice not in [1, 2, 3]:
        print("Invalid Choice!\n")
        continue
    elif user_choice == 1:
        kilometers_to_convert = float(input("Enter Kilometers: "))
        kilometers_to_miles(kilometers_to_convert)
    elif user_choice == 2:
        miles_to_convert = float(input("Enter miles: "))
        miles_to_kilometers(miles_to_convert)
    else:
        break