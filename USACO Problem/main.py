# hello my name is bessie and this is my essay
N = int(input('N'))
K = int(input('K'))
essay = input('Essay: ')

words = essay.split(' ')
print(len(words))

print(words)


txt = ''

for i in range(len(words)):
    if len(words[i]) + len(txt) - txt.count(' ') <= K:
        txt = txt + (words[i]) + ' '
    else:
        print(txt)
        txt = f'{words[i]} '
print(txt)
