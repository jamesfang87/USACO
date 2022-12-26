fin, fout = open('paint.in', 'r'), open('paint.out', 'w')


seg1 = fin.readline().strip('\n').split(' ')
seg2 = fin.readline().strip('\n').split(' ')
seg1[0], seg1[1], seg2[0], seg2[1] = int(seg1[0]), int(seg1[1]), int(seg2[0]), int(seg2[1])

total = [seg1[0], seg1[1], seg2[0], seg2[1]]
total1 = [seg1, seg2]
total1.sort()
maximum = max(total)
minimum = min(total)

if total1[0][1] > total1[1][0]:
    fout.write(f'{maximum - minimum}\n')

else:
    fout.write(f'{abs(int(seg1[0]) - int(seg1[1])) + abs(int(seg2[0]) - int(seg2[1]))}')