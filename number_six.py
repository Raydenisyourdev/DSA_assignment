
matrix = [
    [0, 0, 5],
    [0, 8, 0],
    [3, 0, 0]
]

rows = []
cols = []
values = []

for i in range(3):
    for j in range(3):
        if matrix[i][j] != 0:
            rows.append(i)
            cols.append(j)
            values.append(matrix[i][j])

print("Row:", rows)
print("Column:", cols)
print("Value:", values)
