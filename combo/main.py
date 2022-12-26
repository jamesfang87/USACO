"""
ID: james.f3
LANG: PYTHON3
TASK: combo
"""
import time
import sys

st = time.time()

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')

num_dials = int(fin.readline().strip('\n'))
john_code = list(map(int, fin.readline().strip('\n').split(' ')))
master_code = list(map(int, fin.readline().strip('\n').split(' ')))
possible_dials1 = [{john_code[0]}, {john_code[1]}, {john_code[2]}]
possible_dials2 = [{master_code[0]}, {master_code[1]}, {master_code[2]}]


if num_dials == 1:
    fout.write('1\n')
    sys.exit()



helper_list = [i for i in range(1, num_dials + 1)]
#print(helper_list)


def generate(array, code):
    for j in range(3):
        index_of_code = code[j] - 1
        array[j].add(helper_list[index_of_code - 1])
        array[j].add(helper_list[index_of_code - 2])
        if index_of_code + 1 >= num_dials:
            array[j].add(helper_list[0])
            array[j].add(helper_list[1])
        elif index_of_code + 2 >= num_dials:
            array[j].add(helper_list[index_of_code + 1])
            array[j].add(helper_list[0])
        else:
            array[j].add(helper_list[index_of_code + 1])
            array[j].add(helper_list[index_of_code + 2])


generate(possible_dials1, john_code)
generate(possible_dials2, master_code)
#print(possible_dials1, possible_dials2)



def check(combination):
    for index in range(3):
        code_index = helper_list.index(john_code[index])
        combination_index = helper_list.index(combination[index])
        if abs(code_index - combination_index) > 2:
            return False
    return True


def check_master(combination):
    for index in range(3):
        master_index = helper_list.index(master_code[index])
        combination_index = helper_list.index(combination[index])
        if abs(master_index - combination_index) > 2:
            return False
    return True


already_counted = set()
for one in possible_dials1[0]:
    for two in possible_dials1[1]:
        for three in possible_dials1[2]:
            temp_comb = (one, two, three)
            already_counted.add(temp_comb)


for one in possible_dials2[0]:
    for two in possible_dials2[1]:
        for three in possible_dials2[2]:
            temp_comb = (one, two, three)
            already_counted.add(temp_comb)



end = time.time()

fout.write(f'{len(already_counted)}\n')
# print(count)
# print(end - st)
