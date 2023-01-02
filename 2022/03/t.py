import string
cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')

soma = 0
for txt in cal:
    x = len(txt) // 2
    a, b = txt[:x], txt[x:]
    c = [s for s in a if s in b][0]
    if c.islower():
        i = ord(c) - ord('a') + 1
    else:
        i = ord(c) - ord('A') + 27
    soma += i
    # print(x, a, b, c, i)
print(soma)


soma = 0
z = 0
v = ['', '', '']
for txt in cal:
    v[z] = txt
    z += 1
    if z == 3:
        z = 0
        c = ''.join([s for s in v[0] if s in v[1]])
        c = [s for s in c if s in v[2]][0]
        if c.islower():
            i = ord(c) - ord('a') + 1
        else:
            i = ord(c) - ord('A') + 27
        soma += i
        print(v, c, i)
print(soma)
