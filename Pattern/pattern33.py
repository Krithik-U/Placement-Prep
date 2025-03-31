row = int(input("Enter number of rows: "))
for i in range(row):
    count=0
    for j in range(row):
        if j<i:
            print(end=" ")
        else:
            print(chr(ord("A")+count), end="")
            count+=1
    print()