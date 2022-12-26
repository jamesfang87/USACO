fin, fout = open('cownomics.in', 'r'), open('cownomics.out', 'w')

lst = fin.readline().strip('\n').split(' ')
N = int(lst[0])
M = int(lst[1])
plain = []
spotted = []
count = 0


for i in range(N):
    spotted.append(fin.readline().strip('\n'))

for i in range(N):
    plain.append(fin.readline().strip('\n'))


for i in range(M):
    plainGenes = []
    spottedGenes = []
    for j in range(N):
        plainGenes.append(plain[j][i])
        spottedGenes.append(spotted[j][i])
    plainGenes = set(plainGenes)
    spottedGenes = set(spottedGenes)
    if len(plainGenes.intersection(spottedGenes)) == 0:
        count += 1


fout.write(f'{count}\n')





