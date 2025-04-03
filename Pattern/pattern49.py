row = int(input("Enter number of rows: "))
for i in range(row):
    for j in range(2*row-i-1):
        if j<i:
            print(end=" ")
        else:
            print(2*(row-i)-1, end="")
    print()