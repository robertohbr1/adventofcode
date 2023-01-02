import time

time_start = time.perf_counter()


def ExecTime(Execute, Param1, Caption):
    time_start_int = time.perf_counter()
    print(f'{Caption} {Execute(Param1)} - Time: {time.perf_counter() - time_start_int}')


cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

# Dice number   Dice reference
# .12           .12
# .3.           .4.
# 45.           67.
# 6..           9..
# Dice face numbers
f1, f2, f3, f4, f5, f6 = 1, 2, 4, 6, 7, 9
# Direction 0-Right, 1-Down, 2-Left, 3-Top
R, D, L, U = 0, 1, 2, 3
# (Referencia, Direction): lambda y, x, nDir: (...),
troca = {
    (f1, L): lambda y, x, nDir: (149 - y,            0, R),  # From 1 L to 4 R * 180º
    (f1, U): lambda y, x, nDir: (x + 100,            0, R),  # From 1 U to 6 R * 270º
    (f2, R): lambda y, x, nDir: (149 - y,           99, L),  # From 2 R to 5 L * 180º
    (f2, D): lambda y, x, nDir: (x - 50,            99, L),  # From 2 D to 3 L * 270º
    (f2, U): lambda y, x, nDir: (199,          x - 100, U),  # From 2 U to 6 U * 0º
    (f3, R): lambda y, x, nDir: (49,            y + 50, U),  # From 3 R to 2 U * 90º
    (f3, L): lambda y, x, nDir: (100,           y - 50, D),  # From 3 L to 4 D * 90º
    (f4, L): lambda y, x, nDir: (49 - (y - 100),    50, R),  # From 4 L to 1 R * 180º
    (f4, U): lambda y, x, nDir: (x + 50,            50, R),  # From 4 U to 3 R * 270º
    (f5, R): lambda y, x, nDir: (49 - (y - 100),   149, L),  # From 5 R to 2 L * 180º
    (f5, D): lambda y, x, nDir: (100 + x,           49, L),  # From 5 D to 6 L * 270º
    (f6, R): lambda y, x, nDir: (149,          y - 100, U),  # From 6 R to 5 U * 90º
    (f6, D): lambda y, x, nDir: (0,            x + 100, D),  # From 6 D to 2 D * 0º
    (f6, L): lambda y, x, nDir: (0,            y - 100, D)}  # From 6 L to 1 D * 90º

vMove = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sDirections = ''
vArena = []
bLeDirection = False
for txt in cal:
    if txt == '':
        bLeDirection = True
    elif bLeDirection:
        sDirections = txt.strip()
    else:
        vArena.append([t for t in txt])

x, y, nDir = 0, 0, 0
vDir = []
sDir = 'I'
sQtd = ''
for txt in sDirections + '.':
    if txt in ['R', 'L', '.']:
        vDir.append([sDir, int(sQtd)])
        sDir = txt
        sQtd = ''
    else:
        sQtd += txt


maxX = max([len(t) for t in vArena])
vArena.append([' '])
maxY = len(vArena)
# Resize Lines to same size (maxX)
for z in range(maxY):
    while len(vArena[z]) < maxX:
        vArena[z].append(' ')


def Soma(xd, yd):
    global x, y
    if xd != 0:
        x = (x + xd) % maxX
    if yd != 0:
        y = (y + yd) % maxY


def CalcDir():
    global nDir, xd, yd
    xd, yd = vMove[nDir]


def Roda(dir):
    global nDir
    if dir == 'I':
        while vArena[y][x] == ' ':
            Soma(1, 0)
    elif dir == 'R':
        nDir = (nDir + 1) % 4
    else:
        nDir = (nDir - 1) % 4

    CalcDir()


def Testa(xd, yd, Round):
    global x, y, nDir

    nQua = y // 50 * 3 + x // 50
    Soma(xd, yd)
    if Round == '1':
        while vArena[y][x] == ' ':
            Soma(xd, yd)
    else:
        if vArena[y][x] == ' ':
            (y, x, nDir) = troca[(nQua, nDir)](y, x, nDir)
            CalcDir()


def Exec(Round):
    global x, y, nDir

    x, y, nDir = 0, 0, 0
    for dir, qtd in vDir:
        Roda(dir)
        for _ in range(qtd):
            xAnt, yAnt, nDirAnt = x, y, nDir
            Testa(xd, yd, Round)
            if vArena[y][x] == '#':
                x, y, nDir = xAnt, yAnt, nDirAnt
                break

    print(y, x, nDir)
    return 1000 * (y + 1) + 4 * (x + 1) + nDir


ExecTime(Exec, '1', 'Turn 1: (Target: 1428) - ')  # 1428
ExecTime(Exec, '2', 'Turn 2: (Target 142380) - ')  # 142380

print(f'Total Time: {time.perf_counter() - time_start}')
