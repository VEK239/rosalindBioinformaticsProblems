# noinspection DuplicatedCode
def multiple_lcs(seq1, seq2, seq3):
    m = len(seq1)
    n = len(seq2)
    k = len(seq3)

    L = [[[0] * (k + 1) for i in range(n + 1)] for l in range(m + 1)]
    L_coming_from = [[[0] * (k + 1) for i in range(n + 1)] for l in range(m + 1)]

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(1, m + 1):
                coming_scores = [L[l - 1][j - 1][i - 1] + int(seq1[l - 1] == seq2[j - 1] == seq3[i - 1]),
                                 L[l - 1][j][i],
                                 L[l][j - 1][i],
                                 L[l][j][i - 1],
                                 L[l - 1][j - 1][i],
                                 L[l - 1][j][i - 1],
                                 L[l][j - 1][i - 1]]
                L[l][j][i] = max(coming_scores)
                L_coming_from[l][j][i] = coming_scores.index(L[l][j][i])

    score = L[m][n][k]
    print("counted matrix")

    res_seq1, res_seq2, res_seq3 = '', '', ''
    i = k
    j = n
    l = m
    while i > 0 and j > 0 and l > 0:
        if L_coming_from[l][j][i] == 1:
            l -= 1
            res_seq1 = seq1[l] + res_seq1
            res_seq2 = '-' + res_seq2
            res_seq3 = '-' + res_seq3
        elif L_coming_from[l][j][i] == 2:
            j -= 1
            res_seq1 = '-' + res_seq1
            res_seq2 = seq2[j] + res_seq2
            res_seq3 = '-' + res_seq3
        elif L_coming_from[l][j][i] == 3:
            i -= 1
            res_seq1 = '-' + res_seq1
            res_seq2 = '-' + res_seq2
            res_seq3 = seq3[i] + res_seq3
        elif L_coming_from[l][j][i] == 4:
            l -= 1
            j -= 1
            res_seq1 = seq1[l] + res_seq1
            res_seq2 = seq2[j] + res_seq2
            res_seq3 = '-' + res_seq3
        elif L_coming_from[l][j][i] == 5:
            l -= 1
            i -= 1
            res_seq1 = seq1[l] + res_seq1
            res_seq2 = '-' + res_seq2
            res_seq3 = seq3[i] + res_seq3
        elif L_coming_from[l][j][i] == 6:
            j -= 1
            i -= 1
            res_seq1 = '-' + res_seq1
            res_seq2 = seq2[j] + res_seq2
            res_seq3 = seq3[i] + res_seq3
        else:
            i -= 1
            j -= 1
            l -= 1
            res_seq1 = seq1[l] + res_seq1
            res_seq2 = seq2[j] + res_seq2
            res_seq3 = seq3[i] + res_seq3

    d = [i, j, l]
    d.sort()

    def insert_to_start(res_seq, seq, index):
        if index == d[0]:
            res_seq = '-' * d[2] + res_seq
        elif l == d[2]:
            res_seq = seq[:d[2]] + res_seq
        else:
            res_seq = '-' * (d[2] - d[1]) + seq[:d[1]] + res_seq
        return res_seq

    res_seq1 = insert_to_start(res_seq1, seq1, l)
    res_seq2 = insert_to_start(res_seq2, seq2, j)
    res_seq3 = insert_to_start(res_seq3, seq3, i)
    return str(score) + '\n' + res_seq1 + '\n' + res_seq2 + '\n' + res_seq3


with open("rosalind_ba5m.txt") as inf:
    s = inf.readline().strip()
    t = inf.readline().strip()
    f = inf.readline().strip()
with open("out.txt", 'w') as ouf:
    ouf.write(multiple_lcs(s, t, f))
