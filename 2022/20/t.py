import time
# from rich import print # This greatly increases the time count.

time_start = time.perf_counter()


def ExecTime(Execute, Param1, Caption):
    time_start_int = time.perf_counter()
    print(f'{Caption} {Execute(Param1)} - Time: {time.perf_counter() - time_start_int}')


cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

vLines = []
for txt in cal:
    vLines.append(int(txt))


def Exec(nTimes):
    vPos = list(range(len(vLines)))  # [x for x in range(nLen)]
    nLen = len(vLines)
    nLenCalc = nLen - 1
    for _ in range(nTimes):
        for x in range(nLen):
            vPos.pop(nPos := vPos.index(x))
            vPos.insert((nPos + vLines[x]) % nLenCalc, x)

    nPosZero = vPos.index(vLines.index(0))
    return (sum(vLines[vPos[(nPosZero + x) % nLen]]
                for x in range(1000, 3001, 1000)))


ExecTime(Exec, 1, 'Turn 1:')  # 19559
vLines = [x * 811589153 for x in vLines]
ExecTime(Exec, 10, 'Turn 2:')  # 912226207972

print(f'Total Time: {time.perf_counter() - time_start}')
