row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row):
        print(chr(ord("A")+row-1-i), end="")
    print()