import string
cal = open('input.txt', 'r', encoding='utf-8').read().strip().split('\n')


def Calc(txt):
    global soma
    soma += string.ascii_letters.index(txt[0]) + 1


soma = 0
for txt in cal:
    x = len(txt) // 2
    Calc([s for s in txt[:x] if s in txt[x:]])
print("Round 1:", soma)  # 7674


soma = 0
z = 0
for x in range(0, len(cal), 3):
    Calc([s for s in cal[x] if s in cal[x + 1] and s in cal[x + 2]])
print("Round 2:", soma)  # 2805
