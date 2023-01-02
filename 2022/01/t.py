from rich import print

cal = open('input.txt', 'r', encoding='utf-8').read()
cal = [sum(map(int, i.strip().split('\n'))) for i in cal.split('\n\n')]

print("[red]Maior[/red]", max(cal))

cal.sort()

print("[red]Soma 3 maiores[/red]", sum(cal[-3:]))
