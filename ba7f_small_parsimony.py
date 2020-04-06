from collections import defaultdict

alphabet = ['A', 'C', 'T', 'G']


class Vertex:
    def __init__(self, string=''):
        self.resulting_string = string
        self.is_processed = string != ''
        self.letter_dict = {index: {'A': 0 if letter == 'A' else 1,
                                    'C': 0 if letter == 'C' else 1,
                                    'T': 0 if letter == 'T' else 1,
                                    'G': 0 if letter == 'G' else 1} for index, letter in enumerate(string)}
        self.cost = 0

    def print_info(self):
        print(self.resulting_string, self.cost, self.letter_dict)


def small_parsimony(graph, length):
    for index in range(len(graph) - 1, -1, -1):
        vertex = graph[index]
        if vertex.is_processed:
            continue
        else:
            daughter = graph[2 * index + 1]
            son = graph[2 * index + 2]
            current_daughter_dict = {}
            current_son_dict = {}
            for index in daughter.letter_dict.keys():
                current_daughter_dict[index] = {}
                current_son_dict[index] = {}
                for letter in alphabet:
                    current_daughter_dict[index][letter] = 10e8
                    current_son_dict[index][letter] = 10e8
                    for d_letter in daughter.letter_dict[index]:
                        current_daughter_dict[index][letter] = min(daughter.letter_dict[index][d_letter] +
                                                                   (1 if d_letter != letter else 0),
                                                                   current_daughter_dict[index][letter])
                        current_son_dict[index][letter] = min(son.letter_dict[index][d_letter] +
                                                              (1 if d_letter != letter else 0),
                                                              current_son_dict[index][letter])
            for index in current_daughter_dict.keys():
                vertex.letter_dict[index] = {'A': current_daughter_dict[index]['A'] + current_son_dict[index]['A'],
                                             'C': current_daughter_dict[index]['C'] + current_son_dict[index]['C'],
                                             'T': current_daughter_dict[index]['T'] + current_son_dict[index]['T'],
                                             'G': current_daughter_dict[index]['G'] + current_son_dict[index]['G']}
            for i in range(length):
                cur_min = (None, 10e8)
                for item in vertex.letter_dict[i].items():
                    if item[1] < cur_min[1]:
                        cur_min = item
                vertex.resulting_string += cur_min[0]
                vertex.cost += cur_min[1]


def reconstruct(graph, length):
    for index, element in enumerate(graph):
        if index != 0 and index < n - 1:
            parent = graph[(index - 1) // 2]
            element.resulting_string = ''
            for i in range(length):
                cur_min_value = 10e8
                cur_variant = set()
                for item in element.letter_dict[i].items():
                    if item[1] <= cur_min_value:
                        cur_min_value = item[1]
                        cur_variant = item[0]
                if cur_min_value + 1 < element.letter_dict[i][parent.resulting_string[i]]:
                    element.resulting_string += cur_variant
                else:
                    element.resulting_string += parent.resulting_string[i]


def hamm(s, t):
    d = 0
    for index, symbol in enumerate(s):
        if symbol != t[index]:
            d += 1
    return str(d)


with open("rosalind_ba7f (1).txt") as inf:
    n = int(inf.readline().strip())
    vertices = [Vertex() for i in range(2 * n - 1)]
    vert_dict = defaultdict(list)
    dict_index_to_heap = {2 * n - 2: 0}
    for i in range(2 * n - 2):
        from_v, to_w = inf.readline().strip().split('->')
        vert_dict[int(from_v)].append(to_w)
    for i in range(2 * n - 2, n - 1, -1):
        left, right = vert_dict[i][0], vert_dict[i][1]
        index_in_heap = dict_index_to_heap[i]
        if left.isdigit():
            dict_index_to_heap[int(left)] = index_in_heap * 2 + 1
            dict_index_to_heap[int(right)] = index_in_heap * 2 + 2
        else:
            word_length = len(left)
            vertices[index_in_heap * 2 + 1] = Vertex(left)
            vertices[index_in_heap * 2 + 2] = Vertex(right)

small_parsimony(vertices, word_length)
# for element in vertices:
#     element.print_info()
reconstruct(vertices, word_length)
# for element in vertices:
#     element.print_info()


with open("out.txt", 'w') as ouf:
    ouf.write(str(vertices[0].cost) + '\n')
    for index, element in enumerate(vertices):
        if 2 * index + 1 < len(vertices):
            ouf.write(element.resulting_string + '->' + vertices[2 * index + 1].resulting_string + ':' +
                      hamm(element.resulting_string, vertices[2 * index + 1].resulting_string) + '\n')
            ouf.write(vertices[2 * index + 1].resulting_string + '->' + element.resulting_string + ':' +
                      hamm(element.resulting_string, vertices[2 * index + 1].resulting_string) + '\n')

            ouf.write(element.resulting_string + '->' + vertices[2 * index + 2].resulting_string + ':' +
                      hamm(element.resulting_string, vertices[2 * index + 2].resulting_string) + '\n')
            ouf.write(vertices[2 * index + 2].resulting_string + '->' + element.resulting_string + ':' +
                      hamm(element.resulting_string, vertices[2 * index + 2].resulting_string) + '\n')
