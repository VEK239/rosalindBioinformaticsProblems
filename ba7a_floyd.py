def floyd(distance):
    for i in range(len(distance)):
        for j in range(len(distance)):
            for k in range(len(distance)):
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
    return distance


edges = []

with open("rosalind_ba7a.txt") as inf:
    max_value = 0
    n = int(inf.readline().strip())
    line = inf.readline().strip()
    while (line):
        from_vertex, pair = line.split('->')
        to_vertex, weight = pair.split(':')
        from_vertex, to_vertex, weight = map(int, (from_vertex, to_vertex, weight))
        if max_value < max(from_vertex, to_vertex):
            max_value = max(from_vertex, to_vertex)
        edges.append((from_vertex, to_vertex, weight))
        line = inf.readline().strip()
print(max_value)
distance = [[0 if i == j else 10e8 for i in range(max_value + 1)] for j in range(max_value + 1)]
for element in edges:
    print(element)
    distance[element[0]][element[1]] = element[2]
print(distance)
distance = floyd(distance)

print(distance)
with open("out.txt", 'w') as ouf:
    for i in range(n):
        for j in range(n):
            ouf.write(str(distance[i][j]) + ' ')
        ouf.write('\n')
