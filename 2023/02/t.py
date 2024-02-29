cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

s1 = s2 = 0
for lin in cal:
    lin = lin[5:]
    x, lin = lin.split(": ")
    lin = lin.replace(",", ";")
    r = g = b = 0
    for qtd_cor in lin.split("; "):
        q, cor = qtd_cor.split(" ")
        q = int(q)

        # Max: 12 red cubes, 13 green cubes, and 14 blue cubes
        if (
            (cor == "red" and q > 12)
            or (cor == "green" and q > 13)
            or (cor == "blue" and q > 14)
        ):
            x = "0"

        # take the Biggest
        if cor == "red":
            r = max(r, q)
        elif cor == "green":
            g = max(g, q)
        elif cor == "blue":
            b = max(b, q)
    s1 += int(x)
    s2 += r * g * b

print("Round 1:", s1)  # 2156
print("Round 2:", s2)  # 66909
# input2.txt return 8 and 2286, as defined in the site
