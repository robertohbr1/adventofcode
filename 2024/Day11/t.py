from functools import cache
import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

mat = [*map(int, cal[0].split())]

@cache
def Rec(num, qtd):
    if qtd == 0:
        return 1
    qtd -= 1
    s = str(num)

    if num == 0:
        return Rec(1, qtd)
    elif len(s) % 2 == 0:
        l = len(s) // 2
        return Rec(int(s[0:l]), qtd) + Rec(int(s[l:]), qtd)
    else:
        return Rec(num * 2024, qtd)

for x in mat:
    total1 += Rec(x, 25)
    total2 += Rec(x, 75)

print('Answer 1: ', total1) # 229043
print('Answer 2: ', total2) # 272673043446478

print(f'Total Time: {time.perf_counter() - time_start}')
