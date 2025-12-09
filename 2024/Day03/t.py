cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

total1 = total2 = 0
vSum = True
for lin in cal:
    x = 0
    while x < len(lin):
        if (lin[x:x+4]) == 'mul(':
            vOk = True
            x += 4
            s1 = s2 = ''
            while x < len(lin) and lin[x].isdigit():
                s1 += lin[x]
                x += 1
            if lin[x] != ',':
                vOk = False
            if vOk:    
                x += 1
                while x < len(lin) and lin[x].isdigit():
                    s2 += lin[x]
                    x += 1
                if lin[x] != ')':
                    vOk = False
            if vOk:                
                total1 += int(s1) * int(s2)
                if vSum:
                    total2 += int(s1) * int(s2)
        elif (lin[x:x+4]) == 'do()':
            x += 4
            vSum = True
        elif (lin[x:x+7]) == "don't()":
            x += 7
            vSum = False
        else:
            x += 1

print('Answer 1: ', total1) # 174960292

print('Answer 2: ', total2) # 428
