cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

def IsSafe(v):
    v2 = sorted(v.copy())
    
    if (v == v2) or (v[::-1] == v2):
        vDif = [b - a for a, b in zip(v2, v2[1:])]
        if (max(vDif)) <= 3 and (min(vDif)) > 0:
            return True
    return False

total1 = total2 = 0
for i in cal:
    v = [*map(int, i.split())]
    if IsSafe(v):
        total1 += 1
        total2 += 1
    else:
        for i in range(len(v)):
            if IsSafe(v[:i] + v[i+1:]):
                total2 += 1
                break

print('Answer 1: ', total1) # 369

print('Answer 2: ', total2) # 428
