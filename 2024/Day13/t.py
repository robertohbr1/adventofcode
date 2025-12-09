from functools import cache
import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

def Testa():
    global vA, vB, vP

 # https://en.wikipedia.org/wiki/Cramer%27s_rule
    x = ((vP[0] * vB[1]) - (vP[1] * vB[0])) / ((vA[0] * vB[1]) - (vA[1] * vB[0]))
    y = ((vP[1] * vA[0]) - (vP[0] * vA[1])) / ((vA[0] * vB[1]) - (vA[1] * vB[0]))

    if int(x) == x and int(y) == y:
        return int(x * 3 + y)

    return 0

for lin in cal:
    lin = lin.replace(' ', '').replace('X', '').replace('Y', '').replace('+', '').replace('=', '')
    v1 = lin.split(":")
    if v1[0] == 'ButtonA':
        vA = [*map(int, v1[1].split(','))]
    elif v1[0] == 'ButtonB':
        vB = [*map(int, v1[1].split(','))]
    elif v1[0] == 'Prize':
        vP = [*map(int, v1[1].split(','))]
        total1 += Testa()
        vP[0], vP[1] = vP[0] + 10000000000000, vP[1] + 10000000000000
        total2 += Testa()

print('Answer 1: ', total1) # 26599
print('Answer 2: ', total2) # 106228669504887

print(f'Total Time: {time.perf_counter() - time_start}')
