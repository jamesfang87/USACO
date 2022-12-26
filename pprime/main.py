"""
ID: james.f3
LANG: PYTHON3
TASK: pprime
"""

fin, fout = open('pprime.in', 'r'), open('pprime.out', 'w')

info = fin.readline().strip('\n').split(' ')
start = int(info[0])
end = int(info[1])


def prime(i):
    if i % 2 == 0:
        return False

    for j in range(3, int(i/2) + 1, 2):
        if i % j == 0:
            return False
    return True


for i in range(start, end + 1):
    if str(i) == str(i)[::-1]:
        if prime(i):
            fout.write(f'{i}\n')
