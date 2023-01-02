from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read().strip()

vDir = [x for x in cal]

vRocks = [['@@@@'], [' @', '@@@', ' @'], [
    '  @', '  @', '@@@'], ['@', '@', '@', '@'], ['@@', '@@']]

Arena = ['#' * 7]
nRock = 0
nDir = 0
nTop = 0


def MostraArena():
    global Arena
    for lin in Arena[::-1]:
        print('|' + lin[::-1] + '|')
    print()


def AddArena(Rock):
    global Arena
    for lin in Rock[::-1]:
        Arena.append(lin[::-1])


def Ajusta(xRock):
    vRet = []
    for x in xRock:
        vRet.append((' ' * 2 + x + ' ' * 7)[0:7])
    return vRet


def Troca(Rock):
    global Arena
    global nTop
    for z in range(len(Rock)):
        Arena[-(z + nTop)] = Arena[-(z + nTop)].replace('@', '#')


def PodeDescer(Rock):
    global Arena
    global nTop
    for z in range(len(Rock)):
        for k in range(7):
            if Arena[-(z + nTop)][k] == '@':
                if Arena[-(z + nTop + 1)][k] == '#':
                    Troca(Rock)
                    return False

    for z in range(len(Rock) - 1, -1, -1):
        for k in range(7):
            if Arena[-(z + nTop)][k] == '@':
                Arena[-(z + nTop + 1)] = Arena[-(z + nTop + 1)][0:k] + \
                    '@' + Arena[-(z + nTop + 1)][k + 1:]
                Arena[-(z + nTop)] = Arena[-(z + nTop)][0:k] + \
                    ' ' + Arena[-(z + nTop)][k + 1:]
    if Arena[-1].strip() == '':
        Arena.pop()
    else:
        nTop += 1

    return True


nCut = 100


def Lasts():
    global Arena
    s = ''
    for x in range(1, 31):
        s += Arena[-x]
        if x == len(Arena):
            break
    return s


def JaExiste():
    global Arena
    if len(Arena) < 100:
        return False

    for x in range(1, 31):
        if Arena[x] != Arena[len(Arena) - 31 + x]:
            return False
    return True


def Teste(nMax):
    global Arena, nRock, nDir, nTop
    Arena = ['#' * 7]

    vSave = []
    vPos = []

    nRock = 0
    nDir = 0
    nArenaCut = 0
    x = 0
    while x < nMax:
        Rock = Ajusta(vRocks[nRock])

        for y in range(4):
            bMove = True
            if vDir[nDir] == '>':
                for z in Rock:
                    if z[-1] != ' ':
                        bMove = False
                        break
                if bMove:
                    for z in range(len(Rock)):
                        Rock[z] = ' ' + Rock[z][0:-1]
            else:
                for z in Rock:
                    if z[0] != ' ':
                        bMove = False
                        break
                if bMove:
                    for z in range(len(Rock)):
                        Rock[z] = Rock[z][1:] + ' '

            nDir = (nDir+1) % len(vDir)

        nTop = 1
        AddArena(Rock)

        while True:
            if PodeDescer(Rock):
                bMove = True
                # Atention: The Move is inverted, because the array is inverted
                if vDir[nDir] == '<':
                    for z in range(len(Rock)):
                        sLin = Arena[-(z + nTop)] + '#'
                        for k in range(7):
                            if sLin[k] == '@':
                                if sLin[k + 1] == '#':
                                    bMove = False
                                    break
                    if bMove:
                        for z in range(len(Rock)):
                            sLin = Arena[-(z + nTop)]
                            for k in range(6, -1, -1):
                                if sLin[k] == '@':
                                    sLin = sLin[0:k] + ' @' + sLin[k+2:]
                            Arena[-(z + nTop)] = sLin
                else:
                    for z in range(len(Rock)):
                        sLin = '#' + Arena[-(z + nTop)]
                        for k in range(1, 8):
                            if sLin[k] == '@':
                                if sLin[k - 1] == '#':
                                    bMove = False
                                    break
                    if bMove:
                        for z in range(len(Rock)):
                            sLin = Arena[-(z + nTop)]
                            for k in range(7):
                                if sLin[k] == '@':
                                    sLin = sLin[0:k - 1] + '@ ' + sLin[k+1:]
                            Arena[-(z + nTop)] = sLin
                nDir = (nDir+1) % len(vDir)
            else:
                break

        # MostraArena()

        nRock = (nRock+1) % len(vRocks)

        # Save the Directions Position, the Rocks Position, last 30 lines
        xPos = str(nDir) + ',' + str(nRock) + ',' + Lasts()
        # if Find this configuration in vSave, multiply the difference. Without this, the procedure will consume all memory
        if xPos in vSave:
            oldX, oldLen = vPos[vSave.index(xPos)]
            difTop = len(Arena) - oldLen
            difX = x - oldX
            nMult = (nMax - x) // difX
            nArenaCut += nMult * difTop
            x += nMult * difX
            # Clear to not find again, because lasts a few steps
            vSave = []
            vPos = []

        vSave.append(xPos)
        vPos.append([x, len(Arena)])

        x += 1

    # MostraArena()
    return nArenaCut + len(Arena) - 1


print('Turn 1: ', Teste(2022))  # 3188
print('Turn 2: ', Teste(1000000000000))  # 1591977077342
