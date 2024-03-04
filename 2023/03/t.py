cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

for x in range(len(cal)):
    cal[x] = "." + cal[x] + "."

cal.insert(0, "." * len(cal[0]))
cal.append("." * len(cal[0]))

digits = "0123456789"
digitsPoint = digits + "."


def TestaNum(lin, inic, fim):
    for x in range(lin - 1, lin + 2):
        for y in range(inic - 1, fim + 2):
            if not cal[x][y] in digitsPoint:
                return int(cal[lin][inic : fim + 1])
    return 0


s1 = s2 = 0
for x in range(1, len(cal) - 1):
    y = 1
    while y <= len(cal[0]) - 1:
        if cal[x][y] in digits:
            inic = y
            y += 1
            while cal[x][y] in digits:
                y += 1
            fim = y - 1
            s1 += TestaNum(x, inic, fim)
        else:
            y += 1


def buscaNum(lin, col, v):
    if cal[lin][col] in digits:
        while cal[lin][col - 1] in digits:
            col -= 1
        s = ""
        while cal[lin][col] in digits:
            s += cal[lin][col]
            col += 1

        v.append(int(s))
        return


def TestaMult(lin, col):
    v = []
    for x in range(lin - 1, lin + 2):
        if cal[x][col] in digits:
            buscaNum(x, col, v)
        else:
            buscaNum(x, col - 1, v)
            buscaNum(x, col + 1, v)

    if len(v) > 1:
        return v[0] * v[1]
    else:
        return 0


for x in range(1, len(cal) - 1):
    for y in range(1, len(cal[0])):
        if cal[x][y] == "*":
            s2 += TestaMult(x, y)

print("Round 1:", s1)  # 546312
print("Round 2:", s2)  # 87449461
# input2.txt return 4361 and 467835, as defined in the site
