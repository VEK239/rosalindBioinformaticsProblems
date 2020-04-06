def number_of_breakpoints(text):
    lst = list(map(int, text.split()))
    breakpoints = 0
    if lst[0] != 1:
        breakpoints += 1
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            breakpoints += 1
    return breakpoints


with open("rosalind_ba6b.txt") as inf:
    line = inf.readline().strip()
    print(number_of_breakpoints(line.strip('()')))
