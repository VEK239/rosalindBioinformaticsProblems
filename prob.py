import math

with open("rosalind_prob.txt") as inf:
    dna = inf.readline().strip()
    probGC = list(map(float, inf.readline().strip().split()))
st = ''
for i in range(len(probGC)):
    probs = {'A': (1 - probGC[i]) / 2, 'T': (1 - probGC[i]) / 2, 'C': probGC[i] / 2, 'G': probGC[i] / 2}
    result = 0
    for letter in dna:
        result += math.log10(probs[letter])
    st += str(result) + ' '

with open("prob.txt", 'w') as ouf:
    ouf.write(st)
