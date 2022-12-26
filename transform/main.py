"""
ID: james.f3
LANG: PYTHON3
TASK: transform
"""
from pprint import pprint
import sys
fin, fout = open('transform.in', 'r'), open('transform.out', 'w')

Nsides = int(fin.readline().strip())
rect = []
newRect = []

for i in range(Nsides):
    rect.append(list(fin.readline().strip('\n')))

for i in range(Nsides):
    newRect.append(list(fin.readline().strip('\n')))


def turn(rect):
    return [list(x) for x in zip(*reversed(rect))]


def reflection():
    return [list(reversed(x)) for x in rect]


if turn(rect) == newRect:
    fout.write(f'1\n')
    sys.exit()

elif turn(turn(rect)) == newRect:
    fout.write(f'2\n')
    sys.exit()

elif turn(turn(turn(rect))) == newRect:
    fout.write(f'3\n')
    sys.exit()

elif reflection() == newRect:
    fout.write(f'4\n')
    sys.exit()

elif turn(reflection()) == newRect or turn(turn(reflection())) == newRect or turn(turn(turn(reflection()))) == newRect:
    fout.write(f'5\n')
    sys.exit()

elif rect == newRect:
    fout.write(f'6\n')
    sys.exit()

else:
    fout.write(f'7\n')
    sys.exit()
