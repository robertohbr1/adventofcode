from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

x, y, mx, my, nx, ny = 0, 0, 0, 0, 999999, 999999
for txt in cal:
    d, n = txt.split(' ')
    for c in range(int(n)):
        if d == 'R':
            x += 1
        elif d == 'L':
            x -= 1
        elif d == 'U':
            y -= 1
        elif d == 'D':
            y += 1
    mx = max(mx, x)
    my = max(my, y)
    nx = min(nx, x)
    ny = min(ny, y)

x = -nx
y = -ny
my += y + 1
mx += x + 1

print(x, y, mx, my)


def sign(x):
    return (x > 0) - (x < 0)


def Exec(x, y, mx, my, tam):
    mat = [[0 for i in range(mx)] for j in range(my)]

    mat[y][x] = 1

    vx = [x for i in range(tam)]
    vy = [y for i in range(tam)]
    last = tam - 1

    for txt in cal:
        d, n = txt.split(' ')
        for c in range(int(n)):
            for ct in range(last):
                if ct == 0:
                    if d == 'R':
                        vx[0] += 1
                    elif d == 'L':
                        vx[0] -= 1
                    elif d == 'U':
                        vy[0] -= 1
                    elif d == 'D':
                        vy[0] += 1

                ct1 = ct + 1
                if vx[ct] == vx[ct1]:
                    if abs(vy[ct] - vy[ct1]) > 1:
                        vy[ct1] += sign(vy[ct] - vy[ct1])
                elif vy[ct] == vy[ct1]:
                    if abs(vx[ct] - vx[ct1]) > 1:
                        vx[ct1] += sign(vx[ct] - vx[ct1])
                else:
                    if abs(vy[ct] - vy[ct1]) > 1 or abs(vx[ct] - vx[ct1]) > 1:
                        vy[ct1] += (sign(vy[ct] - vy[ct1]))
                        vx[ct1] += (sign(vx[ct] - vx[ct1]))
            mat[vy[last]][vx[last]] = 1

    print(sum(sum(mat, [])))


Exec(x, y, mx, my, 2)  # 6332
Exec(x, y, mx, my, 10)  # 2511
