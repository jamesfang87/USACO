fin, fout = open('pails.in', 'r'), open('pails.out', 'w')

sizes = fin.readline().split(' ')
greatest = 0
a = int(sizes[2])//int(sizes[0])
b = int(sizes[2])//int(sizes[1])

for x in range(a+1):
    if x * int(sizes[0]) < int(sizes[2]):
        for y in range(b+1):
            if x*int(sizes[0]) + y*int(sizes[1]) <= int(sizes[2]):
                if x*int(sizes[0]) + y*int(sizes[1]) > greatest:
                    greatest = x*int(sizes[0]) + y*int(sizes[1])


fout.write(f'{greatest}\n')
