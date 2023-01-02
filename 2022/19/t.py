import re
from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

vLines = []
for txt in cal:
    valves = list(map(int, re.findall(r'\d+', txt)))
    vLines.append(valves)


def Gera(nTime, num, vNeed, vQtd, vRob, nTry):
    global nMax
    oreore = vNeed[0][0]
    clayore = vNeed[1][0]
    obsore = vNeed[2][0]
    obsclay = vNeed[2][1]
    geoore = vNeed[3][0]
    geoobs = vNeed[3][2]
    qOre, qClay, qObs, qGeo = vQtd
    nOre, nClay, nObs, nGeo = vRob

    xMax = 0
    while nTime > 0:
        nAddOre, nAddClay, nAddObs, nAddGeo = 0, 0, 0, 0
        if nTry == 3:
            if qOre >= geoore and qObs >= geoobs:
                qOre -= geoore
                qObs -= geoobs
                nAddGeo = 1
            # vTimes.append(['Geo', nTime])
        elif nTry == 2:
            if qOre >= obsore and qClay >= obsclay:
                qOre -= obsore
                qClay -= obsclay
                nAddObs = 1
            # vTimes.append(['Obs', nTime])
        elif nTry == 1:
            if qOre >= clayore:
                qOre -= clayore
                nAddClay += 1
            # vTimes.append(['Cla', nTime])
        elif nTry == 0:
            if qOre >= oreore:
                qOre -= oreore
                nAddOre += 1
            # vTimes.append(['Ore', nTime])
        qOre += nOre
        qClay += nClay
        qObs += nObs
        qGeo += nGeo

        nOre += nAddOre
        nClay += nAddClay
        nObs += nAddObs
        nGeo += nAddGeo
        nTime -= 1
        if nTime == 0:
            if qGeo > nMax:
                # print(vTimes)
                # print(
                #     f'Ore={nOre}/{qOre} - Clay={nClay}/{qClay} - Obs={nObs}/{qObs} - Geo={nGeo}/{qGeo}')
                nMax = qGeo
            break
        if nAddOre + nAddClay + nAddObs + nAddGeo > 0:
            for x in range(4):
                bBusca = True
                if x == 3 and nObs == 0:
                    bBusca = False
                elif x == 2 and nClay == 0:
                    bBusca = False
                elif x == 1 and nClay >= obsclay:
                    bBusca = False
                elif x == 0 and nOre >= max(oreore, clayore, obsore, geoore):
                    bBusca = False
                else:
                    nAux = qGeo
                    for y in range(nTime):
                        nAux += (nGeo + y + 1)
                    if nAux < nMax:
                        bBusca = False
                if bBusca:
                    Gera(nTime, num, vNeed, (qOre, qClay,
                                             qObs, qGeo), (nOre, nClay, nObs, nGeo), x)
            break

    # print(num, qOre, qClay, qObs, qGeo)
    return


nMax = 0
nSum = 0
for (num, oreore, clayore, obsore, obsclay, geoore, geoobs) in vLines:
    vNeed = ((oreore, 0, 0), (clayore, 0, 0),
             (obsore, obsclay, 0), (geoore, 0, geoobs))
    nRet = 0
    nMax = 0
    for x in range(0, 2):
        Gera(24, num, vNeed, (0, 0, 0, 0), (1, 0, 0, 0), x)

    # print(num, num * nMax)
    nSum += (num * nMax)

print(nSum)  # 1356

nMax = 0
nSum = 1
for (num, oreore, clayore, obsore, obsclay, geoore, geoobs) in vLines[:3]:
    vNeed = ((oreore, 0, 0), (clayore, 0, 0),
             (obsore, obsclay, 0), (geoore, 0, geoobs))
    nRet = 0
    nMax = 0
    for x in range(0, 2):
        Gera(32, num, vNeed, (0, 0, 0, 0), (1, 0, 0, 0), x)

    # print(num, nMax)
    nSum *= nMax

print(nSum)  # 27720
