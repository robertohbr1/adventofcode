import time

time_start = time.perf_counter()

cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0

matIni = [*map(int, list(cal[0]))]

mat = []
for x, i in enumerate(range(0, len(matIni) - 1, 2)):
    mat.extend(matIni[i] * [x])
    mat.extend(matIni[i + 1] * [-1])

mat.extend(matIni[-1] * [x + 1])

x = 0
while x < len(mat):
    while mat[-1] == -1:
        mat.pop()
    if x == len(mat):
        break
    if mat[x] == -1:
        mat[x] = mat.pop()        
    x += 1

total1 = sum([x * i for x, i in enumerate(mat)])
print('Answer 1: ', total1) # 6323641412437

mat = []
for x, i in enumerate(range(0, len(matIni) - 1, 2)):
    mat.append([matIni[i], x])
    mat.append([matIni[i + 1], -1])

mat.append([matIni[-1], x + 1])

for x in range(len(mat) - 1, 2, -1):
    if mat[x][1] != -1:
        v = mat[x]
        for y in range(1, x):
            if mat[y][1] == -1:
                if v[0] == mat[y][0]:
                    mat[x] = [v[0], -1]
                    mat[y] = v
                    break
                elif v[0] < mat[y][0]:
                    mat[x] = [v[0], -1]
                    mat[y][0] = mat[y][0] - v[0]
                    mat.insert(y, v)
                    break

mat2 = []
for x in mat:
    for y in range(x[0]):
        if x[1] == -1:
            mat2.append(0)
        else:
            mat2.append(x[1])
    

total2 = sum([x * i for x, i in enumerate(mat2)])
print('Answer 2: ', total2) # 6351801932670

print(f'Total Time: {time.perf_counter() - time_start}')
