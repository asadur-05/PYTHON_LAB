mat = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        result[j][i] = mat[i][j]
print("Original Matrix:")
for row in mat:
    print(row)
print("Transposed Matrix:")
for r in result:
    print(r)
