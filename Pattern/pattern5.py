row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row):
        print(chr(ord("A")+j), end="")
    print()