import time

time_start = time.perf_counter()


def ExecTime(Execute, Param1, Caption):
    time_start_int = time.perf_counter()
    print(f'{Caption} {Execute(Param1)} - Time: {time.perf_counter() - time_start_int}')


cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

vLines = dict(line.split(': ') for line in cal)


def Exec(sName):
    s = vLines[sName]
    v = s.split()
    if len(v) == 1:
        return int(v[0])
    x1 = Exec(v[0])
    x2 = Exec(v[2])
    return int(eval(str(x1) + v[1] + str(x2)))


def ExecRetEquacion(sName):
    s = vLines[sName]
    v = s.split()
    if len(v) == 1:
        return v[0]
    x1 = ExecRetEquacion(v[0])
    x2 = ExecRetEquacion(v[2])
    return '(' + x1 + v[1] + x2 + ')'


def Exec2(_):
    vLines['humn'] = 'humn'
    v = vLines['root'].split()
    try:
        x1 = Exec(v[0])
    except:
        x1 = 0

    try:
        x2 = Exec(v[2])
    except:
        x2 = 0

    if x1 == 0:
        c = str(x2) + '-' + ExecRetEquacion(v[0])
    else:
        c = str(x1) + '-' + ExecRetEquacion(v[2])

    # print(c)
    c = eval(c.replace('humn', '-1j'))

    return (round(c.real / c.imag))


ExecTime(Exec, 'root', 'Turn 1:')  # 155708040358220
ExecTime(Exec2, 'root', 'Turn 2:')  # 3342154812537

print(f'Total Time: {time.perf_counter() - time_start}')
