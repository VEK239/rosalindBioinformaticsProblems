def lcs(seq1, seq2, sigma_penalty):
    m = len(seq1)
    n = len(seq2)

    L = [[0] * (m + 1) for i in range(n + 1)]
    L_coming_from = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        L[i][0] = -i * sigma_penalty
    for j in range(1, m + 1):
        L[0][j] = -j * sigma_penalty

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            coming_scores = [L[i - 1][j] - sigma_penalty, L[i][j - 1] - sigma_penalty,
                             L[i - 1][j - 1] + (1 if seq1[j - 1] == seq2[i - 1] else -1)]
            L[i][j] = max(coming_scores)
            L_coming_from[i][j] = coming_scores.index(L[i][j])

    score = L[n][m]

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

    return score, res_seq1, res_seq2


if __name__ == "__main__":
    s, t = input().split()
    score, res_s, res_t = lcs(s, t, 1)
    # print(score)
    print(res_s, res_t)
