"""
NAME: james.f3
LANG: PYTHON3
TASK: skidesign
"""

with open('skidesign.in', 'r') as fin:
    num_hills = int(fin.readline().strip('\n'))
    hills = []
    for i in range(num_hills):
        hills.append(int(fin.readline().strip('\n')))
hills.sort()

print(hills)

least = 10000000000000000
for i in range(17, max(hills) + 1):
    cost = 0
    low = i - 17
    high = i
    print(low, high)
    for hill in hills:
        if hill > high:
            cost += (hill - i) ** 2
        if hill < low:
            cost += (low - hill) ** 2
    if cost < least:
        least = cost
fout = open('skidesign.out', 'w')
fout.write(f'{least}\n')
