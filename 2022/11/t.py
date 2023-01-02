from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

vS = []
vM = []
vO = []
vT = []
vTrue = []
vFalse = []

for txt in cal:
    txt = txt.strip()
    if txt.split(' ')[0] == 'Monkey':
        pos = int(txt.split(' ')[1][:-1])
    elif txt.split(':')[0] == 'Starting items':
        vM.append(pos)
        vM[pos] = txt.split(':')[1].split(',')
        for x in range(len(vM[pos])):
            vM[pos][x] = int(vM[pos][x])
    elif txt.split(':')[0] == 'Operation':
        vO.append(pos)
        _, _, _, _, o, v = txt.split(' ')
        vO[pos] = [o, v]
    elif txt.split(':')[0] == 'Test':
        vT.append(pos)
        vT[pos] = int(txt.split('by')[1].strip())
    elif txt.split(':')[0] == 'If true':
        vTrue.append(pos)
        vTrue[pos] = int(txt.split('monkey')[1].strip())
    elif txt.split(':')[0] == 'If false':
        vFalse.append(pos)
        vFalse[pos] = int(txt.split('monkey')[1].strip())

vS = [0] * len(vM)
vMCopy = []
for y in vM:
    vMCopy.append(y[:])

for x in range(20):
    for y in range(len(vM)):
        for z in range(len(vM[y])):
            vS[y] += 1
            if vO[y][0] == '+':
                t = vM[y][z] + int(vO[y][1])
            else:
                if vO[y][1] == 'old':
                    t = vM[y][z] * vM[y][z]
                else:
                    t = vM[y][z] * int(vO[y][1])
            t = t // 3
            if t % vT[y] == 0:
                xTo = vTrue[y]
            else:
                xTo = vFalse[y]
            vM[xTo].append(t)
        vM[y] = []

vS.sort()

print(vS[-1] * vS[-2])

vM = vMCopy.copy()
vS = []
vS = [0] * len(vM)

dv = 1
for x in vT:
    dv *= x

for x in range(10000):
    for y in range(len(vM)):
        for z in range(len(vM[y])):
            vS[y] += 1
            if vO[y][0] == '+':
                t = vM[y][z] + int(vO[y][1])
            else:
                if vO[y][1] == 'old':
                    t = vM[y][z] * vM[y][z]
                else:
                    t = vM[y][z] * int(vO[y][1])

            t = t % dv

            if t % vT[y] == 0:
                xTo = vTrue[y]
            else:
                xTo = vFalse[y]
            vM[xTo].append(t)
        vM[y] = []

vS.sort()

print(vS[-1] * vS[-2])
