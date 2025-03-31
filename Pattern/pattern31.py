row = int(input("Enter number of rows: "))
for i in range(row):
    count=1
    for j in range(row):
        if j<i:
            print(end=" ")
        else:
            print(count, end="")
            count+=1
    print()