import re
from collections import defaultdict


def parse_to_list(genome):
    genome = re.split(r'\(*\)', genome)[:-1]
    genome = [list(map(int, el[1:].split())) for el in genome]
    return genome


def parse_to_graph(genome, graph_dict, isFirst):
    genome.append(genome[0])
    for block in genome:
        for i in range(len(block)):
            element1 = block[i - 1]
            element2 = block[i]
            graph_dict[(abs(element1), element1 > 0)].add((abs(element2), element2 < 0, isFirst))  # true if the end
            graph_dict[(abs(element2), element2 < 0)].add((abs(element1), element1 > 0, isFirst))  # true if the end
    return graph_dict


def find_cycles(graph_dict, cyclesCheck=True):
    visited = set()
    cycles = []

    for v in graph_dict.keys():
        if v not in visited:
            start = v
            cycle = [v]
            visited.add(v)

            isFromFirst = True
            while True:
                currentList = graph_dict[v]
                for element in currentList:
                    if element[2] == (not isFromFirst) or not cyclesCheck:
                        v = (element[0], element[1])
                        break
                if v == start:
                    cycles.append(cycle)
                    break
                else:
                    cycle.append(v)
                    visited.add(v)
                    isFromFirst = not isFromFirst
    return cycles


with open("rosalind_ba6c.txt") as inf:
    genome1 = parse_to_list(inf.readline().strip())
    genome2 = parse_to_list(inf.readline().strip())
    graph = defaultdict(set)
    graph = parse_to_graph(genome1, graph, True)
    blocks = find_cycles(graph, False)
    graph = parse_to_graph(genome2, graph, False)
    cycles = find_cycles(graph)

with open("out.txt", 'w') as ouf:
    ouf.write(str(len(blocks) - len(cycles)))
