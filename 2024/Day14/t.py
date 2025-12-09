from functools import cache
import time

time_start = time.perf_counter()

# w, h = 11, 7
w, h = 101, 103
cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

@cache
def Calc(n):
    t = [0] * 4
    for v in mat:
        x = (v[0] + (v[2] * n)) % w
        y = (v[1] + (v[3] * n)) % h
        if y != h // 2 and x != w // 2:
            t[(0 if (y < h // 2) else 2) + (0 if (x < w // 2) else 1)] += 1
    xRet = 1
    for x in t:
        xRet *= x
    return xRet

mat = []
for lin in cal:
    lin = lin.replace('p=', '').replace('v=', '').replace(' ', ',')
    mat.append([*map(int, lin.split(','))])

total1 = Calc(100)
print('Answer 1: ', total1) # 214400550

nMin = 1e10
total2 = 0
for x in range(1, 10000):
    s = Calc(x)
    if s < nMin: # I don't understand why the answer is in the step with the lowest value...
        nMin, total2 = s, x

print('Answer 2: ', total2) # 8149

print(f'Total Time: {time.perf_counter() - time_start}')
