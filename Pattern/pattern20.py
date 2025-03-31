row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row-i):
        print(row-i, end="")
    print()