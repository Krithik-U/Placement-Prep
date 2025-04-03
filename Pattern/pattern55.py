row = 4
for i in range(row):
    reset = row-1
    for j in range(i+1):
        print(reset, end="")
        reset-=1
    print()
for i in range(row-1, 0, -1):
    reset = row-1
    for j in range(i):
        print(reset, end="")
        reset-=1
    print()