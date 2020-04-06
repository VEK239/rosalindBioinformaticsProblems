with open("rosalind_iev.txt") as inf:
    line = list(map(int, inf.readline().split()))

with open("iev.txt", 'w') as ouf:
    ouf.write(str((line[0] + line[1] + line[2]) * 2 + line[3] * 1.5 + line[4]))
