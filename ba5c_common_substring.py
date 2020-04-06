def lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif seq1[i - 1] == seq2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]

    sequence = [""] * index
    i = m
    j = n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            sequence[index - 1] = seq1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(sequence)


with open("rosalind_ba3k.txt") as inf:
    s = inf.readline().strip()
    t = inf.readline().strip()
with open("out.txt", 'w') as ouf:
    ouf.write(lcs(s, t))
