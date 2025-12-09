from functools import cache
import time
from collections import deque

time_start = time.perf_counter()

Sample = False
if Sample:
    sFile = "inputsample.txt"
else:
    sFile = "input.txt"

cal = open(sFile, "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

vSet = set()
v = cal[0].replace(' ', '').split(',')
nmax = 0
for i in v:
    vSet.add(i)
    nmax = max(nmax, len(i))

@cache
def Busca(c):
    if len(c) == 0:
        return 1
    if len(c) == 1 and c in vSet:
        return 1
    if c in vNOk:
        return 0

    nQtd = 0
    for i in range(min(nmax, len(c)), 0, -1):
        if c[:i] in vSet:
            nQtd += Busca(c[i:])
    
    if nQtd == 0:
        vNOk.add(c)
    return nQtd

for c in cal[2:]:
    vNOk = set()
    nQtd = Busca(c)
    print(c, nQtd)
    if nQtd > 0:
        total1 += 1
        total2 += nQtd


print('Answer 1: ', total1) # 251
print('Answer 2: ', total2) # 616957151871345

print(f'Total Time: {time.perf_counter() - time_start}')
