row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row):
        if j<row-1-i:
            print(end=" ")
        else:
            print(chr(ord("A")+i), end="")
    print()