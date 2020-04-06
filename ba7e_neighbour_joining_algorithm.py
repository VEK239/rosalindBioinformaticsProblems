from collections import defaultdict


def find_closest_cluster(matrix):
    cur_min = 10e8
    cur_cluster = (-1, -1)
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] < cur_min:
                cur_min = matrix[i][j]
                cur_cluster = (i, j)
    return cur_cluster


def get_star_matrix(matrix, n):
    total_dist = defaultdict(int)
    for i in matrix:
        for j in matrix[i]:
            total_dist[i] += matrix[i][j]
    star_matrix = {}
    for i in matrix:
        star_matrix[i] = {}
        for j in matrix[i]:
            if i == j:
                star_matrix[i][j] = 0
            else:
                star_matrix[i][j] = (n - 2) * matrix[i][j] - total_dist[i] - total_dist[j]
    return star_matrix, total_dist


def neighbour_joining(matrix, n, inserting):
    if n == 2:
        edges = {}
        weights = {}
        for i in matrix:
            for j in matrix[i]:
                if j != i:
                    edges[i] = [j]
                    edges[j] = [i]
                    weights[(i, j)], weights[(j, i)] = matrix[i][j], matrix[i][j]
        return edges, weights
    star_matrix, total_distances = get_star_matrix(matrix, n)
    i, j = find_closest_cluster(star_matrix)
    delta = (total_distances[i] - total_distances[j]) / (n - 2)
    limb_i = (matrix[i][j] + delta) / 2
    limb_j = (matrix[i][j] - delta) / 2
    #   Dk, m = Dm, k = (1 / 2)(Dk, i + Dk, j - Di, j) for any k
    matrix[inserting] = {inserting: 0}
    for element in matrix:
        if element == inserting:
            continue
        matrix[element][inserting] = (matrix[element][i] + matrix[element][j] - matrix[i][j]) / 2
        matrix[inserting][element] = matrix[element][inserting]
    #   remove rows/columns i, j
    del matrix[i], matrix[j]
    for element in matrix:
        del matrix[element][i], matrix[element][j]

    edges, weights = neighbour_joining(matrix, n - 1, inserting + 1)

    edges[i] = [inserting]
    edges[inserting].append(i)
    edges[j] = [inserting]
    edges[inserting].append(j)
    weights[(i, inserting)], weights[(inserting, i)] = limb_i, limb_i
    weights[(j, inserting)], weights[(inserting, j)] = limb_j, limb_j
    return edges, weights


matrix = {}
with open("rosalind_ba7e (1).txt") as inf:
    n = int(inf.readline().strip())
    for v in range(n):
        matrix[v] = {}
        for u, w in enumerate(list(map(int, inf.readline().strip().split()))):
            matrix[v][u] = w

edges, weights = neighbour_joining(matrix, n, n)

with open("out.txt", 'w') as ouf:
    for v in edges:
        for w in edges[v]:
            ouf.write(str(v) + '->' + str(w) + ':' + str(weights[(v, w)]) + '\n')
