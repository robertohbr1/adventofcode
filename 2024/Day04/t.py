cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

busca = 'XMAS'

total1 = total2 = 0

for t in [[0,1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0] , [-1, 1] ]:
    for y in range(len(cal)):
        for x in range(len(cal[0])):
            if cal[y][x] == busca[0]:
                bOk = True
                ymax = y + ((len(busca) - 1) * t[0])
                xmax = x + ((len(busca) - 1) * t[1])
                if ymax >= 0 and ymax < len(cal) and xmax >= 0 and xmax < len(cal[0]):
                    for z in range(1, len(busca)):
                        if cal[y + (z * t[0])][x + (z * t[1])] != busca[z]:
                            bOk = False
                            break
                    if bOk:
                        total1 += 1

for y in range(1, len(cal) - 1):
    for x in range(1, len(cal[0]) - 1):
        if cal[y][x] == 'A':
            s1 = sorted([cal[y - 1][x - 1], cal[y + 1][x + 1]])
            s2 = sorted([cal[y - 1][x + 1], cal[y + 1][x - 1]])
            if s1 == ['M', 'S'] and s2 == ['M', 'S']:
                total2 += 1

print('Answer 1: ', total1) # 2406

print('Answer 2: ', total2) # 1807
