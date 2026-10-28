A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("First Matrix:")
for row in A:
    print(row)

print("Second Matrix:")
for row in B:
    print(row)

print("Addition of Matrices:")
for row in C:
    print(row)