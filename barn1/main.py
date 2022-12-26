"""
ID: james.f3
LANG: PYTHON3
TASK: barn1
"""



fin = open('barn1.in', 'r')

line = list(map(int, fin.readline().strip('\n').split(' ')))

num_boards = line[0]
stalls = []
for i in range(line[2]):
    stall_number = fin.readline().strip('\n')
    stalls.append(int(stall_number))
stalls.sort()
print(stalls)
# print(len(stalls))
fout = open('barn1.out', 'w')

gaps = []


#length = len(stalls)

#print(len(stalls))

min_covered = len(stalls)
#print(min_covered)

for item in range(len(stalls) - 1):
    gaps.append(stalls[item + 1] - stalls[item] - 1)

gaps.sort()

while len(gaps) > num_boards - 1:
    min_covered += gaps[0]
    gaps.pop(0)

#print(gaps)
#print(min_covered)

fout.write(f'{min_covered}\n')