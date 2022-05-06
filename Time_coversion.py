sec = int(input())

mint = sec // 60
sec = sec % 60

hr = mint // 60
mint = mint % 60

print(f'{hr}:{mint}:{sec}')
