fin, fout = open('cowqueue.in', 'r'), open('cowqueue.out', 'w')


nCows = int(fin.readline())
times = []

for i in range(nCows):
    times.append(list(fin.readline().strip('\n').split(' ')))
    times[i][0] = int(times[i][0])
    times[i][1] = int(times[i][1])

times.sort()



for i in range(nCows-1):
    timeNext = times[i][0] + times[i][1]
    if timeNext > times[i+1][0]:
        times[i+1][0] = timeNext


fout.write(f'{times[-1][0]+times[0-1][1]}')