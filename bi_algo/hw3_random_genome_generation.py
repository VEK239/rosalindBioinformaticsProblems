import random


def generate_random_nucleo_seq(length):
    nucleo = ['A', 'C', 'T', 'G']
    genome = ''.join(random.choice(nucleo) for _ in range(length))
    print(genome)
    return genome


if __name__ == "__main__":
    for l in [100, 1000, 100000]:
        with open('random_genome_{}.txt'.format(str(l)), 'w') as ouf:
            ouf.write(generate_random_nucleo_seq(l))
