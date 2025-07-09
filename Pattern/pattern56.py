row = int(input("Enter number of rows: "))
for i in range(row+1):
    for j in range(i):
        print(row-i+j, end="")
    print()
for i in range(row-1, 0, -1):
    for j in range(i):
        print(row-i+j, end="")
    print()