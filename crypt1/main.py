"""
ID: james.f3
LANG: PYTHON3
TASK: crypt1
"""

fin = open('crypt1.in')

line = fin.readlines()

numbers = list(map(int, line[1].split(' ')))

num = int(line[0][0])
#print(numbers)


def works(int1, int2, int3, int4, int5):
    top = int(f'{int1}{int2}{int3}')

    partial_sum1 = str(int5 * top)

    #print(partial_sum1)
    partial_sum2 = str(int4 * top)
    #print(partial_sum2)
    if len(partial_sum1) > 3 or len(partial_sum2) > 3:
        return False
    for i in range(3):
        #print(partial_sum1[i])
        if int(partial_sum1[i]) not in numbers:
            return False
    for i in range(3):
        #print(partial_sum2[i])
        if int(partial_sum2[i]) not in numbers:
            return False

    result = str(top * int(f'{int4}{int5}'))
    #print(result)
    for i in range(len(result)):
        if int(result[i]) not in numbers:
            return False

    return True


#print(works(3, 2, 8, 8, 8))
"""
3 2 8 8 8
4 2 3 8 2
4 3 6 8 8
"""
count = 0
for a in numbers:
    #print(a)
    for b in numbers:
        #print(b)
        for c in numbers:
            #print(c)
            for d in numbers:
                #print(d)
                for e in numbers:
                    pass
                    #print(e)
                    if works(a, b, c, d, e):
                        count += 1
                        #print(a, b, c, d, e)

fout = open('crypt1.out', 'w')
fout.write(f'{count}\n')
