cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')
# cal = [sum(map(int, i.strip().split('\n'))) for i in cal.split('\n\n')]

soma = 0
for i in cal:
    b = i.split(' ')
    x = (ord(b[1]) - ord('X')) + 1
    y = 0
    if b[0] + b[1] in ('AX', 'BY', 'CZ'):
        y = 3
    if b[0] + b[1] in ('CX', 'AY', 'BZ'):
        y = 6
    soma += x + y
    # print(b, x, y)
print(soma)

soma = 0
for i in cal:
    b = i.split(' ')
    if b[0] == 'A':
        if b[1] == 'X':
            x = 3 + 0
        elif b[1] == 'Y':
            x = 1 + 3
        else:
            x = 2 + 6
    elif b[0] == 'B':
        if b[1] == 'X':
            x = 1 + 0
        elif b[1] == 'Y':
            x = 2 + 3
        else:
            x = 3 + 6
    else:
        if b[1] == 'X':
            x = 2 + 0
        elif b[1] == 'Y':
            x = 3 + 3
        else:
            x = 1 + 6

    y = 0
    # if b[0] + b[1] in ('AX', 'BY', 'CZ'):
    #     y = 3
    # if b[0] + b[1] in ('CX', 'AY', 'BZ'):
    #     y = 6
    soma += x + y
    # print(b, x, y)
print(soma)
