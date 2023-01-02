cal = open('input.txt', 'r', encoding='utf-8').read()


def mostra(tam):
    t = ''
    i = 0
    for s in cal:
        i += 1
        x = t.find(s)
        if x > -1:
            t = t[x + 1:]
        t += s
        if len(t) == tam:
            break
    print(t, i)


mostra(4)
mostra(14)
