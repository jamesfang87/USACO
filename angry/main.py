fin, fout = open('angry.in', 'r'), open('angry.out', 'w')

input = []
for line in fin.readlines():
    input.append(int(line.strip('\n')))
input.sort()
input = list(set(input))

positions = [-1 for i in range(max(input) + 1)]
originalPos = [-1 for i in range(max(input) + 1)]
values = []


def fuck_python():
    global originalPos
    for i in range(0, max(input) + 1):
        if i in input:
            originalPos[i] = i


for i in range(0, max(input) + 1):
    if i in input:
        positions[i] = i
print(positions)
fuck_python()

for i in range(len(input)):
    positions[input[i]] = -2
    if input[i] - 1 > 0 and positions[input[i] - 1] >= 0:
        positions[input[i] - 1] = -3
        temp = []
        if input[i] - 2 > 0 and positions[input[i] - 2] >= 0:
            temp.append(input[i] - 2)
            positions[input[i] - 2] = -3

        if input[i] - 3 > 0 and positions[input[i] - 3] >= 0:
            temp.append(input[i] - 3)
            positions[input[i] - 3] = -3
        if temp:
            while temp:
                h = temp[0]
                if (h - 1 >= 0 and positions[h - 1] <= -1) and \
                        (h - 2 >= 0 and positions[h - 2] <= -1) and \
                        (h - 3 >= 0 and positions[h - 3] <= -1):
                    temp.remove(temp[0])
                else:
                    if h - 3 <= len(positions) - 1:
                        temp.append(h - 3)
                        positions[h - 3] = -3
                        positions[h - 2] = -3
                        positions[h - 1] = -3
                        temp.remove(temp[0])
                    elif h - 2 <= len(positions) - 1:
                        temp.remove(temp[0])
                        temp.append(h - 2)
                        positions[h - 2] = -3
                        temp.append(h - 1)

                    elif h - 1 <= len(positions) - 1:
                        temp.remove(temp[0])
                        temp.append(h - 1)
                        positions[h - 1] = -3

    if input[i] + 1 < len(positions) and positions[input[i] + 1] >= 0:
        positions[input[i] + 1] = -3
        temp = []
        if input[i] + 2 < len(positions) and positions[input[i] + 2] >= 0:
            temp.append(input[i] + 2)
            positions[input[i] + 2] = -3
        if input[i] + 3 < len(positions) and positions[input[i] + 3] >= 0:
            temp.append(input[i] + 3)
            positions[input[i] + 3] = -3

        if temp:
            h = temp[0]
            count = 0
            while temp:
                if (h + 1 <= len(positions) - 1 and positions[h + 1] <= -1) and \
                        (h + 2 <= len(positions) - 1 and positions[h + 2] <= -1) and \
                        (h + 3 <= len(positions) - 1 and positions[h + 3] <= -1):
                    pass
                else:
                    if h + 3 <= len(positions) - 1:
                        temp.remove(temp[0])
                        temp.append(h + 3)
                        if positions[h + 3] >= 0:
                            positions[h + 3] = -3
                        if positions[h + 2] >= 0:
                            positions[h + 2] = -3
                        if positions[h + 1] >= 0:
                            positions[h + 1] = -3

                    elif h + 2 <= len(positions) - 1:
                        temp.remove(temp[0])
                        temp.append(h + 2)
                        positions[h + 2] = -3
                        positions[h + 1] = -3

                    elif h + 1 <= len(positions) - 1:
                        temp.remove(temp[0])
                        temp.append(h + 1)
                        positions[h + 1] = -3

    print(f'{positions}\n')
    temp1 = 0
    for f in range(len(positions)):
        if positions[f] == -3 or positions[f] == -2:
            temp1 += 1
    values.append(temp1)

    positions = originalPos
    fuck_python()

fout.write(f'{max(values)}\n')
