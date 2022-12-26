fin, fout = open('backforth.in', 'r'), open('backforth.out', 'w')

barnA = fin.readline().strip('\n').split()
barnB = fin.readline().strip('\n').split()
possibleValues = set()
value = 1000

for i in range(10):
    barnA[i] = int(barnA[i])
    barnB[i] = int(barnB[i])

print(barnA)
print(barnB)


def count(day, amountA, amountB, barnA, barnB):
    if day > 6:
        possibleValues.add(amountA)
        return

    tempA, tempB = amountA, amountB
    if day % 2 == 1:
        for j in range(len(barnA)):
            newA, newB = barnA[:], barnB[:]
            x = newA[j]
            newB.append(x)
            del newA[j]
            amountA -= x
            count(day+1, amountA, amountB+x, newA, newB)
            amountA, amountB = tempA, tempB

    else:
        for j in range(len(barnB)):
            newA, newB = barnA[:], barnB[:]
            x = newB[j]
            newA.append(x)
            del newB[j]
            amountB -= x
            count(day+1, amountA+x, amountB, newA, newB)
            amountA, amountB = tempA, tempB




count(3, 1000, 1000, barnA, barnB)
fout.write(f'{len(possibleValues)}')
print(possibleValues)