fin, fout = open('hoofball.in', 'r'), open('hoofball.out', 'w')

nCows = int(fin.readline())
positions = list(fin.readline().strip('\n').split(' '))
num = [0 for i in range(nCows)]
lastNearest = None
last = [[] for j in range(nCows)]
print(last)

for i in range(nCows):
    positions[i] = int(positions[i])

positions.sort()
print(positions)
pair = 0


def nearest(lst, index):
    global lastNearest, pair
    if index == 0:
        lastNearest = 1
        #last[index].append(lastNearest)
        return lastNearest

    elif index == nCows - 1:
        lastNearest = nCows - 2
        #last[index].append(lastNearest)
        return lastNearest

    else:
        left = abs(lst[index] - lst[index - 1])
        right = abs(lst[index] - lst[index + 1])

        if left < right:
            lastNearest = index - 1
            #last[index].append(lastNearest)
            return lastNearest
        elif right < left:
            lastNearest = index + 1
            #last[index].append(lastNearest)
            return lastNearest
        elif left == right:
            lastNearest = index - 1
            #last[index].append(lastNearest)
            return lastNearest




for i in range(nCows):
    ind = nearest(positions, i)
    num[ind] += 1
    last[ind].append(i)

for i in range(nCows - 1):
    if len(last[i]) != 1 or len(last[i+1]) != 1:
        pass
    elif last[i][0] == i + 1 and last[i + 1][0] == i:
        pair += 1


print(num)
print(pair)
print(last)
fout.write(f'{num.count(0) + pair}')
