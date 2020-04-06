dnaLines = []
with open("rosalind_cons.txt") as inf:
    line = inf.readline()
    while line:
        if line[0] == '>':
            restart = True
        elif restart:
            print(line)
            dnaLines.append(line.strip())
            restart = False
        else:
            dnaLines[len(dnaLines) - 1] += line.strip()
        line = inf.readline()
nucleo = {'A': [0 for i in range(len(dnaLines[0]))], 'C': [0 for i in range(len(dnaLines[0]))],
          'G': [0 for i in range(len(dnaLines[0]))], 'T': [0 for i in range(len(dnaLines[0]))]}
for j in range(len(dnaLines)):
    for i in range(len(dnaLines[j])):
        nucleo[dnaLines[j][i]][i] += 1
st = ""
for i in range(len(dnaLines[0])):
    st += str(max([nucleo['A'][i], 'A'], [nucleo['C'][i], 'C'], [nucleo['G'][i], 'G'], [nucleo['T'][i], 'T'])[1])
for letter in nucleo:
    st += '\n' + letter + ": "
    for number in nucleo[letter]:
        st += str(number) + ' '
with open("cons.txt", 'w') as ouf:
    ouf.write(st)
