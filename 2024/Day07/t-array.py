import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

vVar = [[[0], [1]]]
for x in range(1, 12):
    vVar.append([])
    for y in vVar[x - 1]:
        for z in vVar[0]:
            vVar[x].append(y + z)

vVar2 = [[[0], [1], [2]]]
for x in range(1, 12):
    vVar2.append([])
    for y in vVar2[x - 1]:
        for z in vVar2[0]:
            vVar2[x].append(y + z)

def testaVar(n, v, vX):
    for ct in vX:
        su = v[0]
        for idx, x in enumerate(ct):
            if x == 0:
                su += v[idx + 1]
            elif x == 1:
                su *= v[idx + 1]
            else:
                su = int(str(su) + str(v[idx + 1]))
            if su > n:
                break
        if n == su:
            return True
        # print(v, ct, su)
    return False

for lin in cal:    
    v = [*map(int, lin.replace(':','').split())]
    if testaVar(v[0], v[1:], vVar[len(v) - 3]):
        total1 += v[0]
        total2 += v[0]
    elif testaVar(v[0], v[1:], vVar2[len(v) - 3]):
        total2 += v[0]

print('Answer 1: ', total1) #  1611660863222
print('Answer 2: ', total2) # 945341732469724

print(f'Total Time: {time.perf_counter() - time_start}')
