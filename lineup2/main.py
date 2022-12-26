fin = open('lineup.in', 'r')
fout = open('lineup.out', 'w')

order = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']

print(order)

num = int(fin.readline())
needs = []
for i in range(num):
    temp = fin.readline().strip('\n').replace(' must be milked beside ', ' ').split()
    temp.sort()
    print(temp)
    needs.append(temp)

