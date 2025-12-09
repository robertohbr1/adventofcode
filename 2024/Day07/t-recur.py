# Recursive solution
# It's faster than another solution: t-array.py

import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

# def SumRecur(n, s, v, IsAns2):
#     if n < s: return False
#     r1 = s + v[0]
#     r2 = s * v[0]
#     r3 = int(str(s) + str(v[0]))

#     if len(v) == 1:
#         return (n == r1 or n == r2 or n == r3)

#     if SumRecur(n, r1, v[1:], IsAns2):
#         return True
#     elif SumRecur(n, r2, v[1:], IsAns2):
#         return True
#     elif IsAns2:
#         return SumRecur(n, r3, v[1:], IsAns2)
#     else:
#         return False
    
def SumRecur(n, s, v, IsAns2):
    if n < s: return False

    if len(v) == 0:
        return (n == s)

    if SumRecur(n, s + v[0], v[1:], IsAns2):
        return True
    elif SumRecur(n, s * v[0], v[1:], IsAns2):
        return True
    elif IsAns2:
        return SumRecur(n, int(str(s) + str(v[0])), v[1:], IsAns2)
    else:
        return False

for lin in cal:    
    v = [*map(int, lin.replace(':','').split())]
    if SumRecur(v[0], 0, v[1:], False):
        total1 += v[0]
        total2 += v[0]
    elif SumRecur(v[0], 0, v[1:], True):
        total2 += v[0]

print('Answer 1: ', total1) #  1611660863222
print('Answer 2: ', total2) # 945341732469724

print(f'Total Time: {time.perf_counter() - time_start}')
