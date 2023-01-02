from rich import print
from functools import cmp_to_key

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n\n')

x = 0
v = ['', '']


def comp(a, b):
    i = 0
    while len(a) > i and len(b) > i:
        if type(a[i]) == type(b[i]) == int:
            r = b[i] - a[i]
        elif type(b[i]) == int:
            r = comp(a[i], [b[i]])
        elif type(a[i]) == int:
            r = comp([a[i]], b[i])
        else:
            r = comp(a[i], b[i])
        if r != 0:
            return r
        i += 1
    if len(b) > i:
        return 1
    elif len(a) > i:
        return -1
    else:
        return 0


x = 0
soma = 0
for txt in cal:
    txt = txt.split('\n')
    v[0] = eval(txt[0])
    v[1] = eval(txt[1])
    x += 1
    if comp(v[0], v[1]) > 0:
        soma += x
print(soma)  # 6568


cal = open('input.txt', 'r',
           encoding='utf-8').read().strip().replace("\n\n", "\n").split("\n")

li = list(map(eval, cal))
li.append([[2]])
li.append([[6]])
li = sorted(li, key=cmp_to_key(comp), reverse=True)

for i, v in enumerate(li):
    if v == [[2]]:
        a = i + 1
    if v == [[6]]:
        b = i + 1

print(a * b)
