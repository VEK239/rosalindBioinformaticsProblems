import re


def chrome_to_cycle(genome):
    nodes = []
    for num in genome:
        if num > 0:
            head = num * 2 - 1
            tail = num * 2
        else:
            head = -num * 2
            tail = -num * 2 - 1
        nodes.append(head)
        nodes.append(tail)
    return nodes


def cycle_to_chrome(nodes):
    chrome = []
    for i in range(len(nodes) // 2):
        if nodes[2 * i] < nodes[2 * i + 1]:
            chrome.append('+' + str(nodes[2 * i + 1] // 2))
        else:
            chrome.append(str(-nodes[2 * i] // 2))
    return chrome


def get_edges(chrome, adding):
    edges = {}
    genome = re.split(r'\(*\)', chrome)[:-1]
    genome = [list(map(int, el[1:].split())) for el in genome]
    for element in genome:
        nodes = chrome_to_cycle(element)
        for i in range(len(nodes) // 2):
            n1, n2 = nodes[2 * i + adding], nodes[(2 * i + 1 + adding) % len(nodes)]
            edges[n1] = n2
            edges[n2] = n1
    return edges


def get_colored_edges(chrome):
    return get_edges(chrome, 1)


def get_black_edges(chrome):
    return get_edges(chrome, 0)


def find_cycles(first_edges, second_edges):
    cycles = []
    visited = set()
    nodes = sorted(list(first_edges))
    while len(nodes) > 0:
        node = nodes.pop(0)
        if node in visited:
            continue
        path = []
        is_from_first = True
        while node not in visited:
            visited.add(node)
            path.append(node)
            if is_from_first:
                node = first_edges[node]
                is_from_first = False
            else:
                node = second_edges[node]
                is_from_first = True
        cycles.append(path)
    return cycles


def find_non_trivial_cycle(red_edges, blue_edges):
    cycles = find_cycles(blue_edges, red_edges)
    for cycle in cycles:
        if len(cycle) > 2:
            return cycle[0], red_edges[cycle[0]], blue_edges[cycle[0]], red_edges[blue_edges[cycle[0]]]
    return None


def graph_to_genome(black_edges, colored_edges):
    path = ''
    for cycle in find_cycles(black_edges, colored_edges):
        chrome = cycle_to_chrome(cycle)
        path += '(' + ' '.join(chrome) + ')'
    return path


def two_break_on_graph(edges, indices):
    edges[indices[0]] = indices[2]
    edges[indices[2]] = indices[0]
    edges[indices[1]] = indices[3]
    edges[indices[3]] = indices[1]


def two_break_on_genome(P, indices):
    colored_edges = get_colored_edges(P)
    two_break_on_graph(colored_edges, indices)
    return graph_to_genome(get_black_edges(P), colored_edges)


def two_break_sort(P, Q):
    yield P
    red_edges = get_colored_edges(P)
    blue_edges = get_colored_edges(Q)
    current_2break = find_non_trivial_cycle(red_edges, blue_edges)
    while current_2break is not None:
        P = two_break_on_genome(P, current_2break)
        red_edges = get_colored_edges(P)
        current_2break = find_non_trivial_cycle(red_edges, blue_edges)
        yield P


with open("rosalind_ba6d.txt") as inf:
    genome1 = inf.readline().strip()
    genome2 = inf.readline().strip()

with open("out.txt", 'w') as ouf:
    for line in two_break_sort(genome1, genome2):
        ouf.write(line + '\n')
