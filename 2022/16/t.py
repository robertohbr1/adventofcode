import time
import re
from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().splitlines()

FirstElement = 'AA'

vLines = []
for txt in cal:
    valve, *valves = re.findall(r"[A-Z]{2}", txt)
    qtd = int(re.findall(r"-?\d+", txt)[0])
    vLines.append([valve, valves, qtd, 0, []])


def Find(orig):
    vOrig = vLines[0]
    for x in vLines:
        if x[0] == orig:
            vOrig = x
            break
    return vOrig


def CalcPath(vOrig):
    for x in vOrig[1]:
        vActual = Find(x)
        if vActual[3] > vOrig[3] + 1:
            vActual[3] = vOrig[3] + 1
            vActual[4] = vOrig[4].copy()
            vActual[4].append(vActual[0])
            CalcPath(vActual)


vPath = []


def Clear(vOrig):
    for x in vLines:
        x[3] = 9999999
        x[4] = []
    vOrig[3] = 0


def CreatePaths():
    global vPath
    for x in vLines:
        if x[2] > 0 or x[0] == FirstElement:
            Clear(x)
            CalcPath(x)
            vPath.append([x[0], []])
            for y in vLines:
                if y[0] != x[0] and y[2] > 0 and len(y[4]) > 0:
                    vPath[-1][1].append(y[4])


CreatePaths()
# print(vLines)
# print(vPath)


def FindPaths(vInic):
    for x in vPath:
        if x[0] == vInic:
            return x[1]
    return []


def Testa(vJorn, sSoma, RestTimeOrig, CriaPaths):
    if CriaPaths:
        if vJorn != FirstElement:
            # vAppend = str(sSoma) + ',' + vJorn.replace(FirstElement + ',', '')
            vAppend = [sSoma, vJorn.replace(FirstElement + ',', '')]
            if not vAppend in vSavePaths:
                vSavePaths.append(vAppend)

    vBusca = FindPaths(vJorn.split(',')[-1])

    sSomaMax = sSoma
    vJornRet = vJorn
    for x in vBusca:
        if x[-1] in vJorn.split(','):
            continue
        RestTime = RestTimeOrig - len(x) - 1
        if RestTime < 1:
            continue

        vNew = Find(x[-1])

        sSomaFinal = sSoma + (RestTime * vNew[2])

        sSomaAux, vJornAux = Testa(
            vJorn + ',' + x[-1],  sSomaFinal, RestTime, CriaPaths)

        if sSomaAux > sSomaMax:
            sSomaMax = sSomaAux
            vJornRet = vJornAux

    return sSomaMax, vJornRet


TotalTime = 30
sSomaA, sPath = Testa(FirstElement, 0, TotalTime, False)
print(f'Turn 1: {sSomaA} - {sPath}')  # 1673

# Turn 2


def Unique(xPath1, xPath2):
    for x in xPath1.split(','):
        if xPath2.find(x) != -1:
            return False
    return True


start = time.time()

vSavePaths = []
TotalTime = 26
sSomaA, sPath = Testa(FirstElement, 0, TotalTime, True)
print(f'Tempo cria paths turno 2: {time.time() - start}')

nSumTot = 0
sPath1 = []
sPath2 = []

print(f'Paths: {len(vSavePaths)}')
nMax = 0
# Calculate the Maximum Value to use below
for Path1 in vSavePaths:
    nMax = max(nMax, Path1[0])

for Path1 in vSavePaths:
    nSum1, vPath1 = Path1
    if nSum1 + nMax > nSumTot:
        # Path1 Value + Max Value "Need to be" > The Greatest Finded Value
        # This can reduce the time to just 3% - Before 390'' - After 13''
        for Path2 in vSavePaths:
            nSum2, vPath2 = Path2
            n = int(nSum1) + int(nSum2)
            if n > nSumTot:
                if Unique(vPath1, vPath2):
                    nSumTot = n
                    sPath1 = vPath1
                    sPath2 = vPath2

# Turn 2: 2343 - Path1: AA,OK,HF,CQ,GV,HX,IR - Path2: AA,GR,JI,XM,OH,BX,GB
print(f'Turn 2: {nSumTot} - Path1: AA,{sPath1} - Path2: AA,{sPath2}')

print(f'Tempo total turno 2: {time.time() - start}')
