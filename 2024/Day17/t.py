from functools import cache
import time
import heapq

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

for lin in cal:
    v = lin.split(':')
    v[0] = v[0].replace('Register ','').replace('Program','P')   
    match v[0]:
        case 'A':
            a = int(v[1])
        case 'B':
            b = int(v[1])
        case 'C':
            c = int(v[1])
        case 'P':
            program = [*map(int, v[1].split(','))]

def Calc(a, b = 0, c = 0):        
    def Ret(i):
        if i <= 3:
            return i
        elif i == 4:
            return a
        elif i == 5:
            return b
        elif i == 6:
            return c
        else:
            raise 1
        
    v= []
    x = 0
    while x < len(program):
        o = program[x + 1]
        op = Ret(o)
        match program[x]:
            case 0:
                a = a >> op
            case 1:  # bxl
                b = b ^ o
            case 2:  # bst
                b = op % 8
            case 3:
                if a != 0:
                    x = o
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:
                v.append(op % 8)
            case 6:  # bdv
                b = a >> op
            case 7:  # cdv
                c = a >> op
        x += 2
    return v

v = Calc(a, b, c)

total1 = ','.join([*map(str, v)])

print('Answer 1: ', total1) # 1,6,3,6,5,6,5,1,7

candidates = [0]
for l in range(len(program)):
    next_candidates = []
    for val in candidates:
        for i in range(8):
            target = (val << 3) + i
            if Calc(target) == program[-l - 1 :]:
                next_candidates.append(target)
    candidates = next_candidates

total2 = min(candidates)

print('Answer 2: ', total2) # 247839653009594

print(f'Total Time: {time.perf_counter() - time_start}')
