import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

h = len(cal)
w = len(cal[0])

mat = []
for ny, lin in enumerate(cal):
    mat.append([z for z in lin])
    nx = lin.find('^')
    if nx >= 0:
        x, y = nx, ny

mat[y][x] = '.'

def TestaLoop(x1, y1, sX, sY):
    nx, ny = x1 - sX, y1 - sY # Return one step
    sX, sY = -sY, sX
    ret = False

    mat[y1][x1] = '#'

    visited = set()
    while True:
        if (nx, ny, sX, sY) in visited:
            ret = True
            break

        if not (0 <= nx + sX < w and 0 <= ny + sY < h):
            break

        visited.add((nx, ny, sX, sY))

        if mat[ny + sY][nx + sX] == '#':
            sX, sY = -sY, sX            
        else:
            nx += sX
            ny += sY
    
    mat[y1][x1] = '.'
    return ret

sX, sY = 0, -1 # Up

vis = set()
bloq = set()
tested = set()
while True:
    vis.add((x, y))

    if not (0 <= x + sX < w and 0 <= y + sY < h):
        break

    if mat[y + sY][x + sX] == '#':
        sX, sY = -sY, sX
    else:
        x += sX
        y += sY

        if not (x, y) in tested:
            tested.add((x, y))
            if TestaLoop(x, y, sX, sY):
                bloq.add((x, y))


        # # if not (x + sX, y + sY) in tested:
        # #     tested.add((x + sX, y + sY))
        # #     if TestaLoop(x, y, sX, sY):
        # #         bloq.add((x + sX, y + sY))

        # x += sX
        # y += sY


total1 = len(vis)
print('Answer 1: ', total1) # 5531

total2 = len(bloq)
print('Answer 2: ', total2) # 2165

print(f'Total Time: {time.perf_counter() - time_start}')