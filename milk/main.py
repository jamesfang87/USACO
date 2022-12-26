"""
ID: james.f3
LANG: PYTHON3
TASK: milk
"""


fin, fout = open('milk.in', 'r'), open('milk.out', 'w')

info = list(fin.readline().strip('\n').split(' '))
farmers = list()


for i in range(int(info[1])):
    farmers.append(list(fin.readline().strip('\n').split(' ')))
    farmers[i][0] = int(farmers[i][0])
    farmers[i][1] = int(farmers[i][1])

farmers.sort()
total = 0
amount = 0

print(farmers)

for i in range(len(farmers)):
    total += int(farmers[i][0]) * int(farmers[i][1])
    print(f'total: {total}')
    amount += int(farmers[i][1])
    print(f'amount: {amount}')
    if amount > int(info[0]):
        diff = int(info[0]) - amount
        total += int(farmers[i][0]) * diff
        print(f'total: {total}')
        amount -= (int(farmers[i][1]) + diff)
        print(f'amount: {amount}')
        break


fout.write(f'{total}\n')
