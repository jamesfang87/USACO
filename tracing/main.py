fin, fout = open('tracing.in', 'r'), open('tracing.out', 'w')

first_line = fin.readline().strip('\n').split(' ')
num_cows = int(first_line[0])
num_infections = int(first_line[1])

end_status = fin.readline().strip('\n')
infections = end_status.count('1') - 1

infections_history = []
infections_history2 = []
for i in range(num_infections):
    line = fin.readline().strip('\n').split(' ')
    temp = [int(line[1]), int(line[2]), int(line[0])]
    temp2 = [int(line[0]), int(line[1]), int(line[2])]
    infections_history2.append(tuple(temp2))
    infections_history.append(tuple(temp))
    infections_history.sort()

possible_patient_zeros = num_cows
possible_k_value = [1000000000, 0]

for cur_cow in range(1, num_cows + 1):
    infected = []
    for infection in infections_history:
        if infection[0] == cur_cow:
            infected.append((infection[2], infection[1]))
        else:
            infected.sort()
            temp_status = [0 for i in range(num_cows)]
            temp_status[cur_cow - 1] = 1
            for infection1 in infected:
                temp_status[infection1[1] - 1] = 1

            print(temp_status)

            for infection2 in infected:
                last_time = 0
                if end_status[infection2[1] - 1] == 0:
                    possible_k = infection2[1] - last_time
                    if possible_k > possible_k_value[1]:
                        possible_k_value[1] = possible_k
                    if possible_k < possible_k_value[0]:
                        possible_k_value[0] = possible_k

# print(infections_history)
print(possible_patient_zeros)
print(possible_k_value)
