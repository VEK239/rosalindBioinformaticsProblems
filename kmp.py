def prefixFunction(s):
    prefix = [0 for i in range(len(s))]
    curPrefixValue = 0
    for i in range(1, len(s)):
        curPrefixValue = prefix[i - 1]
        while curPrefixValue > 0 and s[i] != s[curPrefixValue]:
            curPrefixValue = prefix[curPrefixValue - 1]
        if s[i] == s[curPrefixValue]:
            curPrefixValue += 1
        prefix[i] = curPrefixValue
    return prefix


with open("rosalind_kmp.txt") as inf:
    line = inf.readline()
    while line:
        if line[0] == '>':
            restart = True
        elif restart:
            dna = line.strip()
            restart = False
        else:
            dna += line.strip()
        line = inf.readline()

result = prefixFunction(dna)
st = ''
for num in result:
    st += str(num) + ' '
with open("kmp.txt", 'w') as ouf:
    ouf.write(st)
