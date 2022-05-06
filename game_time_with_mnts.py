a, b, c, d = map(int, input().split())

dif = ((c*60)+d) - ((a*60)+b)
if dif <= 0:
    dif = dif + 24*60

hours = dif // 60
minutes = dif % 60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
