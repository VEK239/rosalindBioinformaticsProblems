patterns = []

with open("rosalind_ba3c.txt") as inf:
    line = inf.readline()
    while line:
        patterns.append(line.strip())
        line = inf.readline()


resulting_leafs = {}
for line_1 in patterns:
    suffix = line_1[1:]
    for line_2 in patterns:
        if line_1 == line_2:
            continue
        prefix = line_2[:-1]
        if suffix == prefix:
            if line_1 in resulting_leafs.keys():
                resulting_leafs[line_1].append(line_2)
            else:
                resulting_leafs[line_1] = [line_2]

with open("out.txt", 'w') as ouf:
    for key in resulting_leafs.keys():
        for val in resulting_leafs[key]:
            ouf.write(key + " -> " + val + '\n')