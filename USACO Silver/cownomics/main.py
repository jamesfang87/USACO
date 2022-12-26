from itertools import combinations


fin = open("cownomics.in", "r")

line = fin.readline().strip('\n').split(' ')
num_cows, num_positions = line[0], line[1]
genomes = [[], []]

indices = [i for i in range(int(num_positions))]
combinations = list(combinations(indices, 3))

for i in range(int(num_cows)):
    genomes[0].append(fin.readline().strip('\n'))

for i in range(int(num_cows)):
    genomes[1].append(fin.readline().strip('\n'))


num_possible = len(combinations)

for combination in combinations:
    spotty_genomes = set()
    plain_genomes = set()
    for i in range(int(num_cows)):
        spotty_genomes.add((genomes[0][i][combination[0]], genomes[0][i][combination[1]], genomes[0][i][combination[2]]))
        plain_genomes.add((genomes[1][i][combination[0]], genomes[1][i][combination[1]], genomes[1][i][combination[2]]))

    for genome in spotty_genomes:
        if genome in plain_genomes:
            num_possible -= 1
            break


fout = open("cownomics.out", 'w')
fout.write(f'{num_possible}\n')
