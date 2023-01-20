cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

soma = 0
for txt in cal:
    b1 = ord(txt[0]) - ord('A')
    b2 = ord(txt[2]) - ord('X')
    if b1 == b2:
        y = 3
    elif b1 == (b2 + 2) % 3:
        y = 6
    else:
        y = 0
    soma += (b2 + 1) + y
    # print(b, x, y)
print('Round 1:', soma)  # 12794

soma = 0
for txt in cal:
    b1 = ord(txt[0]) - ord('A')
    b2 = ord(txt[2]) - ord('X')

    x = (b1 + b2) % 3
    if x == 0:
        x = 3

    soma += x + (b2 * 3)

print('Round 2:', soma)  # 14979
