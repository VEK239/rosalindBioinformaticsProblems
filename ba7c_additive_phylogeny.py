def get_limb(matrix, j):
    limb = 10e10
    n = len(matrix)
    for i in range(n):
        for k in range(n):
            if k == j or i == j:
                continue
            limb = min(limb, matrix[i][j] + matrix[k][j] - matrix[i][k])
    return limb // 2


def find_inserting_place(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            if matrix[i][k] == matrix[i][n - 1] + matrix[n - 1][k]:
                return i, k


def find_nearest_nodes(edges, weights, x, i, k):
    queue = [[i]]
    visited = {i}
    res_path = []
    while len(queue) > 0:
        path = queue.pop()
        node = path[-1]
        visited.add(node)
        if node == k:
            res_path = path
            break
        for next_node in edges[node]:
            if next_node not in visited:
                queue.append(path + [next_node])
    dist = 0
    for k in range(len(res_path) - 1):
        i, j = res_path[k], res_path[k + 1]
        if dist + weights[(i, j)] > x:
            return i, j, x - dist, dist + weights[(i, j)] - x
        dist += weights[(i, j)]


def get_bald_matrix(matrix, n, limb_length):
    for i in range(n):
        matrix[i][-1] -= limb_length
        matrix[-1][i] = matrix[i][-1]
    matrix[-1][-1] = 0
    return matrix


def insert_new_node(edges, weights, v, v_weight, inserting, w, w_weight):
    new_node = v
    if v_weight != 0:
        new_node = inserting
        inserting += 1
        edges[v].remove(w)
        edges[v].append(new_node)
        edges[w].remove(v)
        edges[w].append(new_node)
        edges[new_node] = [v, w]
        weights[(new_node, v)] = v_weight
        weights[(v, new_node)] = v_weight
        weights[(new_node, w)] = w_weight
        weights[(w, new_node)] = w_weight
        del weights[(v, w)], weights[(w, v)]
    return inserting, new_node


def additivePhylogeny(matrix, n, inserting):
    if n == 2:
        return {0: [1], 1: [0]}, {(0, 1): matrix[0][1], (1, 0): matrix[0][1]}, inserting

    limb_length = get_limb(matrix, n - 1)
    bald_matrix = get_bald_matrix(matrix, len(matrix), limb_length)
    i, k = find_inserting_place(bald_matrix)

    x = matrix[i][n - 1]
    trim_matrix = [l[:-1] for l in bald_matrix[:-1]]

    current_edges, current_weights, inserting = additivePhylogeny(trim_matrix, n - 1, inserting)
    from_v, to_w, from_v_weight, to_w_weight = find_nearest_nodes(current_edges, current_weights, x, i, k)
    inserting, new_node = insert_new_node(current_edges, current_weights, from_v, from_v_weight, inserting, to_w, to_w_weight)

    current_edges[new_node].append(n - 1)
    current_edges[n - 1] = [new_node]
    current_weights[(n - 1, new_node)] = limb_length
    current_weights[(new_node, n - 1)] = limb_length

    return current_edges, current_weights, inserting


matrix = []
with open("rosalind_ba7c.txt") as inf:
    n = int(inf.readline().strip())
    for v in range(n):
        matrix.append(list(map(int, inf.readline().strip().split())))

edges, weight, _ = additivePhylogeny(matrix, n, n)

with open("out.txt", 'w') as ouf:
    for v in edges:
        for w in edges[v]:
            ouf.write(str(v) + '->' + str(w) + ':' + str(weight[(v, w)]) + '\n')
