import sys


class Vertex(object):
    def __init__(self, value):
        self.children = []
        self.parents = []
        self.value = value
        self.prefix = value[:-1]
        self.suffix = value[1:]
        self.deg = 0

    def push_child(self, value):
        self.children.append(value)
        self.deg += 1

    def push_parent(self, value):
        self.parents.append(value)
        self.deg -= 1

    def get_children(self):
        return self.children

    def get_degree(self):
        return self.deg

    def print_info(self):
        print(self.value, self.deg)
        print("children")
        for element in self.children:
            print(element.value)
        print("parents")
        for element in self.parents:
            print(element.value)


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


def findEulerPath(v):
    while len(v.children) > 0:
        u = v.children[0]
        v.children.remove(u)
        findEulerPath(u)
    print(v.value)
    result.append(v.value)
    # sequence += v.value[0]


sys.setrecursionlimit(15000)

result = []
resulting_leafs = []
with open("rosalind_ba3h.txt") as inf:
    k_mer_len = int(inf.readline().strip()) - 1
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


print(findEulerPath(findStartVertex()))
print(result)

sequence = result[-1]
for i in range(len(result) - 2, -1, -1):
    sequence += result[i][-1]
with open("out.txt", 'w') as ouf:
    ouf.write(sequence)
