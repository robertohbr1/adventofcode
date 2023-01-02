cal = open('input.txt', 'r', encoding='utf-8').read().split('\n')

v = ['', '', '', '', '', '', '', '', '', '']
for txt in cal:
    txt = txt[1::4]
    if txt[0] == '1':
        break
    for i, c in enumerate(txt):
        v[i + 1] = (c + v[i + 1]).strip()
    # print(txt)

v2 = v.copy()
# print(v)

for txt in cal:
    if txt[:4] == 'move':
        _, a, _, b, _, c = txt.split()
        a, b, c = int(a), int(b), int(c)
        # print(a, b, c)

        # print(a[0], v[int(a[1])], v[int(a[2])])
        for x in range(a):
            v[c] += v[b][-1]
            v[b] = v[b][0:-1]
        # print(v[int(a[1])], v[int(a[2])])

        # print(a[0], v2[int(a[1])], v2[int(a[2])])
        v2[c] += v2[b][a * -1:]
        v2[b] = v2[b][0:a * -1]
        # print(v2[int(a[1])], v2[int(a[2])])


print(v, v2)
v.remove('')
print('1', ''.join(s[-1] for s in v))

v2.remove('')
print('2', ''.join(s[-1] for s in v2))
