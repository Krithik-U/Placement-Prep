row = int(input("Enter number of rows: "))
for i in range(row):
    reset = 1
    for j in range(2*row-i-1):
        if j<i:
            print(end=" ")
        else:
            print(reset, end="")
            reset+=1
    print()