fin, fout = open('lifeguards.in', 'r'), open('lifeguards.out', 'w')


N = int(fin.readline())
coveredTimes = [0] * 1000
start = []
end = []


for i in range(N):
    info = fin.readline().strip('\n').split(' ')
    start.append(int(info[0]))
    end.append(int(info[1]))

numCover = [0] * 1000
total_covered = 0

for i in range(N):
    for t in range(start[i], end[i]):
        if numCover[t] == 0:
            total_covered += 1
        numCover[t] += 1

covered = total_covered

ans = 0

for i in range(N):
    for j in range(start[i], end[i]):
        if numCover[j] - 1 <= 0:
            covered -= 1

    ans = max(ans, covered)
    covered = total_covered


fout.write(f'{ans}\n')