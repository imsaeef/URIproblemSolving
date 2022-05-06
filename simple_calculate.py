p1 = input().split(' ')[1:]
p2 = input().split(' ')[1:]

ttl = int(p1[0]) * float(p1[1]) + int(p2[0]) * float(p2[1])

print(f'VALOR A PAGAR: R$ {ttl:.2f}')
