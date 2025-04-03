row = int(input("Enter number of rows: "))
count = row-1
for i in range(row):
    reset = 0
    for j in range(row+i):
        if j<count:
            print(end=" ")
        else:
            print(chr(ord("A")+reset), end="")
            if j<row-1:
                reset+=1
            else:
                reset-=1
    count-=1
    print()