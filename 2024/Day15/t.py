from functools import cache
import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

def multlist(lis):
    vRet = []
    for x in lis:
        if x == '#' or x == '.':
            vRet.extend([x] * 2)
        elif x == 'O':
            vRet.extend(['[',']'])
        elif x == '@':
            vRet.extend(['@', '.'])
    # print(vRet)
    return vRet

def listMov(y, ny, x):
    global mat2, vMov

    vMov.append([y, x])

    s = ''.join(mat2[y + ny][x:x+2])
    if s == '..':
        return True
    elif '#' in s:
        return False
    elif s == '[]':
        return listMov(y + ny, ny, x)
    elif s == '].':
        return listMov(y + ny, ny, x - 1)
    elif s == '.[':
        return listMov(y + ny, ny, x + 1)
    elif s == '][':
        return listMov(y + ny, ny, x - 1) and listMov(y + ny, ny, x + 1)
 
mat = []
mat2 = []
mov = ''
bmat = True
for lin in cal:
    if lin == '':
        bmat = False
    if bmat:
        mat.append(list(lin))
        mat2.append(multlist(list(lin)))
    else:
        mov += lin

s = '<>^v'
vDirection = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for m in range(len(mat)):
    for n in range(len(mat[0])):
        if mat[m][n] == '@':
            mat[m][n] = '.'
            y, x = m, n
            break

for c in list(mov):
    ny, nx = vDirection[s.index(c)]

    py, px = y + ny, x + nx
    oy, ox = py, px
    if mat[py][px] == 'O':
        while mat[py][px] == 'O':
            py, px = py + ny, px + nx

        if mat[py][px] == '.':
            mat[py][px] = 'O'
            mat[oy][ox] = '.'

    if mat[oy][ox] == '.':
        y, x = oy, ox

for m in range(len(mat)):
    for n in range(len(mat[0])):
        if mat[m][n] == 'O':
            total1 += (m * 100) + n

print('Answer 1: ', total1) # 1446158

for m in range(len(mat2)):
    for n in range(len(mat2[0])):
        if mat2[m][n] == '@':
            mat2[m][n] = '.'
            y, x = m, n
            break

for c in list(mov):
    ny, nx = vDirection[s.index(c)]

    py, px = y + ny, x + nx
    oy, ox = py, px
    if mat2[py][px] == '[' or mat2[py][px] == ']':
        if ny == 0:
            while mat2[py][px] == '[' or mat2[py][px] == ']':
                px = px + nx

            if mat2[py][px] == '.':
                while px != ox:
                    mat2[py][px] = mat2[py][px - nx]
                    px = px - nx
                mat2[oy][ox] = '.'
        else:
            pxi = px
            if mat2[py][px] == ']':                
                pxi -= 1

            vMov = []
            if listMov(py, ny, pxi):
                for vaux in vMov[::-1]:
                    mat2[vaux[0]][vaux[1]] = '.'
                    mat2[vaux[0]][vaux[1] + 1] = '.'
                for vaux in vMov[::-1]:
                    mat2[vaux[0] + ny][vaux[1]] = '['
                    mat2[vaux[0] + ny][vaux[1] + 1] = ']'
                    
    if mat2[oy][ox] == '.':
        y, x = oy, ox
    
    # mat2[y][x] = '@'
    # for linaux in mat2:
    #     print(''.join(linaux))
    # mat2[y][x] = '.'
    # print()


for m in range(len(mat2)):
    for n in range(len(mat2[0])):
        if mat2[m][n] == '[':
            total2 += (m * 100) + n

print('Answer 2: ', total2) # 1446175

print(f'Total Time: {time.perf_counter() - time_start}')
