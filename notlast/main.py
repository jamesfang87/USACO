import sys

fin, fout = open('notlast.in', 'r'), open('notlast.out', 'w')

nEntries = int(fin.readline())
cows = {
    'Bessie': 0,
    'Elsie': 0,
    'Daisy': 0,
    'Gertie': 0,
    'Annabelle': 0,
    'Maggie': 0,
    'Henrietta': 0
}
values = list()
valuesSet = set()

for i in range(nEntries):
    temp = fin.readline().strip('\n').split(' ')
    cows[temp[0]] += int(temp[1])



for value in cows.values():
    values.append(value)
    valuesSet.add(value)


valuesSet.remove(min(valuesSet))
count = 0
name = 'asdf'

for item in cows.items():

    if valuesSet:
        if item[1] == min(valuesSet):
            count += 1
            name = item[0]
    else:
        fout.write('Tie\n')
        sys.exit()

if count > 1:
    fout.write('Tie\n')
else:
    fout.write(f'{name}')


