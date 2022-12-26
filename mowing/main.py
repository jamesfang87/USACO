fin, fout = open('mowing.in', 'r'), open('mowing.out', 'w')
from pprint import pprint
nSteps = int(fin.readline())
steps = []
field = [[0 for i in range(2001)] for j in range(2001)]
coords = [1000, 1000]
t = 0
ans = 99999999999999999999999999


def movement(step):
    global t, ans, coords
    if step[0] == 'N':
        for i in range(1, int(step[1]) + 1):
            t += 1
            coords[1] -= 1
            if field[coords[1]][coords[0]] != 0:
                t_last = field[coords[1]][coords[0]]
                if t - t_last <= ans:
                    ans = t - t_last
            field[coords[1]][coords[0]] = t

    elif step[0] == 'S':
        for i in range(1, int(step[1]) + 1):
            t += 1
            coords[1] += 1
            if field[coords[1]][coords[0]] != 0:
                t_last = field[coords[1]][coords[0]]
                if t - t_last <= ans:
                    ans = t - t_last
            field[coords[1]][coords[0]] = t

    elif step[0] == 'E':
        for i in range(1, int(step[1]) + 1):
            t += 1
            coords[0] += 1
            if field[coords[1]][coords[0] + 1] != 0:
                t_last = field[coords[1]][coords[0]]
                if t - t_last <= ans:
                    ans = t - t_last
            field[coords[1]][coords[0]] = t

    elif step[0] == 'W':
        for i in range(1, int(step[1]) + 1):
            t += 1
            coords[0] -= 1
            if field[coords[1]][coords[0] - 1] != 0:
                t_last = field[coords[1]][coords[0]]
                if t - t_last <= ans:
                    ans = t - t_last
            field[coords[1]][coords[0]] = t


for i in range(nSteps):
    steps.append(list(fin.readline().strip('\n').split(' ')))
    movement(steps[i])


"""
array = [[0 for i in range(10)] for j in range(10)]
array[6][6] = 1
array[6 - 1][6] = 1
pprint(array)
"""
fout.write(f'{ans}\n')