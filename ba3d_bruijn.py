import os

patterns = set()

with open("rosalind_ba3d (1).txt") as inf:
    k_mer_len = int(inf.readline().strip()) - 1
    line = inf.readline()

resulting_leafs = {}
for i in range(len(line) - k_mer_len - 1):
    line_1 = line[i: i + k_mer_len]
    line_2 = line[i + 1: i + k_mer_len + 1]
    if line_1 in resulting_leafs.keys():
        resulting_leafs[line_1].append(line_2)
    else:
        resulting_leafs[line_1] = [line_2]

print(resulting_leafs)

with open("out.txt", 'w') as ouf:
    for key in resulting_leafs.keys():
        ouf.write(key + " -> ")
        for val in resulting_leafs[key]:
            ouf.write(val + ',')
        ouf.seek(ouf.tell() - 1, 0)
        ouf.truncate()
        ouf.write('\n')
