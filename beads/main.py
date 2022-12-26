"""
ID: james.f3
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

num_beads = int(fin.readline())
necklace = fin.readline()
necklace += necklace
maximum = 0


def all_same(string):
    for a in range(1, len(string)):
        if string[a] != string[a - 1]:
            return False
    return True


if maximum > num_beads:
    fout.write(f'{num_beads}')
else:
    for j in range(num_beads):
        color_changes = 0
        cur_color = necklace[j]
        string = necklace[j]
        for i in range(j + 1, len(necklace)):
            string += necklace[i]

            if cur_color != 'w' and string[-1] != 'w':
                if necklace[i] != cur_color:
                    color_changes += 1

            if necklace[i] != 'w':
                cur_color = necklace[i]

            if color_changes >= 2:
                if len(string) - 1 > maximum:
                    maximum = len(string) - 1
                print(string[:len(string) - 1])
                string = ''
                break

    fout.write(f'{maximum}\n')