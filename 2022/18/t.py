from collections import deque
from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

Cubes = set()
for txt in cal:
    x, y, z = (map(int, txt.split(',')))
    Cubes.add((x, y, z))

# print(Cubes)

vNeig = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

n = 0
for (x, y, z) in Cubes:
    for (xd, yd, zd) in vNeig:
        if (x + xd, y + yd, z + zd) not in Cubes:
            n += 1

print('Turn 1: ', n)  # 3432


def Compare(vPos, vRef, nDif):
    if (vPos[0] == vRef[0] + nDif
       or vPos[1] == vRef[1] + nDif
       or vPos[2] == vRef[2] + nDif):
        return True
    return False


outside = set()
maxC = [max([cube_position[i] for cube_position in Cubes])
        for i in range(3)]
minC = [min([cube_position[i] for cube_position in Cubes])
        for i in range(3)]


def Test(pos):
    global outside
    global Cubes
    return (
        pos in Cubes
        or pos in outside
        or Compare(pos, minC, -2)
        or Compare(pos, maxC, 2)
    )


def get_outside():
    global outside

    queue = [(minC[0] - 1, minC[1] - 1, minC[2] - 1)]
    while len(queue) > 0:
        pos = queue.pop(0)

        if Test(pos):
            continue

        outside.add(pos)
        for (xd, yd, zd) in vNeig:
            pos2 = (pos[0] + xd, pos[1] + yd, pos[2] + zd)
            if not Test(pos2):
                queue.append(pos2)
    return


get_outside()

n = 0
for (x, y, z) in Cubes:
    for (xd, yd, zd) in vNeig:
        if (x + xd, y + yd, z + zd) in outside:
            n += 1

print('Turn 2: ', n)  # 2042
