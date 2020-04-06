from Bio.SubsMat.MatrixInfo import blosum62


def lcs_by_blosum62(seq1, seq2, sigma_penalty):
    m = len(seq1)
    n = len(seq2)

    L = [[0] * (m + 1) for i in range(n + 1)]
    L_coming_from = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        L[i][0] = -i * sigma_penalty
    for j in range(1, m + 1):
        L[0][j] = -j * sigma_penalty

    print("created matrix")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            coming_scores = [L[i - 1][j] - sigma_penalty, L[i][j - 1] - sigma_penalty,
                             L[i - 1][j - 1] + (blosum62[(seq1[j - 1], seq2[i - 1])]
                                                if ((seq1[j - 1], seq2[i - 1]) in blosum62.keys())
                                                else blosum62[(seq2[i - 1], seq1[j - 1])])]
            L[i][j] = max(coming_scores)
            L_coming_from[i][j] = coming_scores.index(L[i][j])

    score = L[n][m]
    print("counted matrix")

    res_seq1, res_seq2 = '', ''
    i = n
    j = m
    while i > 0 and j > 0:
        if L_coming_from[i][j] == 0:
            i -= 1
            res_seq2 = seq2[i] + res_seq2
            res_seq1 = '-' + res_seq1
        elif L_coming_from[i][j] == 1:
            j -= 1
            res_seq1 = seq1[j] + res_seq1
            res_seq2 = '-' + res_seq2
        else:
            i -= 1
            j -= 1
            res_seq1 = seq1[j] + res_seq1
            res_seq2 = seq2[i] + res_seq2

    if i > 0:
        res_seq2 = seq2[:i] + res_seq2
        res_seq1 = "-" * i + res_seq1

    elif j > 0:
        res_seq1 = seq1[:j] + res_seq1
        res_seq2 = "-" * j + res_seq2

    return str(score) + '\n' + res_seq1 + '\n' + res_seq2


with open("rosalind_ba5e.txt") as inf:
    s = inf.readline().strip()
    t = inf.readline().strip()
with open("out.txt", 'w') as ouf:
    ouf.write(lcs_by_blosum62(s, t, 5))
