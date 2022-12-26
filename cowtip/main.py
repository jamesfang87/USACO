fin, fout = open('cowtip.in', 'r'), open('cowtip.out', 'w')


N = int(fin.readline())

grid = []

for i in range(N):
    x = fin.readline().strip('\n')
    x = [int(x[0]), int(x[1]), int(x[2])]
    grid.append(x)


print(grid)