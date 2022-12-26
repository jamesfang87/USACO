fin, fout = open('whereami.in', 'r'), open('whereami.out', 'w')


nFarm = int(fin.readline())
colors = fin.readline().strip('\n')


def works(length):
    sequences = set()
    for j in range(0, nFarm+1):
        if colors[j:j+length] in sequences:
            return False
        else:
            sequences.add(colors[j:j + length])

    return True


for i in range(1, nFarm + 1):
    if works(i):
        fout.write(f'{i}')
        break



