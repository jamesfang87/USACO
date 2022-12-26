"""
ID: james.f3
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

num = int(fin.readline())
names = []
acc = []

for i in range(num):
    names.append(fin.readline())
    acc.append(0)

for i in range(len(names)):
    name = fin.readline()
    money_info = fin.readline().split(' ')
    z = names.index(name)

    if int(money_info[0]) == 0:
        acc[z] += int(money_info[0])
    elif int(money_info[1]) == 0:
        acc[z] += int(money_info[0])
    else:
        acc[z] = acc[z] - int(money_info[0]) + (int(money_info[0]) % int(money_info[1]))

    for j in range(int(money_info[1])):
        recipient = fin.readline()
        index = names.index(recipient)
        acc[index] += int(money_info[0]) // int(money_info[1])

# finish printing or smth idk
for i in range(len(names)):
    names[i] = names[i].strip('\n')
for i in range(len(names)):
    fout.write(f'{names[i]} {str(acc[i])}\n')

print()
