fin, fout = open('censor.in', 'r'), open('censor.out', 'w')
s, t = fin.readline().strip(), fin.readline().strip()
text = ''


for i in range(len(s)):
    text += s[i]
    if len(text) >= len(t) and text[len(text) - len(t):] == t:
        text = text[:len(text) - len(t)]

fout.write(text)
