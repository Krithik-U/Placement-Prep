row = 5
for i in range(row):
    reset=0
    for j in range(2*row-i-1):
        if j<i:
            print(end=" ")
        else:
            print(chr(ord("A")+reset), end="")
            reset+=1
    print()