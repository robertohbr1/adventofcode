from functools import cache
import time
from collections import deque, defaultdict

time_start = time.perf_counter()

Sample = False
if Sample:
    file = "inputsample.txt"
else:
    file = "input.txt"

cal = open(file, "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

vKeys = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['#', '0', 'A']]
posIniKey = (3, 2)
vDirs = [['#', '^', 'A'], ['<', 'v', '>']]
vDirsFind = '^A<v>'
posIniDir = (0, 2)

def Find(c, v):
    for y in range(len(v) + 1):
        for x in range(3):
            if v[y][x] == c:
                return (y, x)
    return (0, 0)

def Mov(y, x, c, vKeys):
    yn, xn = Find(c, vKeys)
    if ((len(vKeys) == 4 and y == 3) or (len(vKeys) == 2 and y == 0)) and xn == 0:
        return yn, xn, '' \
            + ('^' if yn < y else 'v') * abs(y - yn) \
            + ('<' if xn < x else '>') * abs(x - xn) \
            + 'A'
    else:
        return yn, xn, '' \
            + ('<' if xn < x else '>') * abs(x - xn) \
            + ('^' if yn < y else 'v') * abs(y - yn) \
            + 'A'

def Mov2(c1, c2, vDirs):
    _, _, sRet = Mov(*Find(c1, vDirs), c2, vDirs)
    return sRet

dirKeys = {(p1, p2): Mov2(p1, p2, vDirs)  for p1 in vDirsFind for p2 in vDirsFind}

def Calc(txt):
    Ret = ''
    y, x = posIniKey
    for c in txt:
        y, x, sRet = Mov(y, x, c, vKeys)
        Ret += sRet        
    return Ret

# @cache
# def CalcText(txt, times):
#     if times == 0:
#         return txt
#     length = ''
#     for p1, p2 in zip("A" + txt, txt):
#         s = dirKeys[(p1, p2)]
#         length += s
#     return CalcText(length, times - 1)    

@cache
def Calc2(txt, times):
    length = 0
    for p1, p2 in zip("A" + txt, txt):
        s = dirKeys[(p1, p2)]
        if times == 1:
            length += len(s)
        else:
            length += Calc2(s, times - 1)
    return length

for c in cal:
    s1 = Calc2(Calc(c), 2)
    s2 = Calc2(Calc(c), 25)
    # print(c, s2)
    total1 += s1 * int(c.replace('A',''))
    total2 += s2 * int(c.replace('A',''))
    
print('Answer 1: ', total1) # 197560
print('Answer 2: ', total2) # 242337182910752 Certo
                            # 277554934879758 Atual - Revisar

print(f'Total Time: {time.perf_counter() - time_start}')

# print(CalcText(Calc('964A'), 4))