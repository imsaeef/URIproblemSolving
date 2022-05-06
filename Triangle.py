a, b, c = map(float, input().split())
P = a + b + c
A = 0.5 * (a + b) * c
if (a + b) > c and (a + c) > b and (b + c) > a:
    P = a + b + c
    print(f'Perimetro = {P:0.1f}')
else:
    print(f'Area = {A:0.1f}')
