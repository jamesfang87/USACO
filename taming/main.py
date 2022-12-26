import sys

fin, fout = open('taming.in', 'r'), open('taming.out', 'w')

nDays = int(fin.readline())
days = fin.readline().strip('\n').split(' ')
days[0] = 0

for i in range(len(days)):
    days[i] = int(days[i])

original = days[:]

for i in range(0, nDays - 1):
    if days[i] == -1 and days[i + 1] == 1:
        days[i] = 0

    if days[i] > 0 and days[i + 1] > 0:
        if days[i] == days[i + 1]:
            fout.write(f'-1\n')
            sys.exit()

counter = 0
index = 0
while index < nDays:
    if days[index] == -1:
        days[index] = counter

    if days[index] == 0:
        counter = 0

    if days[index] > 0 and days[index] != counter:
        for j in range(1, int(days[index]) + 1):
            days[index - j] = int(days[index]) - j

    index += 1

maxAmount = days.count(0)
minAmount = 0

for i in range(1, nDays):
    if days[i] == 1 and days[i - 1] == 0:
        pass
    else:
        if original[i - 1] != 0:
            days[i - 1] = days[i - 2] + 1

if original[-1] != 0:
    days[-1] = days[-2] + 1

fout.write(f'{days.count(0)} {maxAmount}\n')
