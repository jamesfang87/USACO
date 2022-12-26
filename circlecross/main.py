fin = open('circlecross.in', 'r')



temp = fin.readline().strip('\n')
string = list()
for i in range(len(temp)):
    string.append(temp[i])

print(string)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
crosses = 0
continuing = True
prev_letter = None
new_letter = False
exit_entrance = [[] for i in range(26)]

for i in range(26):
    for j in range(2):
        exit_entrance[i].append(string.index(alphabet[i]))
        string[exit_entrance[i][j]] = ' '

print(exit_entrance)


for letter in exit_entrance:
    for other_letter in exit_entrance:
        if letter[1] - letter[0] == 1 or other_letter[1] - other_letter[0] == 1:
            pass
        elif letter[0] < other_letter[0] < letter[1] and other_letter[0] < letter[1] < other_letter[1]:
            crosses += 1



fout = open('circlecross.out', 'w')
fout.write(f"{crosses}\n")

