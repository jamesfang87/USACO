"""
ID: james.f3
LANG: PYTHON3
TASK: transform
"""


import sys

fin = open('transform.in', 'r')

length = int(fin.readline())
cube_initial = []
cube_after = []

for i in range(length):
    line = fin.readline().strip('\n')

    temp = []
    for j in range(length):
        temp.append(line[j])
    cube_initial.append(temp)

for i in range(length):
    line = fin.readline().strip('\n')

    temp = []
    for j in range(length):
        temp.append(line[j])
    cube_after.append(temp)


def rotate(square):
    new = [[] for b in range(length)]
    for col in range(length):
        for a in range(length):
            new[a].insert(0, square[col][a])

    return new

def reflection(square):
    new = [[] for b in range(length)]
    for row in range(length):
        for item in range(1, length + 1):
            new[row].append(square[row][-1 * item])
    return new

#print(reflection(cube_initial))
with open('transform.out', 'w') as fout:
    if rotate(cube_initial) == cube_after:
        fout.write('1\n')
    elif rotate(rotate(cube_initial)) == cube_after:
        fout.write('2\n')
    elif rotate(rotate(rotate(cube_initial))) == cube_after:
        fout.write('3\n')
    elif reflection(cube_initial) == cube_after:
        fout.write('4\n')
    elif reflection(rotate(cube_initial)) == cube_after:
        fout.write('5\n')
    elif reflection(rotate(rotate(cube_initial))) == cube_after:
        fout.write('5\n')
    elif reflection(rotate(rotate(rotate(cube_initial)))) == cube_after:
        fout.write('5\n')
    elif cube_initial == cube_after:
        fout.write('6\n')
    else:
        fout.write('7\n')