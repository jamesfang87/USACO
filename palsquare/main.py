"""
ID: james.f3
LANG: PYTHON3
TASK: palsquare
"""

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fin, fout = open('palsquare.in', 'r'), open('palsquare.out', 'w')
base = int(fin.readline())


def convert(num, baseTo):
    ans = ''
    result = num // baseTo
    remainder = num % baseTo
    ans += alphabet[remainder]
    while result != 0:
        num = result
        result = num // baseTo
        remainder = num % baseTo
        ans += alphabet[remainder]
    ans = ans[::-1]
    return ans


for i in range(1, 301):
    number = convert(i, base)
    numSquared = convert(i**2, base)
    if numSquared == numSquared[::-1]:
        fout.write(f'{number} {numSquared}\n')


