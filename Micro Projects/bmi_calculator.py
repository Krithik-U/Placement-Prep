weight = float(input("Enter weight in kgs: "))
height = float(input("Enter height in cms: "))
bmi = weight / (height/100) ** 2
print(f"The BMI value is {bmi:.2f}")