def find_closest_cluster(distances):
    cur_min = 10e8
    cur_cluster = (-1, -1)
    for key in distances:
        if key[0] != key[1]:
            dist = distances[(key[0], key[1])]
            if dist < cur_min:
                cur_min = dist
                cur_cluster = (key[0], key[1])
    return cur_cluster, cur_min


def upgma(current_distances, n):
    tree = {}
    clusters = [i for i in range(n)]
    for i in clusters:
        tree[i] = (-1, -1, 0, 1)  # left child, right child, weight, cluster size

    while len(clusters) != 2:
        (i, j), distance = find_closest_cluster(current_distances)
        i_size = tree[i][3]
        j_size = tree[j][3]
        tree[n] = (i, j, distance / 2, i_size + j_size)

        clusters.remove(i)
        clusters.remove(j)

        new_distances = {}
        for a in clusters:
            for b in clusters:
                new_distances[(a, b)] = current_distances[(a, b)]

        for c in clusters:
            new_distances[(n, c)] = (current_distances[(i, c)] * i_size + current_distances[(j, c)] * j_size) / (
                    i_size + j_size)
            new_distances[(c, n)] = new_distances[(n, c)]

        new_distances[(n, n)] = 0

        clusters.append(n)
        current_distances = new_distances
        n += 1

    (i, j), distance = find_closest_cluster(current_distances)
    i_size = tree[i][3]
    j_size = tree[j][3]
    tree[n] = (i, j, distance / 2, i_size + j_size)

    return tree


matrix = []
with open("rosalind_ba7d.txt") as inf:
    n = int(inf.readline().strip())
    for v in range(n):
        matrix.append(list(map(int, inf.readline().strip().split())))

edges = {}
for i in range(n):
    for j in range(n):
        edges[(i, j)] = matrix[i][j]

print(upgma(edges, n))
with open("out.txt", 'w') as ouf:
    edges = upgma(edges, n)
    for key, value in edges.items():
        if value[0] != -1:
            ouf.write(str(key) + '->' + str(value[0]) + ':' + str(value[2] - edges[value[0]][2]) + '\n')
            ouf.write(str(key) + '->' + str(value[1]) + ':' + str(value[2] - edges[value[1]][2]) + '\n')
            ouf.write(str(value[0]) + '->' + str(key) + ':' + str(value[2] - edges[value[0]][2]) + '\n')
            ouf.write(str(value[1]) + '->' + str(key) + ':' + str(value[2] - edges[value[1]][2]) + '\n')
