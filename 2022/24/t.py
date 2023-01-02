import time

time_start = time.perf_counter()

cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

yE, xE = 0, 1
vPos = {(yE, xE)}

vArena = []
for txt in cal:
    vArena.append([x for x in txt])

yMax = len(vArena) - 2
xMax = len(vArena[0]) - 2

# Since the start and end points are known, these targets are fixed.
# If they could be anywhere in the Arena, the points would need to be fetched
vTarget = [(yMax + 1, xMax), (yE, xE), (yMax + 1, xMax)]
# To the firts Round, you can use this configuration
#vTarget = [(yMax + 1, xMax)]

vSnow = []
for y in range(len(vArena)):
    for x in range(len(vArena[0])):
        xd, yd = 0, 0
        if vArena[y][x] == '>':
            xd, yd = 1, 0
        elif vArena[y][x] == '<':
            xd, yd = -1, 0
        elif vArena[y][x] == '^':
            xd, yd = 0, -1
        elif vArena[y][x] == 'v':
            xd, yd = 0, 1
        if xd + yd != 0:
            vSnow.append((y, x, yd, xd, vArena[y][x]))
            vArena[y][x] = '.'


def Move():
    for n in range(len(vSnow)):
        (y, x, yd, xd, c) = vSnow[n]
        y = ((y + yd - 1) % yMax) + 1
        x = ((x + xd - 1) % xMax) + 1
        vSnow[n] = (y, x, yd, xd, c)


vMove = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]


def Mount():
    global vPos, yE, xE
    # Clear the Arena
    for y in range(len(vArena)):
        for x in range(len(vArena[0])):
            if vArena[y][x] != '#':
                vArena[y][x] = '.'

    # Put the Snow in the Arena
    for pos in vSnow:
        (y, x, _, _, c) = pos
        vArena[y][x] = c
        # You can use this code to show how the sample site
        # To change, comment the line above and uncomment the block below
        # if vArena[y][x] == '.':
        #     vArena[y][x] = c
        # elif vArena[y][x] == '2':
        #     vArena[y][x] = '3'
        # else:
        #     vArena[y][x] = '2'

    # Calc all the posible moves (or if can stay in the same place)
    vNewPos = {(0, 0)}
    vNewPos.pop()
    while vPos:
        (yE, xE) = vPos.pop()

        for (yD, xD) in vMove:
            yF = yE + yD
            xF = xE + xD
            if (0 <= yF <= yMax + 1 and 0 <= xF <= xMax + 1):
                if vArena[yF][xF] == '.':
                    vNewPos.add((yF, xF))
                    if yF == yTarget and xF == xTarget:
                        yE = yF
                        xE = xF
                        # Use this to Show how the Arena looks
                        # vArena[yE][xE] = 'E'
                        return

    vPos = vNewPos
    # Use this to Show how the Arena looks
    # for (yE, xE) in vPos:
    #     vArena[yE][xE] = 'E'

# Use this to show how the Arena looks


def Show():
    for x in vArena:
        print(''.join(x))
    print()


nCount = 0
while vTarget:
    (yTarget, xTarget) = vTarget.pop()
    while True:
        nCount += 1
        # Use this to Show how the Arena looks - Show the Minutes
        # print(nCount)
        Move()
        Mount()
        # Use this to Show how the Arena looks
        # Show()
        if yE == yTarget and xE == xTarget:
            break

    if len(vTarget) == 2:
        print('Round 1: ', nCount)  # 257
    elif len(vTarget) == 0:
        print('Round 2: ', nCount)  # 828
    # print(yE, xE)
    # Start new position with last position ONLY
    vPos = {(yE, xE)}

print(f'Total Time: {time.perf_counter() - time_start}')
