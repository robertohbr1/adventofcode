t = 'v<<A>A>^Av<<A>>^AAvAA<^A>A<vA>^AAv<<A>^A>AvA^AAAv<<A>A>^AvA<^A>Av<<A>>^AvA^Av<<A>A>^Av<<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^Av<<A>^A>AvA^Av<<A>A>^AvA<^A>A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^AvA<^A>A<vA<AA>>^AvAA<^A>AA<vA>^AAv<<A>^A>AvA^AAv<<A>A>^AvA<^A>AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^AvA<^A>A<vA>^Av<<A>^A>AvA^AAv<<A>A>^Av<<A>>^AAvAA<^A>A<vA>^AAv<<A>^A>AvA^AAv<<A>A>^AvA<^A>A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A'

vDirs = [['#', '^', 'A'], ['<', 'v', '>']]
vKeys = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['#', '0', 'A']]


def Ret(t, y, x, v):
    ret = ''
        
    for c in t:
        match c:
            case '<':
                x -= 1
            case '>':
                x += 1
            case '^':
                y -= 1
            case 'v':
                y += 1
            case 'A':
                ret += v[y][x]
        if v[y][x] == '#':
            raise ('Error')
    return ret

s = t
for x in range(4):
    s = Ret(s, 0, 2, vDirs)
    print(s)

s = Ret(s, 3, 2, vKeys)
print(s)