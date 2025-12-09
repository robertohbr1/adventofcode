cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

vLeft = []
vRight = []

for i in cal:
    x, y = map(int, i.split())
    vLeft.append(x)
    vRight.append(y)

vLeft.sort()
vRight.sort()

print('Answer 1: ', sum(abs(vLeft[i] - vRight[i]) for i in range(len(vLeft)))) # 2166959

print('Answer 2: ', sum(vLeft[i] * vRight.count(vLeft[i]) for i in range(len(vLeft)))) #23741109
