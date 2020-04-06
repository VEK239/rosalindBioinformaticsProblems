class Vertex(object):
    def __init__(self, value):
        self.children = []
        self.parents = []
        self.value = value
        self.prefix = value[:-1]
        self.suffix = value[1:]
        self.out_degree = 0
        self.in_degree = 0
        self.is_visited = False

    def push_child(self, value):
        self.children.append(value)
        self.out_degree += 1

    def push_parent(self, value):
        self.parents.append(value)
        self.in_degree += 1

    def get_children(self):
        return self.children

    def get_degree(self):
        return self.out_degree - self.in_degree

    def get_in_out_degrees(self):
        return self.in_degree, self.out_degree

    def print_info(self):
        print(self.value, self.out_degree - self.in_degree, self.is_visited)
        print("children")
        for element in self.children:
            print("'" + element.value + "'" )
        print("parents")
        for element in self.parents:
            print("'" + element.value + "'" )


def hasLeaf(line):
    for element in resulting_leafs:
        if element.value == line:
            return True
    return False


def findLeaf(line):
    for element in resulting_leafs:
        if element.value == line:
            return element


def findStartVertex():
    v = resulting_leafs[0]
    for u in resulting_leafs:
        if u.get_degree() % 2 == 1 and u.get_degree() > 0:
            v = u
            break
    return v


def maximal_non_branching_paths():
    paths = []
    for v in resulting_leafs:
        in_degree, out_degree = v.get_in_out_degrees()
        print(v.value, in_degree, out_degree)
        if (not (in_degree == 1 and out_degree == 1)) and out_degree > 0:
            print('entered')
            v.is_visited = True
            for w in v.children:
                non_branching_path = [v, w]
                while w.in_degree == 1 and w.out_degree == 1 and v.value != w.value:
                    w.is_visited = True
                    w = w.children[0]
                    non_branching_path.append(w)
                paths.append(non_branching_path)
    return paths


resulting_leafs = []
with open("rosalind_ba3k.txt") as inf:
    line = inf.readline().strip()
    while line:
        if not hasLeaf(line[:-1]):
            resulting_leafs.append(Vertex(line[:-1]))
        if not hasLeaf(line[1:]):
            resulting_leafs.append(Vertex(line[1:]))

        prefix = findLeaf(line[:-1])
        suffix = findLeaf(line[1:])

        suffix.push_parent(prefix)
        prefix.push_child(suffix)

        line = inf.readline().strip()

paths = maximal_non_branching_paths()
with open("out.txt", 'w') as ouf:
    for path in paths:
        sequence = path[0].value
        for i in range(1,len(path)):
            sequence += (path[i].value)[-1]
        ouf.write(sequence + ' ')
