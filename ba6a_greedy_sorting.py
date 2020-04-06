def reverse(lst):
    lst = [-el for el in lst]
    return lst[::-1]


def print_perm(lst):
    st = '('
    for el in lst:
        st += ('+' + str(el) if el > 0 else str(el)) + ' '
    st = st[:-1]
    st += ')'
    ouf.write(st + '\n')

def greedy_sorting(permutation):
    for i in range(1, len(permutation) + 1):
        if i in permutation:
            j = permutation.index(i)
        else:
            j = permutation.index(-i)
        if j != i - 1 or permutation[j] != i:
            permutation = permutation[:i - 1] + reverse(permutation[i - 1: j + 1]) + permutation[j + 1:]
            print_perm(permutation)
            print(permutation[i - 1])
            if permutation[i - 1] < 0:
                permutation[i - 1] = i
                print_perm(permutation)


with open("rosalind_ba6a (3).txt") as inf:
    line = inf.readline().strip()
    permutation = list(map(int, line.strip('()').split()))
with open("out.txt", 'w') as ouf:
    greedy_sorting(permutation)


