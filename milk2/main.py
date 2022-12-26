"""
ID: james.f3
LANG: PYTHON3
TASK: milk2
"""


fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
times = []
merged_times = []


N = int(fin.readline().strip())

for i in range(N):
    times.append(tuple(map(int, fin.readline().strip().split(' '))))

times.sort()
print(times)
merged = times[0]
for i in range(1, N):
    if merged[1] >= times[i][0]:
        merged = (merged[0], max(times[i][1], merged[1]))
    else:
        merged_times.append(merged)
        merged = times[i]
merged_times.append(merged)


longestb = 0
longest = 0
for i in range(len(merged_times)):
    ans = merged_times[i][1] - merged_times[i][0]
    if ans >= longest:
        longest = ans


for i in range(1, len(merged_times)):
    ans = merged_times[i][0] - merged_times[i-1][1]
    if ans >= longestb:
        longestb = ans


print(merged_times)
fout.write(f'{longest} {longestb}\n')
