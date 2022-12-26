from itertools import combinations



num_cows = int(input())
cow_pos = []
stopping_values = []
grass_ate = []

for i in range(num_cows):
    info = input().split(' ')
    cow_pos.append((info[0], int(info[1]), int(info[2])))

comb = combinations(cow_pos, 2)

for i in list(comb):
    if i[0][0] == 'E' and i[1][0] == 'N':
        if i[0][1] > i[1][1] or i[1][2] > i[0][2]:
            pass
        else:
            x_diff = abs(i[0][1] - i[1][1])
            y_diff = abs(i[0][2] - i[1][2])
            if x_diff > y_diff:
                stopping_values.append((x_diff, i[0], i[1]))  # the first value is the one that is stopped and the second is the stopper
            elif y_diff > x_diff:
                stopping_values.append((y_diff, i[1], i[0]))  # the first value is the one that is stopped and the second is the stopper

    elif i[0][0] == 'N' and i[1][0] == 'E':
        if i[1][1] > i[0][1] or i[0][2] > i[1][2]:
            pass
        else:
            x_diff = abs(i[0][1] - i[1][1])
            y_diff = abs(i[0][2] - i[1][2])
            if x_diff > y_diff:
                stopping_values.append((x_diff, i[1], i[0]))  # the first value is the one that is stopped and the second is the stopper
            elif y_diff > x_diff:
                stopping_values.append((y_diff, i[0], i[1]))  # the first value is the one that is stopped and the second is the stopper

stopping_values.sort()
print(stopping_values)
print(cow_pos)
stopped = list()
stopped_at = list()

for i in range(len(stopping_values)):
    if stopping_values[i][2] in stopped and stopping_values[i][1] in stopped:
        pass
    elif stopping_values[i][2] in stopped:
        if stopping_values[i][1][0] == 'E':
            if stopping_values[i][2][2] + stopped_at[stopped.index(stopping_values[i][2])] >= stopping_values[i][1][2]:
                stopped.append(stopping_values[i][1])
                stopped_at.append(stopping_values[i][0])


        elif stopping_values[i][1][0] == 'N':
            if stopping_values[i][2][1] + stopped_at[stopped.index(stopping_values[i][2])] >= stopping_values[i][1][1]:
                stopped.append(stopping_values[i][1])
                stopped_at.append(stopping_values[i][0])

    elif stopping_values[i][1] in stopped:
        pass
    elif stopping_values[i][1] not in stopped and stopping_values[i][2] not in stopped:
        stopped.append(stopping_values[i][1])
        stopped_at.append(stopping_values[i][0])

print(stopped)
print(stopped_at)


for i in range(num_cows):
    if cow_pos[i] in stopped:
        fout.write(f'{stopped_at[stopped.index(cow_pos[i])]}\n')
    else:
        fout.write('Infinity\n')



answer_key = open("answer.in", "r")
my_answer = open("stuck.out", "r")
key = answer_key.readlines()
answer = my_answer.readlines()

if key == answer:
    print("correct")
else:
    print("incorrect")