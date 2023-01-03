cal = open('input.txt', 'r', encoding='utf-8').read()
cal = [sum(map(int, i.strip().split('\n'))) for i in cal.split('\n\n')]

print("Round 1:", max(cal))

cal.sort()

print("Round 2:", sum(cal[-3:]))
