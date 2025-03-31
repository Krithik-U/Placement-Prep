row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(row):
        if j<i:
            print(end=" ")
        else:
            print(chr(ord("A")+row-1-i), end="")
    print()