from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

# Calcule the size of Arena
xMin, yMin, xMax, yMax = 9999999, 9999999, 0, 0
for txt in cal:
    v = txt.split(' -> ')
    for i in v:
        x, y = i.split(',')
        x = int(x)
        y = int(y)
        xMin = min(xMin, x)
        yMin = min(yMin, y)
        xMax = max(xMax, x)
        yMax = max(yMax, y)

yMin = 0

# This code is an ajust for the secound turn
# How I don´t redraw the arena, this is requeried
# xMin has been the Origin (500) minus the Height - 2
# xMax too, 500 plus Height + 2
# But, to run the first turn, this 2 lines are not necessary
xMin = min(xMin, 500 - yMax - 2)
xMax = max(xMax, 500 + yMax + 2)

#print(xMin, yMin, xMax, yMax)

# Create Arena with Spaces
arena = [[' ' for x in range(xMax - xMin + 2)]for y in range(yMax + 3)]

# Only show the Arena to visual validation


def mostra():
    for txt in arena:
        print(''.join(txt))


def splitXY(txt):
    x, y = txt.split(',')
    return int(x), int(y)


# Draw the Lines
for txt in cal:
    v = txt.split(' -> ')
    x1, y1 = splitXY(v[0])
    for i in range(1, len(v)):
        x2, y2 = splitXY(v[i])

        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                arena[y][x - xMin + 1] = '#'

        x1, y1 = x2, y2

# mostra()


def processa():
    global x, y
    if arena[y + 1][x] == ' ':
        pass
    elif arena[y + 1][x - 1] == ' ':
        x -= 1
    elif arena[y + 1][x + 1] == ' ':
        x += 1
    else:
        arena[y][x] = 'o'
        return True
    y += 1
    return False


y = 0
conta = 0
xIni = 500 - xMin + 1
while y < yMax:
    conta += 1
    x, y = xIni, 0
    while y < yMax:
        if processa():
            break

# mostra()
conta -= 1
print('Turn 1', conta)  # 779

# Draw the bottom line for the secound turn
for x in range(len(arena[0])):
    arena[yMax + 2][x] = '#'

# This turn begin in the same position where the first turn ended
yMax += 1
while arena[0][xIni] == ' ':
    conta += 1
    x, y = xIni, 0
    while arena[0][xIni] == ' ':
        if processa():
            break

# mostra()
print('Turn 2', conta)  # 27426
