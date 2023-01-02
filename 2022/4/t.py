cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

soma = 0
soma2 = 0
for txt in cal:
    a = txt.split(',')
    b = a[0].split('-')
    c = a[1].split('-')

    if ((int(b[0]) >= int(c[0])) and (int(b[1]) <= int(c[1]))) or \
            ((int(c[0]) >= int(b[0])) and (int(c[1]) <= int(b[1]))):
        soma += 1

    if not ((int(b[1]) < int(c[0])) or (int(c[1]) < int(b[0]))):
        soma2 += 1

print('1', soma)
print('2', soma2)
