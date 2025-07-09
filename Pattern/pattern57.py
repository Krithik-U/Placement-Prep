row = int(input("Enter number of rows: "))
for i in range(row+1):
    reset = 1
    for j in range(i):
        print(chr(ord("A") + row - reset), end="")
        reset+=1
    print()
for i in range(row-1, 0, -1):
    reset = 1
    for j in range(i):
        print(chr(ord("A") + row - reset), end="")
        reset+=1
    print()