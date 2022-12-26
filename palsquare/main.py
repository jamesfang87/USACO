"""
NAME: james.f3
LANG: PYTHON3
TASK: palsquare
"""



fin = open('palsquare.in', 'r')


base = int(fin.readline())

variables = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
}


def convert(base, number):
    if number < base:
        return variables[number]
    else:
        answer = ''
        while number >= base:
            answer += variables[number % base]
            number //= base
        answer += variables[number % base]
        return answer[::-1]

#print(convert(5, 10))

with open('palsquare.out', 'w') as fout:
    for i in range(1, 301):
        temp_str = convert(base, i * i)
        if temp_str == temp_str[::-1]:
            fout.write(f'{convert(base, i)} {temp_str}\n')
