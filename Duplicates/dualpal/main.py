"""
NAME: james.f3
LANG: PYTHON3
TASK: dualpal
"""


fin = open('dualpal.in', 'r')
line = list(map(int, fin.readline().strip('\n').split(' ')))


def convert(base, number):
    answer = 0
    if number == 0:
        return answer
    elif number < base:
        answer = number % base
        return answer
    else:
        answer = ''
        while number // base != 0:
            answer += str(number % base)
            number = number // base
        answer += str(number % base)
        return answer[::-1]


def count(number):
    counter = 0
    for j in range(2, 10 + 1):
        temp_str = str(convert(j, number))
        #print(f'{number} in base {j} is {temp_str}, opposite is {temp_str[::-1]}')
        if temp_str == temp_str[::-1]:
            counter += 1
        if counter >= 2:
            fout.write(f'{number}\n')
            #print(f'{number} returned as true')
            #print(counter)
            return True
    return False


with open('dualpal.out', 'w') as fout:
    number_printed = 0
    for i in range(line[1] + 1, 10000000):
        #print(f'number is: {i}')
        #count(i)
        if count(i):
            #
            #print(i)
            number_printed += 1
                    #print(number_printed)
            if number_printed == line[0]:
                break

