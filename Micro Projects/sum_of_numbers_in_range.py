start_number = int(input("Enter starting number: "))
end_number = int(input("Enter ending number: "))
sum_of_numbers = 0
for i in range(start_number, end_number+1):
    sum_of_numbers += i
print(f"Sum of Numbers from {start_number} to {end_number} is {sum_of_numbers}")