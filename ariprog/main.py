"""
NAME: james.f3
LANG: PYTHON3
TASK: ariprog
"""

fin = open('ariprog.in', 'r')

prog_len = int(fin.readline().strip('\n'))
upper_bound = int(fin.readline().strip('\n'))

bisquares = set()

for p in range(upper_bound + 1):
    for q in range(upper_bound + 1):
        bisquares.add(p ** 2 + q ** 2)

#print(bisquares)


# have like 2 for loops, the outer will run for the common difference and the inner will do the starting one. another one inside will check if the next 5 times, the thing works idfk

def check(array):
    global bisquares
    for thing in array:
        if thing not in bisquares:
            return False
    return True


fout = open('ariprog.out', 'w')
printed = False
#print(max(bisquares) // 4 + 3)
for diff in range(1, max(bisquares) // (prog_len - 1) + 1):
    for item in bisquares:
        needed = set()
        for i in range(prog_len):
            needed.add(item + diff * i)
        if check(needed):
            fout.write(f'{item} {diff}\n')
            printed = True

if not printed:
    fout.write('NONE\n')

