row = int(input("Enter number of rows: "))
count = 2*(row-1)
for i in range(row):
    for j in range(2*row-i-1):
        if j<i:
            print(end=" ")
        else:
            print(chr(ord("A")+count), end="")
    count-=2
    print()