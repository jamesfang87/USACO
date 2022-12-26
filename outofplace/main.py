fin, fout = open('outofplace.in', 'r'), open('outofplace.out', 'w')

numCows = int(fin.readline())
heights = []
Bessie = [0, 0]

for i in range(numCows):
    height = fin.readline().strip('\n')
    heights.append(int(height))

for i in range(numCows):
    copy = heights[:]
    temp1 = heights[:]
    temp1.pop(i)
    copy.pop(i)
    copy.sort()
    if copy == temp1:
        Bessie = [i, heights[i]]


original = heights[:]

heights.sort()
neededIndex = heights.index(Bessie[1])

maxChanges = abs(neededIndex - Bessie[0])
print(Bessie[0])
print(neededIndex)

x = original[min(Bessie[0], neededIndex):max(Bessie[0], neededIndex)+1]
print(x)

if len(x) == len(set(x)):
    fout.write(f'{maxChanges}\n')
else:
    diff = len(x) - len(set(x))
    fout.write(f'{maxChanges-(diff)}\n')
