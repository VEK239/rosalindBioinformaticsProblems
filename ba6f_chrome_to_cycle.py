import re


def chrome_to_cycle(genome):
    nodes = []
    for element in genome:
        for num in element:
            if num > 0:
                head = num * 2 - 1
                tail = num * 2
            else:
                head = -num * 2
                tail = -num * 2 - 1
            nodes.append(head)
            nodes.append(tail)
    return nodes

with open("rosalind_ba6f.txt") as inf:
    genome = re.split(r'\(*\)', inf.readline().strip())[:-1]
    genome = [list(map(int, el[1:].split())) for el in genome]
    genome = [str(element) for element in chrome_to_cycle(genome)]
with open("out.txt", 'w') as ouf:
    ouf.write('(')
    ouf.write(' '.join(genome))
    ouf.write(')')
