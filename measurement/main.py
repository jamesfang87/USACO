fin, fout = open('measurement.in', 'r'), open('measurement.out', 'w')


num = int(fin.readline())
info = []

for i in range(num):
    info.append(list(fin.readline().strip('\n').split(' ')))
    info[i][0], info[i][-1] = int(info[i][0]), int(info[i][-1])
    info.sort()

cows = [7, 7, 7]
prevHigh = []
currHigh = []
count = 0


def findMax(cows):
    global currHigh, prevHigh
    highest = max(cows)
    indices = [index for index, value in enumerate(cows) if value == highest]
    prevHigh = currHigh
    currHigh = indices


for i in range(len(info)):
    if info[i][1] == 'Bessie':
        cows[0] += info[i][2]
        findMax(cows)
        if currHigh != prevHigh:
            count += 1
    elif info[i][1] == 'Elsie':
        cows[1] += info[i][2]
        findMax(cows)
        if currHigh != prevHigh:
            count += 1
    elif info[i][1] == 'Mildred':
        cows[2] += info[i][2]
        findMax(cows)
        if currHigh != prevHigh:
            count += 1


fout.write(f'{count}\n')