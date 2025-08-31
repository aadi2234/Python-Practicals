start, end, columns = 1, 100, 10

for row in range(start, columns + 1):
    for col in range(row, end + 1, columns):
        print(col, end="\t")
    print()
