row = int(input("Enter number of rows: "))
count = row-1
for i in range(row):
    for j in range(row+i):
        if j<count:
            print(end=" ")
        else:
            print(end="*")
    count-=1
    print()