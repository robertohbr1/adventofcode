import time

time_start = time.perf_counter()


def ExecTime(Execute, Param1, Caption):
    time_start_int = time.perf_counter()
    print(f'{Caption} {Execute(Param1)} - Time: {time.perf_counter() - time_start_int}')


cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

vArena = []
for txt in cal:
    vArena.append(txt)

d_5_10 = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}


def conv_5_10(txt):
    # Fisrt Code
    # nSum = 0
    # for x in range(len(txt)):
    #     nSum += (5 ** x) * d_5_10[txt[-(x + 1)]]
    # print(txt, nSum)
    # return nSum
    # Refactory 1
    # nSum = sum([(5 ** x) * d_5_10[txt[-(x + 1)]] for x in range(len(txt))])
    # print(txt, nSum)
    # return nSum
    # Refactory 2
    return sum([(5 ** x) * d_5_10[txt[-(x + 1)]] for x in range(len(txt))])


d_10_5 = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}


def conv_10_5(num):
    txt = ''
    while num > 0:
        rem = num % 5
        if rem > 2:
            num += rem
            txt += d_10_5[rem - 5]
        else:
            txt += d_10_5[rem]

        num //= 5

    return txt[::-1]


def Exec(Round):
    # First Code
    # nTot = 0
    # for txt in vArena:
    #     nTot += conv_5_10(txt)
    # Refactory 1
    # nTot = sum(map(conv_5_10, vArena))
    # return conv_10_5(nTot)
    # Refactory 2
    return conv_10_5(sum(map(conv_5_10, vArena)))


ExecTime(Exec, '1', 'Turn 1: ')  # 2-=12=2-2-2-=0012==2

print(f'Total Time: {time.perf_counter() - time_start}')
