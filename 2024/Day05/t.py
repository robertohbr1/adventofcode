cal = open("input.txt", "r", encoding="utf-8").read().split("\n")


total1 = total2 = 0

vConf = []
vTest = []
vList = []

bConf = True
for y in cal:
    if y == '':
        bConf = False
    elif bConf:
        vConf.append(y.split('|'))
    else:
        vTest.append(y.split(','))

for x in vConf:
    bFind = False
    for y in range(len(vList)):
        if x[0] == vList[y][0]:
            vList[y][1].append(x[1])
            bFind = True
    if not bFind:
        vList.append([x[0], [x[1]]])

def Test(x, y):
    for v in vList:
        if v[0] == x:
            return y in v[1]
    return False

def SortItems(items):
    while True:
        bTrocou = False
        for x in range(len(items) - 1):
            if not Test(items[x], items[x+1]):
                items[x], items[x+1] = items[x+1], items[x]
                bTrocou = True
        if not bTrocou:
            break
    return items

for items in vTest:
    bOk = True
    for x in range(len(items) - 1):
        if not Test(items[x], items[x+1]):
            bOk = False
    
    pos = int(len(items) / 2) 
    if bOk:
        total1 += int(items[pos])
    else:
        items = SortItems(items)
        total2 += int(items[pos])

print('Answer 1: ', total1) # 6242

print('Answer 2: ', total2) # 5169
