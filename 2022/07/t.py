cal = open('input.txt', 'r', encoding='utf-8').read().split('\n')
# print(cal)

v = ['/']
p = v.copy()
soma = [0]

atual = '-'.join(s for s in v)
for txt in cal:
    if txt == '':
        pass
    elif txt[0] == '$':
        txt = txt[2:]
        if txt == 'ls':
            pass
        elif txt == 'cd ..':
            if len(v) > 1:
                v = v[:-1]
        elif txt[0:3] == 'cd ':
            atual = txt[3:]
            if atual == '/':
                v = ['/']
            else:
                v.append(atual)
                atual = '-'.join(s for s in v)
                p.append(atual)
                soma.append(0)
    elif txt[:4] == 'dir ':
        pass
    else:
        t = int(txt.split(' ')[0])
        cam = ''
        for s in atual.split('-'):
            if len(cam) == 0:
                cam = s
            else:
                cam += '-' + s
            i = p.index(cam)
            soma[i] += t

tot = 0
for x in soma:
    if x < 100000:
        tot += x
print('Resp 1:', tot)

need = 30000000 - (70000000 - soma[0])
print('Need to 2:', need)

mn = 999999999999
for x in soma:
    if x > need:
        mn = min(mn, x)
i = soma.index(mn)
print('Resp 2:', mn)
print('Caminho:', p[i])
