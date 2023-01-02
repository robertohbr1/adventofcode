# This solution is only to Turn 1
# The t.py solution is to all Turns
import time
# from rich import print # This greatly increases the time count.

time_start = time.perf_counter()


def ExecTime(Execute, Param1, Caption):
    time_start_int = time.perf_counter()
    print(f'{Caption} {Execute(Param1)} - Time: {time.perf_counter() - time_start_int}')


cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

vLines = []
nIndex = 0
for txt in cal:
    v = txt.split(':')
    if v[0] == 'root':
        nIndex = len(vLines)
    vLines.append([v[0], v[1], v[1], ''])

n = 0
while True:
    v = vLines[n]
    if v[3] == "":
        try:
            res = str(int(eval(v[2])))
        except:
            pass
        else:
            vLines[n][3] = res
            if n == nIndex:
                break
            for z in range(len(vLines)):
                vLines[z][2] = vLines[z][2].replace(v[0], res)

    n += 1
    if n >= len(vLines):
        n = 0

print(vLines[nIndex][3])  # 155708040358220

print(f'Total Time: {time.perf_counter() - time_start}')
