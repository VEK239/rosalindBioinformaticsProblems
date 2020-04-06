import re


def cycle_to_chrome(nodes):
    chrome = []
    for i in range(len(nodes) // 2):
        if nodes[2 * i] < nodes[2 * i + 1]:
            chrome.append('+' + str(nodes[2 * i + 1] // 2))
        else:
            chrome.append(str(-nodes[2 * i] // 2))
    return chrome

with open("rosalind_ba6g.txt") as inf:
    nodes = re.split(r'\(*\)', inf.readline().strip())[:-1]
    nodes = list(map(int, nodes[0][1:].split()))
    genome = cycle_to_chrome(nodes)

with open("out.txt", 'w') as ouf:
    ouf.write('(')
    ouf.write(' '.join(genome))
    ouf.write(')')
