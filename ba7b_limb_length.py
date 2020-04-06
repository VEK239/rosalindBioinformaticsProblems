def limbLength(matrix, j):
    limb = 10e10
    for i in range(n):
        for k in range(n):
            if k == j or i == j:
                continue
            limb = min(limb, matrix[i][j] + matrix[k][j] - matrix[i][k])
    return limb // 2


matrix = []
with open("rosalind_ba7b.txt") as inf:
    n = int(inf.readline().strip())
    leaf_number = int(inf.readline().strip())
    for i in range(n):
        matrix.append(list(map(int, inf.readline().strip().split())))
print(limbLength(matrix, leaf_number))
