x, y = map(int, input().split())

if x < y:
    print(f'O JOGO DUROU {y-x} HORA(S)')
else:
    print(f'O JOGO DUROU {(y+24)-x} HORA(S)')
