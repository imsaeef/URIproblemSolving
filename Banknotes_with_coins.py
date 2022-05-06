# For Banknotes
value = float(input())
print("NOTAS:")

for i in [100, 50, 20, 10, 5, 2]:
    print(f'{int(value / i)} nota(s) de R$ {i}.00')
    value = float(f'{value % i:.2f}')

# For Coins
print("MOEDAS:")

for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f'{int(value / i)} moeda(s) de R$ {i:.2f}')
    value = float(f'{value % i:.2f}')
