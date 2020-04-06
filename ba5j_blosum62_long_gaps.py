from Bio.SubsMat.MatrixInfo import blosum62


def lcs_by_blosum62(seq1, seq2, sigma_penalty, epsilon_penalty):
    m = len(seq1)
    n = len(seq2)

    L = [[0 for j in range(m + 1)] for i in range(n + 1)]  # second arg T if is a gap to here
    L_coming_from = [[0] * (m + 1) for i in range(n + 1)]
    L[0][1] = -sigma_penalty
    L[1][0] = -sigma_penalty

    for i in range(2, n + 1):
        L[i][0] = L[i - 1][0] - epsilon_penalty
    for j in range(2, m + 1):
        L[0][j] = L[0][j - 1] - epsilon_penalty

    print("created matrix")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = L[i - 1][j - 1] + (blosum62[(seq1[j - 1], seq2[i - 1])]
                                                   if ((seq1[j - 1], seq2[i - 1]) in blosum62.keys())
                                                   else blosum62[(seq2[i - 1], seq1[j - 1])])
            if match > L[i][j]:
                L[i][j] = match
                L_coming_from[i][j] = 0

            for k in range(1, i + 1):
                new_match = L[i - k][j] - sigma_penalty - epsilon_penalty * (k - 1)
                if new_match > L[i][j]:
                    L[i][j] = new_match
                    L_coming_from[i][j] = -k # if i becomes less we do negative

            for k in range(1, j + 1):
                new_match = L[i][j - k] - sigma_penalty - epsilon_penalty * (k - 1)
                if new_match > L[i][j]:
                    L[i][j] = new_match
                    L_coming_from[i][j] = k

    score = L[n][m]
    print(L)
    print("counted matrix")

    res_seq1, res_seq2 = '', ''
    i = n
    j = m
    while i > 0 and j > 0:
        if L_coming_from[i][j] < 0:
            k = -L_coming_from[i][j]
            i -= k
            res_seq2 = seq2[i:i + k] + res_seq2
            res_seq1 = '-' * k + res_seq1
        elif L_coming_from[i][j] > 0:
            k = L_coming_from[i][j]
            j -= k
            res_seq1 = seq1[j: j + k] + res_seq1
            res_seq2 = '-' * k + res_seq2
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


with open("rosalind_ba5j (1).txt") as inf:
    s = inf.readline().strip()
    t = inf.readline().strip()
with open("out.txt", 'w') as ouf:
    ouf.write(lcs_by_blosum62(s, t, 11, 1))
