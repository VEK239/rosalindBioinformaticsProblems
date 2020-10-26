def base_pair(rna, i, j):
    pair = [rna[i], rna[j]]
    return 1 if 'A' in pair and 'U' in pair or 'G' in pair and 'C' in pair else 0


def get_scoring_matrix(rna):
    N = len(rna)
    scoring_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for L in range(1, N):
        for i in range(0, N - L):
            j = i + L
            if j - i >= 4:
                fragments_case = max(scoring_matrix[i][k] + scoring_matrix[k + 1][j] for k in range(i + 1, j))
                scoring_matrix[i][j] = max(scoring_matrix[i + 1][j], scoring_matrix[i][j - 1],
                                           scoring_matrix[i + 1][j - 1] + base_pair(rna, i, j), fragments_case)
            else:
                scoring_matrix[i][j] = 0
    return scoring_matrix


def get_pairs(scoring_matrix, rna, i, j, pair):
    if j - i >= 4:
        if scoring_matrix[i][j] == scoring_matrix[i + 1][j - 1] + base_pair(rna, i, j):
            pair.append([i, j, str(rna[i]), str(rna[j])])
            get_pairs(scoring_matrix, rna, i + 1, j - 1, pair)
        elif scoring_matrix[i][j] == scoring_matrix[i + 1][j]:
            get_pairs(scoring_matrix, rna, i + 1, j, pair)
        elif scoring_matrix[i][j] == scoring_matrix[i][j - 1]:
            get_pairs(scoring_matrix, rna, i, j - 1, pair)
        else:
            for k in range(i + 1, j):
                if scoring_matrix[i][j] == scoring_matrix[i][k] + scoring_matrix[k + 1][j]:
                    get_pairs(scoring_matrix, rna, i, k, pair)
                    get_pairs(scoring_matrix, rna, k + 1, j, pair)
                    break
    return pair


if __name__ == "__main__":
    rna = input().strip()
    s = get_scoring_matrix(rna)
    print(s[0][-1])
    # print(get_pairs(s, rna, 0, len(rna) - 1, []))

