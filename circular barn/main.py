fin, fout = open('cbarn.in', 'r'), open('cbarn.out', 'w')


N = fin.readline()
N2 = int(N)
list = []
new_list = []
answer = N2*N2*100


for i in range(N2):
    list.append(int(fin.readline()))


for i in range(N2):
    score = 0
    for j in range(0, N2):
        score += j * list[(i+j)%N2]




    if score < answer:
        answer = score


fout.write(f'{answer}')