"""
ID: james.f3
LANG: PYTHON3
TASK: namenum
"""


with open('namenum.in', 'r') as f:
    numbers = f.readline().strip()
with open('dict.txt', 'r') as f:
    cDict = f.read().strip().split('\n')

keyMap = {2: 'ABC', 5: 'JKL', 8: 'TUV',
          3: 'DEF', 6: 'MNO', 9: 'WXY',
          4: 'GHI', 7: 'PRS'}
bName = []


def keyToBrandName(name, numbers, i):
    if i == len(str(numbers)):
        for dName in cDict:
            if name == dName:
                bName.append(name)
        return

    for k in keyMap[int(numbers[i])]:
        temp = name + k
        for dName in cDict:
            if dName.startswith(temp):
                keyToBrandName(temp, numbers, i + 1)
                break


keyToBrandName("", numbers, 0)
if not bName:
    bName.append('NONE')

with open('namenum.out', 'w') as f:
    for i in range(len(bName)):
        f.write(f'{bName[i]}\n')
