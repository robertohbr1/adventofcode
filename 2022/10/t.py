# from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

pontos = [20, 60, 100, 140, 180, 220]
ciclo = 1
x = 1
tot = 0


def teste():
    global ciclo
    global tot
    ciclo += 1
    if ciclo in pontos:
        tot += x * ciclo


for txt in cal:
    if txt.strip() == 'noop':
        teste()
        continue
    _, d = txt.split(' ')
    teste()
    x += int(d)
    teste()

print(tot)


def desenha(t):
    if abs(x - (t % 40)) > 1:
        mat[t // 40][t % 40] = ' '


def teste2():
    global ciclo
    ciclo += 1
    if ciclo // 40 > 5:
        return
    desenha(ciclo)


mat = [['#' for _ in range(40)] for _ in range(6)]
ciclo = 0
x = 1
for txt in cal:
    if txt.strip() == 'noop':
        teste2()
        continue
    _, d = txt.split(' ')
    teste2()
    x += int(d)
    teste2()

for x in range(6):
    print(''.join(mat[x]))
