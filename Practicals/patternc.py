rows = 4

for i in range(rows, 0, -1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        if k % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    
    print()
