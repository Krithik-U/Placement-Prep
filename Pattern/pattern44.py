row = int(input("Enter number of rows: "))
count = row-1
for i in range(row):
    reset = i
    for j in range(row+i):
        if j<count:
            print(end=" ")
        else:
            print(chr(ord("A")+abs(reset)), end="")
            reset-=1
    count-=1
    print()
